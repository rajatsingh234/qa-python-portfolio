# Test Scenarios – Transaction History Module (SmartBank)

> Transaction History is critical for **auditability, user trust, and compliance**. Scenarios focus on accuracy, filters, downloads, and edge cases.

---

## 1. View & Display Scenarios

**TXN-01** Verify user can view transaction history after login
**TXN-02** Verify transactions are displayed in correct chronological order
**TXN-03** Verify debit and credit transactions are clearly differentiated

---

## 2. Filter & Search Scenarios

**TXN-04** Verify user can filter transactions by valid date range
**TXN-05** Verify system handles invalid date range selection gracefully
**TXN-06** Verify system behavior when no transactions exist for selected range

---

## 3. Download & Export Scenarios

**TXN-07** Verify user can download transaction statement in PDF format
**TXN-08** Verify user can download transaction statement in CSV format

---

## 4. Accuracy & Integrity Scenarios

**TXN-09** Verify transaction amounts match account balance changes
**TXN-10** Verify transaction reference numbers are unique and visible

---

## 5. Negative & Security Scenarios

**TXN-11** Verify unauthorized user cannot access transaction history URL directly
**TXN-12** Verify system behavior when transaction service is unavailable

---

## Notes

* Scenarios emphasize correctness and compliance
* Detailed Excel test cases will be derived from these scenarios
