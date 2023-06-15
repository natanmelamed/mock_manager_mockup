from mock_clients.mock_client import MockClient


def get_all_scenarios() -> dict:
    base_urls_mapping: dict = MockClient.load_base_urls_mapping()
    scenarios_per_pack_list: dict = {}
    for pack in base_urls_mapping.keys():
        mock_client: MockClient = MockClient(pack)
        pack_scenarios: [list, dict] = mock_client.get_all_scenarios()
        if type(pack_scenarios) is list:
            scenarios_per_pack_list[pack] = pack_scenarios

    return scenarios_per_pack_list


def config_scenario(pack_name: str, scenario_mode: bool, scenario_id: str) -> dict:
    mock_client: MockClient = MockClient(pack_name)
    current_config: dict = mock_client.get_config()
    load_base_urls_mapping: dict = MockClient.load_base_urls_mapping()
    if "body" in load_base_urls_mapping[pack_name]:
        current_config = load_base_urls_mapping[pack_name]["body"]
    current_config["current_scenario"]: str = scenario_id
    current_config["scenario_mode"]: bool = scenario_mode
    mock_client.set_config(current_config)
    return current_config
