from flask import Flask
from redis import Redis

app = Flask(__name__)

cache = Redis(host="redis", port=6379)

@app.route("/")
def main_page():
    visits = cache.incr("quentin_hits")

    return f"""
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Quentin docker compose site</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding: 25px;">
            <h1>Welcome to Quentin's Docker compose Site</h1>

            <img src="/static/Welcome-Banner.png" width="300"/>

            <p>This page is running inside a Docker container.</p>
            <p>Redis is tracking how many times it gets opened.</p>

            <h2>Visits: {visits}</h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
