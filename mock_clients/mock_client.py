from mock_clients.api_client import ApiClient
from common.json_parser import load_data_from_json_file
import os
from mock_clients import options


class MockClient(ApiClient):
    def __init__(self, pack_name: str):
        self.urls_mapping: dict = self.load_base_urls_mapping()
        self.pack_mapping: dict = self.urls_mapping[pack_name]
        self.base_url: str = self._format_base_url(pack_name) + self.pack_mapping["base_url"]
        super().__init__(self.base_url)

    def get_config(self) -> dict:
        return self.get("get_creation_size")

    def set_config(self, config: dict) -> dict:
        return self.post("change_creation_size", config)

    def get_all_scenarios(self) -> [list, dict]:
        return self.get("get_scenario_config")

    @staticmethod
    def _format_base_url(pack_name: str) -> str:
        base_url: str = options.FAST_API_URL_FORMAT
        if 'MOCK_NAME' in os.environ:
            pack_name: str = pack_name.replace("_", "-")
            return base_url.format(pack_name, os.environ['MOCK_NAME'])
        else:
            base_url: str = options.LOCAL_URL_FORMAT
            return base_url.format(pack_name)

    @staticmethod
    def load_base_urls_mapping() -> dict:
        config_json_path: str = os.path.join(os.getcwd(), os.path.dirname(__file__),
                                             "base_urls_mapping.json")
        return load_data_from_json_file(config_json_path)
