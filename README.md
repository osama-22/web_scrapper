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
```

---

# 🛠️ Setup Instructions  

Follow these steps to set up and run the FastAPI web scraper.  
## **1️⃣ Clone the Repository**  
First, clone the repository from GitHub and navigate into the project directory:  
```sh
git clone https://github.com/osama-22/web_scrapper.git
cd web_scrapper
```

## **2️⃣ Create & Activate a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate
```

## **3️⃣ Install Dependencies**  
Install the required Python packages using pip:  
```sh
pip install -r requirements.txt
```

## **4️⃣ Set Up Environment Variables**  
Copy the `.env.example` file and create a new `.env` file:  
```sh
cp .env.example .env
```
Edit the `.env` file with your specific settings.
```sh
API_KEY=your_static_api_key
REDIS_HOST=localhost
REDIS_PORT=6379
RETRY_COUNT=3
```

## **5️⃣ Start Redis Server (For Caching)**  
For macOS (Homebrew):
```sh
brew install redis
brew services start redis
```
For Ubuntu/Debian:
```sh
sudo apt update
sudo apt install redis
sudo systemctl start redis
sudo systemctl enable redis
```
To verify Redis is running, open a new terminal window and run:
```sh
redis-cli ping
```
Expected output:
```sh
PONG
```

## **6️⃣ Run the Scraper**  
Start the FastAPI server:  
```sh
uvicorn main:app --reload
```
The server should start and display:
```sh
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## **7️⃣ Test the API**  
### Using Postman:
1. Open Postman and create a new request.
2. Set the request type to POST.
3. Enter the URL: 
```sh
http://127.0.0.1:8000/scrape/
```
4. Go to the Headers tab and add:
```sh
Key: Authorization
Value: your_static_api_key
```
5. Go to the Body tab, select raw, choose JSON, and enter:
```sh
{
  "pages": 1,
  "proxy": ""
}
```
6. Click "Send".

### Using cURL
Alternatively, test the API using cURL in the terminal:
```sh
curl -X POST "http://127.0.0.1:8000/scrape/" \
     -H "Content-Type: application/json" \
     -H "Authorization: your_static_api_key" \
     -d '{"pages": 1, "proxy": ""}' 
```

---


