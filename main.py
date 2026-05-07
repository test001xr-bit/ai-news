import feedparser
import json
from datetime import datetime

SOURCES = [
    "https://hnrss.org/frontpage",
    "https://www.reddit.com/r/programming/.rss"
]

def fetch_news():
    items = []

    for url in SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            items.append({
                "title": entry.title,
                "link": entry.link
            })

    return items


def build_html(news):
    html = "<html><head><meta charset='utf-8'><title>AI News</title></head><body>"
    html += f"<h1>AI News - {datetime.now()}</h1>"

    for n in news:
        html += f"<p><a href='{n['link']}'>{n['title']}</a></p>"

    html += "</body></html>"
    return html


def main():
    news = fetch_news()
    html = build_html(news)

    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("done")


if __name__ == "__main__":
    main()