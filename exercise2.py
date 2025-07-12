import requests

def exercise2():
    url = "https://en.wikipedia.org/robots.txt"
    response = requests.get(url)
    print("Wikipedia robots.txt (first 10 lines):\n")
    print('\n'.join(response.text.split('\n')[:10]))

if __name__ == "__main__":
    exercise2()