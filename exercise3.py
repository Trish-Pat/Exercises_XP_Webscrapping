import requests
from bs4 import BeautifulSoup

def exercise3():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print("Wikipedia headers (first 10):")
    headers = []
    for level in range(1, 7):  # h1 to h6
        headers.extend(soup.find_all(f'h{level}'))

    for i, header in enumerate(headers[:10], 1):
        print(f"{i}. {header.get_text().strip()}")

if __name__ == "__main__":
    exercise3()

