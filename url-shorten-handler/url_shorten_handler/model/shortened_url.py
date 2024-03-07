from typing import Optional

from pydantic import BaseModel, AnyHttpUrl
from pydantic_core import Url


class ShortenedUrl(BaseModel):
    id: str
    owner: str
    original_url: AnyHttpUrl
    addresses: Optional[list] = []
    country_stats: Optional[dict] = {}