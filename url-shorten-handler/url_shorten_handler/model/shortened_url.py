from pydantic import BaseModel, AnyHttpUrl


class ShortenedUrl(BaseModel):
    id: str
    original_url: AnyHttpUrl
