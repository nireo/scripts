import requests
from bs4 import BeautifulSoup


def has_number(string):
    return any(char.isdigit() for char in string)


def main():
    print(f"Parsing https://github.com/nireo")
    page = requests.get(f"https://github.com/nireo")
    soup = BeautifulSoup(page.content, "html.parser")

    # Get the contributions this year
    for header in soup.find_all("h2"):
        text = header.get_text()
        if has_number(text):
            print(text)
            break

    # Get the contributions today
    days = soup.find_all(attrs={"class": "day"})
    print(f"{days[len(days)-1]['data-count']} contributions today!")


if __name__ == '__main__':
    main()

