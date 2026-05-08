import feedparser
import os
import google.generativeai as genai
from datetime import datetime

# RSS源（你可以以后自己加）
SOURCES = [
    "https://hnrss.org/frontpage",
    "https://www.reddit.com/r/programming/.rss"
]

# 初始化 Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def ai_process(title):
    prompt = f"""
你是一个全球科技新闻分析助手。

请对下面英文新闻做处理：

1. 翻译成中文
2. 写一句话总结
3. 判断重要性（高/中/低）
4. 判断是否可能是噪音/营销（是/否）

新闻标题：
{title}

输出格式：
中文标题：
一句话总结：
重要性：
是否噪音：
"""

    try:
        result = model.generate_content(prompt)
        return result.text
    except Exception as e:
        return f"AI处理失败: {str(e)}"


def fetch_news():
    news_list = []

    for url in SOURCES:
        feed = feedparser.parse(url)

        for entry in feed.entries[:8]:
            summary = ai_process(entry.title)

            news_list.append({
                "title": entry.title,
                "link": entry.link,
                "summary": summary
            })

    return news_list


def build_html(news):
    html = "<html><meta charset='utf-8'><body>"
    html += f"<h1>AI News Dashboard</h1>"
    html += f"<p>{datetime.now()}</p><hr>"

    for n in news:
        html += f"<h3><a href='{n['link']}'>{n['title']}</a></h3>"
        html += f"<pre>{n['summary']}</pre><hr>"

    html += "</body></html>"
    return html


def main():
    news = fetch_news()

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(build_html(news))

    print("done")


if __name__ == "__main__":
    main()