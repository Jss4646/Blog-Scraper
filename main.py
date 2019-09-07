from flask import Flask, render_template, jsonify

import scraper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/get-articles/<website>')
def get_articles(website):
    websites = [
        "The Crazy Programmer",
        "CSS Tricks",
        "Stack Abuse",
    ]
    website = website.replace('-', ' ')

    if website in websites:
        articles = scraper.get_articles(website)
        return jsonify(articles)
    else:
        return "That's not a valid website"


@app.route('/loading-icon.svg')
def get_loading_icon():
    return app.send_static_file('loading-icon.svg')


if __name__ == '__main__':
    app.run()
