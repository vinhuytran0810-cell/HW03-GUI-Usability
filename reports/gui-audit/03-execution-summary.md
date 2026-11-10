# GUI Checklist Execution Summary

## Scope and environment

- **SUT:** EShop Web
- **URL:** http://127.0.0.1:5173/
- **Screens:** Registration, Login, Forgot Password, Profile
- **Browser:** VS Code integrated browser (Electron 43.8.3; Chrome 150.0.7871.250)
- **OS:** Windows (browser user agent reports Windows NT 10.0)
- **Viewport:** 1281 × 676
- **Execution window:** 2026-11-09 10:21–10:35 +07
- **Checklist:** [`02-checklist.csv`](./02-checklist.csv) — all 66 original Expected Result values were retained.

## Results

| Status | Count |
|---|---:|
| Passed | 28 |
| Failed | 35 |
| Blocked | 0 |
| Not Run | 3 |
| N/A | 0 |
| **Total** | **66** |

## Category breakdown

| Category | Passed | Failed | Blocked | Not Run | N/A | Total |
|---|---:|---:|---:|---:|---:|---:|
| IA-01 | 6 | 6 | 0 | 0 | 0 | 12 |
| IA-02 | 16 | 21 | 0 | 2 | 0 | 39 |
| IA-03 | 4 | 6 | 0 | 0 | 0 | 10 |
| IA-04 | 2 | 2 | 0 | 1 | 0 | 5 |
| **Total** | **28** | **35** | **0** | **3** | **0** | **66** |

## Failed checks and evidence

Screenshots are original browser captures in [`evidence/gui/`](../../evidence/gui/). When multiple IDs cite the same file, they refer to the same observed UI state. Items with no screenshot explain the evidence limitation.

