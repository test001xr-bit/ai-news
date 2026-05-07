import datetime

def main():
    now = datetime.datetime.now()

    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <body>
        <h1>AI News System</h1>
        <p>Generated at: {now}</p>
        </body>
        </html>
        """)

if __name__ == "__main__":
    main()