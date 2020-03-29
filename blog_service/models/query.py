from pydantic import BaseModel, Json
from typing import Optional

class QueryModel(BaseModel):
    filter: Optional[Json] = {}