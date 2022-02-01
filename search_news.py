import time
import requests


def search_news(top):
    # トップページに掲載されている30記事のidをとってくる。
    top30id = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

    # 30記事のidを入れる空の配列を定義。
    top30url = []
    # 30記事のid情報が入った配列「top30id」を30回繰り返し、idに入れ、30個のurlを生成する。それを配列「top30url」に追加。
    for id in top30id.json()[0:top]:
        top30url.append(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")

    news = []
    for i in range(len(top30url)):
        # 各記事の情報を取得し、変数「response」に定義。
        response = requests.get(top30url[i])
        # 1秒待ってね。
        time.sleep(1)
        dic = response.json()
        # 「'title'」の情報を変数「title」に定義。
        title = dic['title']
        # 「'url'」の情報を変数「url」に定義。
        if 'url' in dic:
            url = dic['url']
        else:
            url = ""
        # 追加
        news.append(f"'title': '{title}', 'link': '{url}'")
    return news
