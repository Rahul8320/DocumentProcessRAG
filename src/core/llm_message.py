from pydantic import BaseModel
from typing import Literal


class LLMMessage(BaseModel):
    role: Literal["user", "system"]
    content: str
