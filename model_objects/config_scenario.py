from pydantic import BaseModel


class ConfigScenario(BaseModel):
    scenario_id: str
    scenario_mode: bool
    pack_name: str
