from typing import Optional

from pydantic import BaseModel, AnyHttpUrl


class ShortenedUrl(BaseModel):
    id: str
    original_url: AnyHttpUrl
    addresses: Optional[list] = []
    country_stats: Optional[dict] = {}
