# GUI Criteria Reference

These are **candidate prompts for observation**, not universal requirements. Check the SUT specification and actual UI before turning any candidate into an expected result. An item may be N/A.

## IA-01 — General UI standards

- Consistent typography, color, spacing, icon meaning and visual hierarchy across comparable screens.
- Readable labels and status text; no clipping, overlap, unintended truncation or horizontal overflow at specified viewports.
- Visual alignment of controls, headings, cards and action areas.
- Images and icons are displayed correctly (a visible image can still be the **wrong** image).
- Visible focus indication and sufficient contrast where requirements or accepted standards apply.
- Layout adapts to explicitly requested viewport sizes; don't infer real-device coverage from emulation.

## IA-02 — Forms

- Input labels/placeholder text and required indicators match documented requirements.
- Correct visible input type, mask, default state and enabled/disabled state.
- Validation feedback is placed near the relevant control or in the documented location.
- Error message remains legible and is dismissible or persistent as specified.
- User-entered values remain in the intended fields when focus changes or validation occurs.
- Focus order and keyboard interaction are consistent with the specified GUI behavior.

## IA-03 — Navigation

- Navigation links, tabs, menus and breadcrumbs are visible and distinguishable.
- Current/selected navigation state is visually identifiable.
- Menu open/close and back navigation produce expected visible state.
- Header/footer navigation does not overlap content at specified viewports.
- Destination labels and screen headings are consistent; do not turn this into backend routing verification unless the GUI requirement says so.

## IA-04 — Feedback and state

- Loading, empty, success, error and disabled states appear when appropriate and are visually understandable.
- Buttons and controls provide expected visible feedback after interaction.
- Validation messages have correct text and visibility; dismiss action updates the GUI.
- Badge/count, selection and modal states remain visually coherent when UI state changes.
- Toast/banner/modal is not obscured, clipped or duplicated at target viewports.

## How to write an atomic checkpoint

**Weak:** "Checkout GUI works well." (vague, mixes functional and usability)

**Better:** "At viewport 1280×900, after submitting the form with a missing required Last Name, the validation message is visible, readable, and does not overlap the Continue button."

For each item specify:
- `ID`: e.g. `GUI-001` (unique across environments).
- `Category`: one of `IA-01`, `IA-02`, `IA-03`, `IA-04`.
- `Screen`, `Precondition`, `Steps`, `Expected Result`.
- `Status`: `Not Run` until actually checked.
- `Actual Result`, `Environment`, `Executed At`, `Evidence`, `Notes` after execution.

## Common false positives and scope errors

- `toBeVisible()` does not prove that the right image, text alignment, or responsive layout is correct.
- A passing functional checkout flow does not prove its GUI is correct.
- A 390px desktop viewport does not prove Android Chrome was tested.
- A usability score requires responses from real participants, not an agent's opinion.
- A suspected defect without a requirement/reference should be flagged for confirmation.

## HW03 adaptation notes

If the assignment rubric requires more than 40 items, design **at least 41 meaningful checks** spanning the four IA groups. Use the actual EShop screens and requirements to choose coverage. Do not invent 41 execution results or use filler to hit the count.

For cross-platform testing, reuse checklist IDs, identify the real environment and capture the evidence required by the course. Confirm any required overlay/watermark text from the original assignment before altering copies of screenshots; preserve the unmodified originals.
