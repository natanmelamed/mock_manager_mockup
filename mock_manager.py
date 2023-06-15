from fastapi import APIRouter
from mock_manager_resources import config_scenario, get_all_scenarios
from model_objects.config_scenario import ConfigScenario
from common.response_data_handler import ResponseDataHandler

_response_data_handler: ResponseDataHandler = ResponseDataHandler()
router: APIRouter = APIRouter()

SCENARIOS: str = "scenarios"


@router.get('/scenarios')
async def get_scenarios() -> dict:
    return get_all_scenarios()


@router.post('/configure_scenario')
async def configure_scenario(config_scenario_data: ConfigScenario) -> dict:
    return config_scenario(config_scenario_data.pack_name,
                           config_scenario_data.scenario_mode,
                           config_scenario_data.scenario_id)
