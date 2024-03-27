import datetime
from typing import Optional

from pydantic import BaseModel, AnyHttpUrl


class ShortenedUrl(BaseModel):
    id: str
    owner: str
    created_on: datetime.datetime
    original_url: AnyHttpUrl
    addresses: Optional[list] = []
    country_stats: Optional[dict] = {}
