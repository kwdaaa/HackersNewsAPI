from search_news import search_news


def main():
    # 入力
    top = 5
    # 処理
    all_news = search_news(top=top)
    # 出力
    for news in all_news:
        print(news)


if __name__ == '__main__':
    main()
