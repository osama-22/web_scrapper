# 🦾 FastAPI Web Scraper  

This is a **FastAPI-based web scraper** designed to extract product data from an e-commerce website. The scraper collects **product names, prices, and images**, stores them efficiently, and notifies users about the scraping process.  

The project is **modular and extensible**, allowing easy integration with **different storage backends (JSON, Database, Cloud)** and **notification systems (Console, Email, Webhooks)**.

---

## 🚀 Features  
✅ **Scrapes product data** (name, price, image)  
✅ **Configurable settings**:
   - Limit the number of pages to scrape  
   - Use a proxy for requests  
✅ **Storage Options**:
   - JSON (default)  
   - Easily extendable to Databases like PostgreSQL or MongoDB  
✅ **Notification Options**:
   - Console (default)  
   - Extendable to Email, Webhooks, Slack, etc.  
✅ **Error Handling & Retries**:
   - Retries failed requests (`RETRY_COUNT` configurable)  
✅ **Caching with Redis**:
   - Prevents redundant updates when the product price hasn’t changed  
✅ **Authentication**:
   - Simple token-based authentication  

---

## 📂 Project Structure  

```bash
/scraper_app
│── main.py                 # FastAPI entry point
│── config.py               # Loads .env variables
│── storage/                # Storage-related files
│   │── base.py             # Abstract Base Class for Storage
│   │── json_storage.py     # JSON Storage Implementation
│   │── db_storage.py       # Database Storage (Placeholder)
│── notifier/               # Notification-related files
│   │── base.py             # Abstract Base Class for Notifier
│   │── console_notifier.py # Console Notifier Implementation
│   │── email_notifier.py   # Email Notifier Implementation (Example)
│── scraper.py              # Web Scraper Class
│── auth.py                 # Authentication Handler
│── cache.py                # Redis Caching
│── models.py               # Pydantic Models
│── requirements.txt        # Dependencies
│── .env.example            # Example environment variables
│── README.md               # Documentation
