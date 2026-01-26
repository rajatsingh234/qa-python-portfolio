# Test Scenarios – Profile & Security Module (SmartBank)

> Profile & Security ensures **user data protection, account safety, and compliance**. Scenarios focus on authentication strength, session safety, and data validation.

---

## 1. Password Management Scenarios

**SEC-01** Verify user can change password with correct current password
**SEC-02** Verify password change fails with incorrect current password
**SEC-03** Verify password complexity rules are enforced
**SEC-04** Verify user is logged out from all active sessions after password change

---

## 2. Profile Update Scenarios

**SEC-05** Verify user can update personal profile details successfully
**SEC-06** Verify profile update fails with invalid input data
**SEC-07** Verify mandatory fields validation during profile update

---

## 3. Session & Security Scenarios

**SEC-08** Verify session timeout after configured inactivity period
**SEC-09** Verify user cannot reuse old password after password change
**SEC-10** Verify direct URL access to profile page without login is restricted

---

## Notes

* Scenarios are designed with security and compliance in mind
* Detailed test cases will be derived in Excel format

