def exercise4():
    def has_title(url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, 'html.parser')
            return bool(soup.title and soup.title.string.strip())
        except Exception:
            return False

    urls = [
        "https://www.google.com",
        "https://en.wikipedia.org/wiki/Main_Page",
        "https://www.example.com/no-title-page"
    ]

    print("Page title check:")
    for url in urls:
        print(f"- {url}: {'Has title' if has_title(url) else 'No title'}")

if __name__ == "__main__":
    exercise4()

