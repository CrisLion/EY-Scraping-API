from pydantic import BaseModel

from app.models.value_objects import IneligibilityPeriod

class WorldBankItem(BaseModel):
    firmName: str
    address: str | None
    country: str
    ineligibilityPeriod : IneligibilityPeriod
    grounds: str

class WorldBankResponse(BaseModel):
    size: int
    worldBankItems: list[WorldBankItem]