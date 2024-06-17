from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import AnyStr
import requests
import re


class CrawlerBot:
    """
    クローラーボット
    ==========

    CrawlerBotクラスは、ウェブページをクロールしてデータを抽出するために使用されます。

    メソッド
    -------
    __init__(url: str)
        与えられたURLでCrawlerBotオブジェクトを初期化します。URLにGETリクエストを送り、HTMLページを取得します、
        を取得し、html_page属性に格納します。また、html_pageでBeautifulSoupオブジェクトを作成する。

    css_selector(selector: str) -> タグ
        selectorで指定されたCSSセレクタを使ってHTML要素を検索する。最初に見つかったマッチをbs4.Tagオブジェクトとして返します。

    regular_expression(req: str) -> AnyStr
        HTMLページ内でreqで指定された正規表現パターンを検索する。最初にマッチしたグループを返します。

    例外
    ----------
    例外
        最初のリクエスト要素が CSS セレクタで見つからない場合に発生します。

    属性
    ----------
    html_page : str
        リクエストされたWebページのHTMLコンテンツ。

    bs4 : BeautifulSoup
        要求されたWebページのHTMLコンテンツを表すBeautifulSoupオブジェクト。

    """
    def __init__(self, url: str):
        html_resp = requests.get(url)
        html_resp.raise_for_status()
        self.html_page = html_resp.text
        self.bs4 = BeautifulSoup(self.html_page, 'html.parser')

    def css_selector(self, selector: str) -> Tag:
        initial_request_id = self.bs4.select_one(selector)
        if initial_request_id is None:
            raise Exception("Initial request not found")
        return initial_request_id

    def regular_expression(self, req: str) -> AnyStr:
        return re.search(
            req,
            self.html_page
        ).group(1)

