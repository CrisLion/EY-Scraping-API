from pydantic import BaseModel
from datetime import date
from typing import Literal

class IneligibilityPeriod(BaseModel):
    fromDate: str
    toDate: str