import html2text
import requests
from bs4 import BeautifulSoup

urls = {
    "The Crazy Programmer": "https://www.thecrazyprogrammer.com",
    "CSS Tricks": "https://css-tricks.com/archives",
    "Stack Abuse": "https://stackabuse.com",
}


class BadUrlError(Exception):
    pass


h = html2text.HTML2Text()
h.ignore_links = False


def get_articles(site_name):
    articles = []

    home_page_response = requests.get(urls[site_name])
    home_page_html = BeautifulSoup(home_page_response.text, "html.parser")
    articles_html = home_page_html.select("article")

    summery_texts = []

    for i in articles_html:
        if i.p is not None:
            if len(i.p.text) > 0:
                html2text_summery = h.handle(i.p.text)
                stripped_summery = html2text_summery.strip()
                summery = stripped_summery.replace("\n", " ")
                summery = summery.replace("… Read More »", "")
                summery = summery.replace("… Read article", "")
                summery = summery[:400] if len(summery) > 418 else summery
                summery += '...'
                summery_texts.append(summery)

    headers = [i.h2.text.strip() for i in articles_html if i.h2 is not None]
    links = [i.a["href"] for i in articles_html]

    if links[0][0] == "/":
        links = list(map(lambda x: urls[site_name] + x, links))
    elif links[0][:5] == "https":
        pass
    else:
        raise BadUrlError(f"{links[0]} isn't in the right format")

    for header, summery_text, link in zip(headers, summery_texts, links):
        article_data = {
            "header": header,
            "summeryText": summery_text,
            "link": link,
        }
        articles.append(article_data)

    return articles
