# Binance Futures Assignment

## 👤 Author
- Name: [Your Full Name]
- Internship Role: Python Developer Intern

---

## 📌 Project Description
A Python project that connects to the **Binance Futures Testnet** to place:
- Market Orders  
- Limit Orders  
- TWAP Orders (Time-Weighted Average Price Strategy)  

It demonstrates:
- Binance API integration  
- Order execution & logging  
- Secure `.env` handling  
- Modular project structure  

⚠️ **Note:** This runs on the Binance **Testnet** (no real funds).

---

## 📂 Project Structure
```
binance-futures-assignment/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── twap_orders.py
│   ├── binance_client.py
│   ├── utils.py
│   ├── logger_config.py
│   └── __init__.py
├── logs/
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone Project
```bash
git clone https://github.com/<your-username>/binance-futures-assignment.git
cd binance-futures-assignment
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

Activate:
- Windows: `.venv\Scripts\activate`
- Linux/Mac: `source .venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Copy `.env.example` → `.env` and add your API keys:
```ini
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
BASE_URL=https://testnet.binancefuture.com
```

---

## ▶️ Usage

### Market Order
```bash
python -m src.market_orders 0.001 BUY BTCUSDT
```

### Limit Order
```bash
python -m src.limit_orders 0.001 BUY BTCUSDT 85000
```

### TWAP Order
```bash
python -m src.twap_orders twap BTCUSDT 0.01 BUY 10 5
```
➡️ Splits 0.01 BTC into 5 parts, every 10 seconds.

---

## 📝 Logs
All trades and responses are saved in:
```
logs/app.log
```

---

## ✅ Submission Notes
- Do **not** upload `.env`.  
- Use `.env.example` for template.  
- Tested with Binance Futures **Testnet**.
