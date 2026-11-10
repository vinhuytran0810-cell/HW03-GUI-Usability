# GUI Checklist — Design Notes

## Design scope

- SUT: EShop Web at `http://127.0.0.1:5173/`.
- Screens selected by the user: Registration (primary), Login, Forgot Password, and Profile.
- Checklist: [`02-checklist.csv`](./02-checklist.csv), 66 atomic GUI checkpoints.
- Every checkpoint is initially `Not Run`. Actual Result, Environment, and Executed At are intentionally blank; no GUI checks were run for this design stage.
- The CSV uses the Skill template columns. The Evidence column describes evidence to collect during a future approved execution; it does not imply evidence exists.

## Requirement traceability

- Registration: FR-01, FR-21, FR-22, FR-23.
- Login: FR-02, FR-21, FR-22, FR-23.
- Forgot Password: FR-03, FR-21, FR-22, FR-23.
- Profile: FR-04, FR-11 (order-history display), FR-21, FR-22, FR-23, FR-24 (empty state).
- Cross-screen form color and common UI checks: FR-21.
- IA categories follow the Skill rubric: IA-01 General UI, IA-02 Forms, IA-03 Navigation, IA-04 Feedback/State.

The checklist targets GUI presentation and observable feedback only. Authentication, registration, password-reset, profile persistence, authorization, security, and business-rule correctness are not independently certified by this design.

## AI critique / review

### Candidate gaps

- The assignment material available here does not specify target browser versions, viewport sizes, or a physical device. Each viewport is therefore to be recorded when execution is approved; no mobile-device claim is made.
- The reset second-step UI requires reaching the OTP-request response. If the test environment cannot provide a registered account or the recovery step, affected items should be marked `Blocked`, not inferred.
- Profile phone/name/address requiredness is not fully stated as a form-level visual rule. GUI-058 asks the executor to verify required markers only for fields the form actually presents as required and flags the uncertainty for review.
- Error placement above submit follows FR-22. Some checks require triggering a validation or request-error state; they are test design steps, not completed tests.
- Profile order-history checks need suitable test accounts: one with no orders for the empty state and one with order history for the table state.

### Unsupported assumptions avoided

- No browser, viewport, successful registration, OTP, error message wording, or visual pass/fail result is asserted as observed.
- No expectation is included for private implementation details (database state, token contents, API response internals).
- GUI accessibility of a route is not treated as proof that its business behavior is correct.

### Discarded checks

- Removed backend-only checks such as duplicate-email enforcement, failed-login attempt count, account-lock duration, OTP entropy/reuse, ownership enforcement, and profile role authorization; these are not GUI presentation checks.
- Removed unrelated Home, product, cart, checkout, Admin, and Mobile checks because they are outside the user-selected screen scope.
- Did not make subjective checks such as “attractive” or “easy to use.”

### Human review decisions

- Pending: user review/approval of the proposed checkpoints, target browser and viewport, test accounts, and any required course-specific evidence format.
- No human approval is implied by this draft.
