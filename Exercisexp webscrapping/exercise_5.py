import requests
from bs4 import BeautifulSoup
from datetime import datetime

def exercise5():
    current_year = datetime.now().year
    url = "https://www.cisa.gov/news-events/cybersecurity-advisories"
    params = {'f[0]': 'advisory_type:93'}  # Security Advisory filter

    try:
        response = requests.get(url, params=params, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        count = sum(1 for tag in soup.select('time') if str(current_year) in tag.text)
        print(f"US-CERT Security Alerts in {current_year}: {count}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    exercise5()