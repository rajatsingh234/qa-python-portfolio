# Test Scenarios – Fund Transfer Module (SmartBank)

> Fund Transfer is a **high‑risk banking module**. Scenarios focus on correctness, limits, duplication prevention, and user safety.

---

## 1. Own Account Transfer Scenarios

**FT-01** Verify user can transfer funds between own accounts within available balance
**FT-02** Verify transfer fails when amount exceeds available balance
**FT-03** Verify minimum transfer amount validation
**FT-04** Verify maximum transfer amount validation

---

## 2. Beneficiary Management Scenarios

**FT-05** Verify user can add a new beneficiary with valid details
**FT-06** Verify beneficiary addition fails with invalid account details
**FT-07** Verify inactive beneficiary cannot receive funds

---

## 3. Third‑Party Transfer Scenarios

**FT-08** Verify fund transfer to active beneficiary within daily limit
**FT-09** Verify transfer blocked when daily transaction limit is exceeded
**FT-10** Verify confirmation screen shows correct transfer details

---

## 4. Transaction Integrity & Reliability

**FT-11** Verify duplicate transaction is not processed on page refresh
**FT-12** Verify system behavior during network interruption at confirmation stage
**FT-13** Verify transaction reference number is generated after success

---

## 5. Negative & Security Scenarios

**FT-14** Verify transfer fails when mandatory fields are empty
**FT-15** Verify unauthorized user cannot access fund transfer URL directly

---

## Notes

* Detailed Excel test cases will be derived from these scenarios
* Scenarios are prioritized based on business and financial risk

