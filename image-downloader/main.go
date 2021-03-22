package main

import (
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/gocolly/colly"
)

var (
	thread = flag.String("thread", "", "the thread to download images from")
	where  = flag.String("where", "./", "where to save all of the images")
)

func init() {
	flag.Parse()

	if *thread == "" {
		log.Fatalf("you need to provide a flag thread")
	}
}

func ByteCountDecimal(b int64) string {
	const unit = 1000
	if b < unit {
		return fmt.Sprintf("%d B", b)
	}
	div, exp := int64(unit), 0
	for n := b / unit; n >= unit; n /= unit {
		div *= unit
		exp++
	}
	return fmt.Sprintf("%.1f %cB", float64(b)/float64(div), "kMGTPE"[exp])
}

func ParseFilename(src string) string {
	splitted := strings.Split(src, "/")
	return splitted[len(splitted)-1]
}

func main() {
	if *where != "./" {
		_, err := os.Stat(*where)
		if os.IsNotExist(err) {
			os.Mkdir(*where, os.FileMode(0775))
		}
	}

	c := colly.NewCollector()
	c.OnHTML("img[src]", func(e *colly.HTMLElement) {
		// download only the images in the thread
		if e.Attr("alt") == "" || e.Attr("alt") == "4chan" {
			return
		}

		// remove the s flag from image url
		src := strings.Replace(e.Attr("src"), "s", "", -1)
		filename := ParseFilename(src)
		resp, err := http.Get("http:" + src)
		if err != nil {
			log.Printf("failed to load image: %s", err)
			return
		}
		defer resp.Body.Close()

		file, err := os.Create(*where + "/" + filename)
		if err != nil {
			log.Printf("failed creating a file: %s", err)
			return
		}
		defer file.Close()

		size, err := io.Copy(file, resp.Body)
		if err != nil {
			log.Printf("failed parsing request body")
			return
		}

		log.Printf("downloaded file %s with size %s", filename, ByteCountDecimal(size))
	})

	c.Visit(*thread)
}
