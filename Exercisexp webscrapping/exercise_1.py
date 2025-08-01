
from bs4 import BeautifulSoup

def exercise1():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sports World</title>
        <style>
            body { font-family: Arial, sans-serif; }
            header, nav, section, article, footer { margin: 20px; padding: 15px; }
            nav { background-color: #333; }
            nav a { color: white; padding: 14px 20px; text-decoration: none; display: inline-block; }
            nav a:hover { background-color: #ddd; color: black; }
            .video { text-align: center; margin: 20px 0; }
        </style>
    </head>
    <body>

        <header>
            <h1>Welcome to Sports World</h1>
            <p>Your one-stop destination for the latest sports news and videos.</p>
        </header>

        <nav>
            <a href="#football">Football</a>
            <a href="#basketball">Basketball</a>
            <a href="#tennis">Tennis</a>
        </nav>

        <section id="football">
            <h2>Football</h2>
            <article>
                <h3>Latest Football News</h3>
                <p>Read about the latest football matches and player news.</p>
                <div class="video">
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/football-video-id" frameborder="0" allowfullscreen>
                    </iframe>
                </div>
            </article>
        </section>

        <section id="basketball">
            <h2>Basketball</h2>
            <article>
                <h3>NBA Highlights</h3>
                <p>Watch highlights from the latest NBA games.</p>
                <div class="video">
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/basketball-video-id" frameborder="0" allowfullscreen>
                    </iframe>
                </div>
            </article>
        </section>

        <section id="tennis">
            <h2>Tennis</h2>
            <article>
                <h3>Grand Slam Updates</h3>
                <p>Get the latest updates from the world of Grand Slam tennis.</p>
                <div class="video">
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/tennis-video-id" frameborder="0" allowfullscreen></iframe>
                </div>
            </article>
        </section>

        <footer>
            <form action="mailto:contact@sportsworld.com" method="post" enctype="text/plain">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br>
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email"><br>
                <label for="message">Message:</label><br>
                <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
                <input type="submit" value="Send">
            </form>
        </footer>
        </body>
    </html>
        """

    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.title.string
    print(f"1. Page Title: {title}")

    print("\n2. Paragraphs:")
    for i, p in enumerate(soup.find_all('p'), 1):
        print(f"   {i}. {p.get_text()}")

    print("\n3. Links:")
    for i, a in enumerate(soup.find_all('a'), 1):
        print(f"   {i}. {a.get('href')}")

if __name__ == "__main__":
    exercise1()
