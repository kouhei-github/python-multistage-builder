import requests
import json
from requests import Response
from requests.cookies import RequestsCookieJar


class HttpRequest:
    """
    HttpRequestクラスはHTTPリクエストを実行するメソッドを提供する。

    メソッドを提供します：
        - login(lsd, datr, initial_request_id, phone, password)： ログイン・リクエストを実行します。
        - get_after_login_page(cookies)：ログイン・リクエストを実行する： ログイン後のメインページのHTMLコンテンツを取得します。
        - get_email_inbox(クッキー, email_inbox)： 指定したユーザのメールボックス・データを取得します。

    静的メソッド：
        - login(lsd, datr, initial_request_id, phone, password)： ログイン・リクエストを実行する。
        - get_after_login_page(cookies)： ログイン後のメインページのHTMLコンテンツを取得します。
        - get_email_inbox(クッキー, email_inbox)： 指定されたユーザのメールボックス・データを取得します。

    属性：
        なし
    """
    @staticmethod
    def login(
            lsd: str,
            datr: str,
            initial_request_id: str,
            phone: str,
            password: str
    ) -> Response:
        login = requests.post(
            "https://www.messenger.com/login/password/",
            cookies={"datr": datr},
            data={
                "lsd": lsd,
                "initial_request_id": initial_request_id,
                "email": phone,
                "pass": password
            },
            allow_redirects=False  # do not follow 302
        )

        if not login.status_code == 302:
            raise Exception("Login failed")
        return login

    @staticmethod
    def get_after_login_page(cookies: RequestsCookieJar) -> str:
        inbox_html_resp = requests.get(
            "https://www.messenger.com",
            cookies=cookies
        )
        return inbox_html_resp.text

    @staticmethod
    def get_email_inbox(cookies: RequestsCookieJar, email_inbox: dict) -> dict:
        inbox_resp = requests.post(
            "https://www.messenger.com/api/graphql/",
            cookies=cookies,
            data={
                "fb_dtsg": email_inbox["dtsg"],
                "doc_id": email_inbox["doc_id"],
                "variables": json.dumps({
                    "deviceId": email_inbox["device_id"],
                    "requestId": 0,
                    "requestPayload": json.dumps({
                        "database": 1,
                        "version": email_inbox["schema_version"],
                        "sync_params": json.dumps({})
                    }),
                    "requestType": 1
                })
            }
        )
        inbox_resp.raise_for_status()

        return json.loads(inbox_resp.text)