import sys
import os


def main():
    print("starting convertion of pdf files to djvu...")
    dir = sys.argv[1]
    pdf_files = []

    for r, _, f in os.walk(dir):
        for item in f:
            if '.pdf' in item:
                pdf_files.append(os.path.join(r, item[:len(item)-4]))

    for file in pdf_files:
        print("current converting ", file, "to djvu...")
        os.system(f"pdf2djvu -o {file+'.djvu'} {file+'.pdf'}") 

    print("successfully converted", len(pdf_files), "into djvus!")
    

if __name__ == "__main__":
    main()
