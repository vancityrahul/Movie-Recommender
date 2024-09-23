from pydantic import BaseModel
from typing import Optional


class MovieRequest(BaseModel):
    query : str
    genre :  Optional[list] = None
    k : Optional[int] = None

class MovieRequestv2(BaseModel):
    query : str
    k: Optional[int] = None