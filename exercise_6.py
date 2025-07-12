import requests
from bs4 import BeautifulSoup
import re

def scrape_imdb_movies():
    """Scrapes top 10 movies from IMDb list with details"""
    print("="*50)
    print("EXERCISE 6: Scraping Movie Details from IMDb")
    print("="*50)

    # Configure request
    url = "https://www.imdb.com/list/ls091294718/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/'
    }

    try:
        # Fetch the webpage
        print("Fetching IMDb data...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise error for bad status

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Found movie list. Extracting top 10 movies...\n")

        # Find all movie containers
        movies = []
        for container in soup.select('.lister-item-content')[:10]:
            # Extract title
            title_elem = container.select_one('.lister-item-header a')
            title = title_elem.text.strip() if title_elem else "Unknown Title"

            # Extract year
            year_elem = container.select_one('.lister-item-year')
            if year_elem:
                year_match = re.search(r'\d{4}', year_elem.text)
                year = year_match.group(0) if year_match else "N/A"
            else:
                year = "N/A"

            # Extract summary
            summary_elem = container.select_one('p:nth-of-type(2)')
            summary = summary_elem.text.strip() if summary_elem else "No summary available"

            movies.append({
                'title': title,
                'year': year,
                'summary': summary
            })

        # Display results
        print("Top 10 Movies from IMDb:")
        print("-"*50)
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie['title']} ({movie['year']})")
            print(f"   Summary: {movie['summary'][:100]}{'...' if len(movie['summary']) > 100 else ''}")
            print("-"*50)

        print("\nScraping completed successfully!")

    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error occurred: {e}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    scrape_imdb_movies()