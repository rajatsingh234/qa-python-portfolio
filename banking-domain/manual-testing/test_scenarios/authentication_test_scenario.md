# Test Scenarios – User Authentication Module (SmartBank)

> Authentication is the **first security gate** of a banking application. Scenarios focus on access control, session handling, and account protection.

---

## 1. Login Scenarios

**AUTH-01** Verify user can log in with valid username and password
**AUTH-02** Verify login fails with invalid username
**AUTH-03** Verify login fails with invalid password
**AUTH-04** Verify validation message is shown when username and password are empty

---

## 2. Account Lock & Security Scenarios

**AUTH-05** Verify account is locked after configured number of failed login attempts
**AUTH-06** Verify locked account cannot log in even with correct credentials

---

## 3. Logout & Session Management Scenarios

**AUTH-07** Verify user can log out successfully
**AUTH-08** Verify session is terminated after logout
**AUTH-09** Verify user session expires after inactivity timeout
**AUTH-10** Verify user cannot access dashboard using browser back button after logout

---

## Notes

* Scenarios are designed with security and compliance considerations
* Detailed test cases are derived in Excel format

