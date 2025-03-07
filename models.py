from pydantic import BaseModel, Field

class ScrapeSettings(BaseModel):
    pages: int = Field(..., gt=0, description="Number of pages to scrape")
    proxy: str = Field(None, description="Optional proxy string")
