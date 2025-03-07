from fastapi import FastAPI, Depends
from scraper import ProductScraper
from storage.storage import Storage
from notifier.notifier import Notifier
from auth import get_current_user
from models import ScrapeSettings
import asyncio

app = FastAPI()
scraper = ProductScraper()
# Initialize storage & notifier with default strategies
storage = Storage()  # Default: JSON Storage
notifier = Notifier()  # Default: Console Notification


@app.post("/scrape/")
async def scrape_products(settings: ScrapeSettings, user: str = Depends(get_current_user)):
    products = await asyncio.to_thread(scraper.scrape, settings.pages, settings.proxy)
    updated_count = storage.save(products)
    notifier.notify(updated_count)
    return {"message": f"Scraped {updated_count} new products"}
