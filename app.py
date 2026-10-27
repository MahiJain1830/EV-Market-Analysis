from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EV Market Analysis</title>
    </head>
    <body>
        <h1>Electric Vehicle Market Analysis &amp; Insights</h1>
        <p>Welcome to our Electric Vehicle Market Analysis project!</p>
        <p>
            We are exploring EV sales, manufacturers, battery technologies,
            vehicle range, customer ratings, and manufacturing countries.
        </p>
        <h2>Dashboard Coming Soon</h2>
        <p>Our interactive Tableau dashboard will be integrated here.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)