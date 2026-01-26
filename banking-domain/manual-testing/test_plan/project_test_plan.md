# Test Plan – SmartBank Retail Internet Banking

## 1. Introduction

This document defines the manual testing approach for **SmartBank – Retail Internet Banking**, a mock banking web application created for QA portfolio purposes. The goal is to validate core banking functionalities with a strong focus on correctness, security awareness, and user experience.

---

## 2. Objective

* Verify that critical banking features work as per business requirements
* Identify functional, negative, and boundary defects early
* Ensure secure handling of user sessions and transactions
* Produce high-quality test artifacts suitable for enterprise QA environments

---

## 3. Application Overview

**Application Name:** SmartBank – Retail Internet Banking
**Application Type:** Web Application
**Target Users:** Retail banking customers

### Core Modules in Scope

* User Authentication
* Account Overview
* Fund Transfer
* Transaction History
* Profile & Security Settings

---

## 4. Test Scope

### 4.1 In-Scope

* Functional testing of all core modules
* Negative and edge-case testing
* Boundary value validation (amounts, dates, attempts)
* Basic security validations (session, password rules)
* Usability and UI consistency checks

### 4.2 Out-of-Scope

* Performance / Load testing
* Penetration testing
* Automation testing
* API testing
* Mobile application testing

---

## 5. Test Approach

### 5.1 Test Levels

* System Testing (Manual)

### 5.2 Test Types

* Functional Testing
* Negative Testing
* Boundary Testing
* Security-Oriented Testing (non-intrusive)
* Usability Testing

### 5.3 Test Design Techniques

* Boundary Value Analysis
* Error Guessing
* Risk-Based Testing

---

## 6. Test Environment

* **Browser:** Chrome, Firefox
* **OS:** Windows / macOS
* **Test Data:** Mock banking users and accounts
* **Network:** Stable internet connection

---

## 7. Test Data Strategy

* Valid and invalid user credentials
* Accounts with zero, low, and high balances
* Transactions at minimum, maximum, and beyond limits
* Active and inactive beneficiary accounts

---

## 8. Entry & Exit Criteria

### Entry Criteria

* Application is deployed and accessible
* Requirements are finalized and reviewed
* Test data is available

### Exit Criteria

* All planned test cases executed
* Critical and high-severity defects addressed
* Test summary report prepared

---

## 9. Defect Management

* Defects will be logged with:

  * Summary
  * Steps to Reproduce
  * Expected vs Actual Result
  * Severity & Priority
  * Environment details

---

## 10. Roles & Responsibilities

* **QA Engineer:** Test planning, execution, defect reporting
* **Developer (Assumed):** Defect fixing
* **Product Owner (Assumed):** Requirement clarification

---

## 11. Risks & Mitigation

| Risk                         | Impact | Mitigation             |
| ---------------------------- | ------ | ---------------------- |
| Ambiguous requirements       | High   | Assumptions documented |
| Limited test data            | Medium | Mock data creation     |
| Browser compatibility issues | Medium | Multi-browser testing  |

---

## 12. Deliverables

* Test Plan document
* Test Scenarios
* Test Cases
* Bug Reports
* Test Summary Report

---

## 13. Approval

This test plan is prepared for portfolio demonstration and reflects industry-standard QA practices.

