import requests
from bs4 import BeautifulSoup
import time
import random
import os
import re
from cache import Cache
from config import RETRY_COUNT
class ProductScraper:
    def __init__(self):
        self.base_url = "https://dentalstall.com/shop/"
        self.cache = Cache()
    
    def scrape(self, num_pages: int, proxy: str = None):
        headers = {"User-Agent": "Mozilla/5.0"}
        proxies = {"http": proxy, "https": proxy} if proxy else None
        all_products = []
        
        for page in range(1, num_pages + 1):
            url = f"{self.base_url}/page/{page}/"
            retries = RETRY_COUNT

            while retries > 0:
                try:
                    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, "html.parser")
                    products = self.parse_products(soup)
                    all_products.extend(products)
                    break  
                except requests.exceptions.RequestException:
                    retries -= 1
                    time.sleep(random.randint(3, 6))  
        
        return all_products

    def parse_products(self, soup):
        product_list = []

        for product in soup.find_all("li", class_="product"):
            print("Scraping product...")
            # Extract title
            title_tag = product.find("h2", class_="woo-loop-product__title")
            title = title_tag.get_text(strip=True) if title_tag else "Unknown"

            # Extract price (new and old price, take the new price if available)
            price_tag = product.select_one(".price ins .woocommerce-Price-amount")
            if not price_tag:  # If no discount, take regular price
                price_tag = product.select_one(".price .woocommerce-Price-amount")
            price = float(price_tag.get_text(strip=True).replace("₹", "").replace(",", "")) if price_tag else 0.0

            cached_price = float(self.cache.get(title) or 0.0)
            if cached_price and cached_price == price:
                print(f"Skipping {title} as it's already cached.")
                continue  
            self.cache.set(title, price)
            # Extract correct image URL (handle lazy-loaded images)
            img_tag = product.select_one(".mf-product-thumbnail img")

            if img_tag:
                img_url = img_tag.get("data-lazy-src") or img_tag.get("src")
            else:
                img_url = ""

            if img_url.startswith("data:image"):
                img_url = ""  

            # Download and store the image locally
            image_path = self.download_image(img_url, title) if img_url else "No image available"

            product_list.append({
                "product_title": title,
                "product_price": price,
                "path_to_image": image_path
            })

        return product_list

    def download_image(self, url, title):
        """Downloads and saves an image using a clean filename."""
        if not url:
            return "No image available"

        # Clean and shorten title for filename
        clean_title = re.sub(r"[^a-zA-Z0-9_-]", "_", title)  # Replace spaces & special chars
        clean_title = clean_title[:50]  # Limit filename length to 50 chars

        img_path = f"images/{clean_title}.jpg"

        os.makedirs("images", exist_ok=True)
        
        try:
            img_data = requests.get(url).content
            with open(img_path, "wb") as f:
                f.write(img_data)
            return img_path
        except Exception as e:
            return f"Error downloading: {str(e)}"
