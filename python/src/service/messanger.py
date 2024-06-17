import re


class Messanger:
    """
    Messanger` クラスは静的メソッド `get_email_inbox_params` を提供し、メールの受信箱を表す HTML ページから特定のパラメータを抽出します。

    このメソッドは1つのパラメータを受け取る：
    - inbox_html_page` : str : メールの受信トレイページの HTML コンテンツ。

    戻り値
    抽出されたパラメータを含む辞書：
    - dtsg` : str : `dtsg` パラメータの値。
    - schema_version` : str : `schema_version` パラメータの値。
    - doc_id` : str : `doc_id` パラメータの値。
    - device_id` : str : `device_id` パラメータの値。
    """
    @staticmethod
    def get_email_inbox_params(inbox_html_page: str)->dict:
        dtsg = inbox_html_page.split('["DTSGInitialData",[],{"token":"')[1].split('"},')[0]

        pattern = r'\\\"version\\\":([0-9]+)}'
        schema_version = re.search(
            pattern,
            inbox_html_page
        ).group(1)

        doc_id = inbox_html_page.split('"queryID":"')[1].split('","variables"')[0]

        device_id = inbox_html_page.split('deviceId":"')[1].split('",')[0]

        return {
            "dtsg": dtsg,
            "schema_version": schema_version,
            "doc_id": doc_id,
            "device_id": device_id
        }