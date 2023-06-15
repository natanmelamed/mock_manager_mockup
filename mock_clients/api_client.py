import json
import requests
from typing import Union


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url: str = base_url

    def get(self, url_path: str, param: dict = None) -> dict:
        return self.format_response_by_type(
            requests.get(f"{self.base_url}/{url_path}", params=param))

    def post(self, url_path: str, config: dict) -> dict:
        return self.format_response_by_type(
            requests.post(f"{self.base_url}/{url_path}", data=json.dumps(config)))

    @staticmethod
    def format_response_by_type(response: any) -> Union[str, dict, list]:
        if response.headers.get('content-type') == 'application/json':
            return response.json()
        else:
            return response.text