| ID | Observed discrepancy | Evidence |
|---|---|---|
| GUI-001 | Registration heading is H2; no H1. | [Screenshot](../../evidence/gui/GUI-001-registration-heading.png) |
| GUI-006 | Registration email input is `type=text`, not `type=email`. | [Screenshot](../../evidence/gui/GUI-006-registration-email-type.png) |
| GUI-008 | Registration form has no password-confirmation field. | [Screenshot](../../evidence/gui/GUI-008-registration-confirmation.png) |
| GUI-009 | Required registration labels have no visible asterisk. | [Screenshot](../../evidence/gui/GUI-009-registration-required-markers.png) |
| GUI-011 | Password helper text does not list permitted special characters. | [Screenshot](../../evidence/gui/GUI-011-registration-special-chars-guidance.png) |
| GUI-020 | Registration Login link opens `/login`, whose heading says “Đăng Ký”. | [Screenshot](../../evidence/gui/GUI-020-registration-link-destination-heading.png) |
| GUI-021 | Registration nav item has no visible selected state. | [Screenshot](../../evidence/gui/GUI-021-registration-active-nav.png) |
| GUI-023 | Login page has H2 and no H1. | [Screenshot](../../evidence/gui/GUI-023-login-heading.png) |
| GUI-024 | Login UI includes English “Username” and “Sign In”. | [Screenshot](../../evidence/gui/GUI-024-login-language.png) |
| GUI-026 | Login email field is labeled “Username” and uses `type=text`. | [Screenshot](../../evidence/gui/GUI-026-login-email-type-label.png) |
| GUI-027 | Login password input uses `type=text`, so it is unmasked. | [Screenshot](../../evidence/gui/GUI-027-login-password-type.png) |
| GUI-028 | Login required fields have no visible asterisk. | [Screenshot](../../evidence/gui/GUI-028-login-required-markers.png) |
| GUI-029 | Malformed email produced generic auth feedback below the button, not email feedback above it. | [Screenshot](../../evidence/gui/GUI-029-login-invalid-email.png) |
| GUI-030 | Login error appears below the submit button. | [Screenshot](../../evidence/gui/GUI-030-login-auth-error.png) |
| GUI-032 | Tab order focused the Registration link before the visually preceding Sign In button. | [Link focus](../../evidence/gui/GUI-032-login-tab-order-register-link.png); [button focus](../../evidence/gui/GUI-032-login-tab-order-submit.png) |
| GUI-035 | Login nav item has no visible selected state. | [Screenshot](../../evidence/gui/GUI-035-login-active-nav.png) |
| GUI-036 | Forgot Password page has H2 and no H1. | [Screenshot](../../evidence/gui/GUI-036-forgot-heading.png) |
| GUI-038 | Initial recovery screen has no step 1-of-2 indicator. | [Screenshot](../../evidence/gui/GUI-038-forgot-step-indicator.png) |
| GUI-039 | Recovery email input uses `type=text`. | [Screenshot](../../evidence/gui/GUI-039-forgot-email-type.png) |
| GUI-040 | Recovery email label has no visible asterisk. | [Screenshot](../../evidence/gui/GUI-040-forgot-required-marker.png) |
| GUI-041 | Invalid email request shows browser alert “Lỗi: User not found”, not inline validation above the button. | Alert observed; modal prevented screenshot capture. |
| GUI-042 | Initial recovery screen has no return-to-Login control. | [Screenshot](../../evidence/gui/GUI-042-forgot-login-return.png) |
| GUI-043 | No return-to-Login control is available to activate. | [Same initial-screen evidence](../../evidence/gui/GUI-042-forgot-login-return.png) |
| GUI-044 | OTP request reaches reset step, but no step 2-of-2 indicator appears. | Browser observation only; screenshot withheld because the page displays the OTP. |
| GUI-046 | OTP label says “4 số”, not six digits. | [Cropped label screenshot](../../evidence/gui/GUI-046-forgot-otp-length.png) |
| GUI-047 | Reset form has no password-confirmation field. | [Screenshot](../../evidence/gui/GUI-047-forgot-confirm-password-missing.png) |
| GUI-048 | Reset required fields have no visible asterisks. | [Screenshot](../../evidence/gui/GUI-048-forgot-required-markers.png) |
| GUI-049 | Invalid OTP shows a browser alert, not inline feedback above the button. | Alert observed; modal prevented screenshot capture. |
| GUI-050 | Back returns to step one, but no step 1-of-2 indicator appears. | [Screenshot](../../evidence/gui/GUI-050-forgot-return-step.png) |
| GUI-052 | Profile sections use H2; no H1 is present. | [Screenshot](../../evidence/gui/GUI-052-profile-heading.png) |
| GUI-058 | Required Name field label has no asterisk. | [Screenshot](../../evidence/gui/GUI-058-profile-required-markers.png) |
| GUI-059 | Invalid phone input shows a browser alert instead of feedback above Save; alert text refers to 9–10 digits. | Alert observed; screenshot timed out while modal was open. |
| GUI-063 | Logout action is labeled “Thoát”, not “Đăng xuất”. | [Screenshot](../../evidence/gui/GUI-063-profile-logout-label.png) |
| GUI-064 | Empty order state has a message but no image or SVG illustration. | [Screenshot](../../evidence/gui/GUI-064-profile-empty-orders.png) |
| GUI-066 | Registration positive-action button is red, not blue. | [Screenshot](../../evidence/gui/GUI-066-registration-primary-color.png) |

## Not Run and limitations

- **GUI-014:** Not run because malformed email is accepted by a `type=text` field and submission could create an unintended invalid account.
- **GUI-016:** Not run because the Registration confirmation input is absent; the prerequisite mismatch state cannot be entered. GUI-008 records the observed missing field.
- **GUI-065:** Not run because both available accounts had empty order histories; no order was created just to generate test data.
- Native browser alerts interrupted or timed out screenshot capture for GUI-041, GUI-049, and GUI-059. GUI-044’s screenshot was intentionally not stored to avoid retaining the displayed OTP.
- Viewport/browser coverage is limited to the single integrated-browser environment above; no physical device or additional browser was tested.
- Registration was completed with a disposable test account. The disposable account’s profile was updated for GUI-060 and an OTP request was made for GUI-044; password reset was not completed. No EShop source code was modified.
- Browser console showed HTTP 401/404/400 responses while deliberately exercising invalid Login/recovery/reset states. These are execution context, not separate API test results.

## Human review / next actions

- This is the execution stage only. No GitHub Issues or bug reports were created.
- Review the failed observations and four screenshot exceptions before deciding whether to repeat any checks with safer test data or another capture method.
