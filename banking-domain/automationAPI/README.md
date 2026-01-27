# 🔌 Banking API Automation – ParaBank

This module contains **API automation for a banking application** using **Python, requests, and Pytest**.
It validates **backend business logic independently of the UI**, focusing on authentication, account data,
and fund transfer operations.

This project demonstrates **real-world backend QA skills**, including session handling,
dynamic data extraction, and validation of state-changing APIs.

---

## 📌 Purpose of This Module

- Validate backend banking logic without UI dependency
- Demonstrate session-based authentication testing
- Perform data-driven API chaining
- Show realistic API testing for legacy banking systems
- Complement UI automation with backend coverage

---

## 🔗 Application Under Test (AUT)

**ParaBank – Public Banking Demo Application**  
https://parabank.parasoft.com/parabank/index.htm

---

## 🧪 Automated API Scenarios

### ✅ Implemented APIs

1. **Login API**
   - Authenticates user via form-based login
   - Validates session creation (`JSESSIONID`)

2. **Account Overview API**
   - Fetches customer accounts using `customerId`
   - Validates response structure and account data

3. **Fund Transfer API**
   - Transfers funds between two accounts
   - Validates successful transaction response

---

## 🏗 Project Structure

```
banking-domain/automationAPI/
├── tests/
│   ├── test_login_api.py
│   ├── test_account_overview_api.py
│   └── test_fund_transfer_api.py
│
├── utils/
│   └── api_client.py
│
├── config/
│   └── config.py
│
├── README.md
└── requirements.txt
```

---

## 🛠 Technology Stack

- Python 3
- requests
- Pytest
- Allure Reports

---

## ⚙️ Setup Instructions

### Activate Virtual Environment
```bash
source automation/banking/.venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ API Test Execution

### Run All API Tests
```bash
pytest api/banking/tests -v
```

### Run a Specific API Test
```bash
pytest api/banking/tests/test_login_api.py -v
```

---

## 🔐 Configuration Management

Configuration is externalized in:

```
config/config.py
```

Example:
```python
BASE_URL = "https://parabank.parasoft.com/parabank"
USERNAME = "your_username"
PASSWORD = "your_password"
```

---

## ⏳ Authentication Strategy

- Uses `requests.Session()` to persist authentication cookies
- Same session is reused across API calls
- Simulates real backend interaction

---

## 📊 Allure Reporting

### Generate Allure Results
```bash
pytest api/banking/tests -v --alluredir=reports/allure-results
```

### View Allure Report
```bash
allure serve reports/allure-results
```

---

## 🧠 Interview Explanation

> “I automated backend banking APIs using Python and requests, validating authentication,
account retrieval, and fund transfer operations with session-based authentication
and Allure reporting.”

---

## 🚀 Future Enhancements

- Negative API scenarios
- Schema validation
- CI/CD integration

---

## 📌 Disclaimer

This project is created **for learning and portfolio purposes only**
using a public demo banking application.
