# Test Scenarios – SmartBank Retail Internet Banking

> These scenarios represent **what to test**, not detailed steps. They are designed using risk-based and real-world banking considerations.

---

## 1. User Authentication Scenarios

**AUTH-01** Verify user can log in with valid credentials
**AUTH-02** Verify login fails with invalid username
**AUTH-03** Verify login fails with invalid password
**AUTH-04** Verify error message is displayed for empty username and password
**AUTH-05** Verify account is locked after configured number of failed login attempts
**AUTH-06** Verify locked account cannot log in even with correct credentials
**AUTH-07** Verify user can successfully log out from the application
**AUTH-08** Verify user session is terminated after logout
**AUTH-09** Verify session expires after inactivity timeout
**AUTH-10** Verify user cannot access dashboard using browser back button after logout

---

## 2. Account Overview Scenarios

**ACC-01** Verify user can view savings account details after login
**ACC-02** Verify correct available balance is displayed
**ACC-03** Verify account number is partially masked for security
**ACC-04** Verify mini statement shows latest transactions
**ACC-05** Verify system behavior when account balance is zero
**ACC-06** Verify error handling when account data is unavailable

---

## 3. Fund Transfer Scenarios

**FT-01** Verify user can transfer funds between own accounts within balance limit
**FT-02** Verify fund transfer fails when amount exceeds available balance
**FT-03** Verify fund transfer fails when amount exceeds daily transaction limit
**FT-04** Verify user can add a new beneficiary successfully
**FT-05** Verify fund transfer is blocked to inactive beneficiary
**FT-06** Verify confirmation message is displayed before final submission
**FT-07** Verify correct debit and credit entries after successful transfer
**FT-08** Verify system behavior during network interruption at confirmation stage
**FT-09** Verify duplicate transaction is not processed on page refresh
**FT-10** Verify transaction reference number is generated for successful transfer

---

## 4. Transaction History Scenarios

**TXN-01** Verify user can view transaction history for selected date range
**TXN-02** Verify transactions are displayed in correct chronological order
**TXN-03** Verify debit and credit transactions are clearly distinguished
**TXN-04** Verify system behavior when no transactions exist for selected range
**TXN-05** Verify user can download transaction statement in PDF format
**TXN-06** Verify user can download transaction statement in CSV format
**TXN-07** Verify invalid date range selection is handled gracefully

---

## 5. Profile & Security Scenarios

**SEC-01** Verify user can change password with valid old password
**SEC-02** Verify password change fails if old password is incorrect
**SEC-03** Verify password complexity rules are enforced
**SEC-04** Verify user is logged out from all active sessions after password change
**SEC-05** Verify user can update personal profile details successfully
**SEC-06** Verify invalid data is not accepted in profile update form

---

## 6. Negative & Edge Case Scenarios

**NEG-01** Verify application behavior when browser cookies are disabled
**NEG-02** Verify system behavior on multiple simultaneous logins using same user
**NEG-03** Verify error handling when mandatory fields are skipped
**NEG-04** Verify application handles unexpected user actions gracefully

---

## 7. Usability & UI Scenarios

**UI-01** Verify consistent labels, fonts, and alignment across pages
**UI-02** Verify error messages are clear and user-friendly
**UI-03** Verify important actions require confirmation before execution

---

## Notes

* Detailed test cases will be derived from these scenarios
* Scenarios are prioritized based on business risk and user impact
