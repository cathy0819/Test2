import requests
import logging

logger = logging.getLogger(__name__)


class HttpRequest:
    def __init__(self):
        self.session = requests.Session()

    def send(self, method, url, headers=None, params=None, data=None, json=None, timeout=10):
        try:
            logger.info(
                f"发送 {method.upper()} 请求: URL={url}, headers={headers}, params={params}, data={data}, json={json}")
            response = self.session.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout
            )
            #response.raise_for_status()  # 如果状态码不是2xx，则抛出异常
            try:
                return response.json()
            except ValueError:
                return response.text

        except requests.RequestException as e:
            logger.error(f"HTTP请求失败：{e}")
            raise

    def get(self, url, headers=None, params=None, timeout=10):
        return self.send("GET", url, headers=headers, params=params, timeout=timeout)

    def post(self, url, headers=None, data=None, json=None, timeout=10):
        return self.send("POST", url, headers=headers, data=data, json=json, timeout=timeout)
