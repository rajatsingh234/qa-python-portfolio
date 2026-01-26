# 🏦 Banking Automation Framework – ParaBank

This project contains a **UI automation framework for a banking application** built using **Python, Selenium, and Pytest**, following **industry-standard best practices** such as **Page Object Model (POM)**, explicit waits, externalized configuration, and professional reporting using **Allure**.

The goal of this project is to demonstrate **real-world QA automation skills** in a **banking domain context**, suitable for **interviews, portfolios, and real projects**.

---

## 📌 Purpose of This Project

- Demonstrate **SDET-level automation skills**
- Show conversion of **manual test cases into automation**
- Build a **scalable and maintainable framework**
- Handle **real-world synchronization challenges**
- Present a **clean GitHub-ready portfolio project**

---

## 🔗 Application Under Test (AUT)

**ParaBank – Public Banking Demo Application**  
https://parabank.parasoft.com/parabank/index.htm

### Why ParaBank?
- Banking-style UI and workflows
- Supports login, account overview, fund transfer, logout
- No OTP / Captcha (automation-friendly)
- Public and stable demo environment

> ⚠️ Real banking applications are intentionally avoided due to OTP, captcha, and security restrictions.

---

## 🧪 Automated Scenarios

### ✅ Implemented Scenarios
- User Login (Happy Path)
- User Login (Negative Scenario)
- Account Overview Validation
- Fund Transfer (Happy Path)
- User Logout

### ❌ Intentionally Excluded
- OTP / 2FA flows
- Captcha handling
- Payment gateway validation
- Security & performance testing

---

## 🏗 Project Structure

```
automation/banking/
├── pages/
├── tests/
├── utils/
├── config/
├── reports/
├── .venv/
├── requirements.txt
└── README.md
```

---

## 🛠 Technology Stack

- Python 3
- Selenium WebDriver
- Pytest
- webdriver-manager
- Allure Reports

---

## ⚙️ Setup Instructions

### Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Test Execution

```bash
pytest -v
pytest tests/test_login.py -v
pytest tests/test_fund_transfer.py::test_fund_transfer -v
pytest -k login -v
```

---

## 📊 HTML Reporting

```bash
pip install pytest-html
pytest -v --html=reports/report.html --self-contained-html
```

---

## 📊 Allure Reporting

```bash
pytest -v --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 📌 Disclaimer

This project is for **learning and portfolio purposes only** using a public demo application.
