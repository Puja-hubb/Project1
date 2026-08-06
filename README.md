# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console application that analyses a student's placement-preparation performance. The application collects the student's profile details, attendance percentage, project completion status, profile verification status, and seven daily coding-practice scores. It validates all user inputs, classifies each practice score, calculates the total and average score, identifies the highest and lowest attempted scores, detects the first critical score, and evaluates whether the student is ready for a placement mock interview. Finally, it displays a detailed performance report along with the student's final status, primary blocker, and recommended next action.

---

## Features Implemented

* Student name validation using a `while` loop.
* Registration number and graduation year input.
* Graduation year eligibility check.
* Attendance validation (0–100).
* Project completion (Yes/No) validation.
* Profile verification (Yes/No) validation.
* Processing seven coding-practice scores using a single `for` loop.
* Validation of each practice score.
* Handling absent practice days using `continue`.
* Score classification:

  * Strong (75–100)
  * Satisfactory (60–74)
  * Needs Improvement (40–59)
  * Critical (0–39)
* Counting:

  * Attempted days
  * Absent days
  * Passed days
  * Failed days
  * Strong days
  * Satisfactory days
  * Needs Improvement days
  * Critical days
* Highest and lowest score identification with corresponding day.
* First critical score detection.
* Total score accumulation.
* Average score calculation with division-by-zero prevention.
* Placement readiness evaluation using Boolean expressions.
* Final status generation based on the first major blocker.
* Complete placement performance report.

---

## Python Concepts Used

* `print()`
* `input()`
* `int()`
* `float()`
* Variables
* Strings
* Boolean values
* Arithmetic operators
* Relational operators
* Logical operators
* Boolean expressions
* `if`, `elif`, `else`
* Nested conditions
* Compound conditions
* `while` loops
* `for` loops
* `range()`
* `break`
* `continue`
* Counters
* Accumulators
* f-strings

---

## How to Run

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## Test Result Summary

| Test ID | Scenario                     | Expected Result                 | Actual Result                   | Status |
| ------- | ---------------------------- | ------------------------------- | ------------------------------- | ------ |
| TC-01   | All requirements satisfied   | Ready for Mock Interview        | Ready for Mock Interview        | Pass   |
| TC-02   | Critical score present       | Critical Support Required       | Critical Support Required       | Pass   |
| TC-03   | Fewer than six attempts      | Practice Incomplete             | Practice Incomplete             | Pass   |
| TC-04   | Fewer than four passed days  | Insufficient Passed Practices   | Insufficient Passed Practices   | Pass   |
| TC-05   | Average below 70             | Practice Improvement Required   | Practice Improvement Required   | Pass   |
| TC-06   | Attendance below 75          | Attendance Improvement Required | Attendance Improvement Required | Pass   |
| TC-07   | Graduation year not eligible | Graduation Criteria Not Met     | Graduation Criteria Not Met     | Pass   |
| TC-08   | Project incomplete           | Application On Hold             | Application On Hold             | Pass   |
| TC-09   | Profile not verified         | Application On Hold             | Application On Hold             | Pass   |
| TC-10   | All days absent              | Practice Not Evaluated          | Practice Not Evaluated          | Pass   |
| TC-11   | Invalid score below -1       | Input Rejected                  | Input Rejected                  | Pass   |
| TC-12   | Invalid score above 100      | Input Rejected                  | Input Rejected                  | Pass   |
| TC-13   | Boundary value scores        | Correct Classification          | Correct Classification          | Pass   |
| TC-14   | Multiple blockers            | First Major Blocker Displayed   | First Major Blocker Displayed   | Pass   |

---

## Individual Contribution

**Name:** Puja Kumari

**Repository URL:** https://github.com/Puja-hubb/Project1

**My Main Contribution:**

Designed and implemented the complete PrepTrack Python application according to the project requirements. Developed the input validation, practice-score processing, performance analysis, placement readiness evaluation, and final reporting modules.

**Features I Implemented:**

* Student profile input
* Attendance validation
* Project and profile verification validation
* Seven-day practice score processing
* Score classification
* Passed and failed day counting
* Highest and lowest score detection
* First critical score detection
* Average score calculation
* Placement readiness evaluation
* Final performance report generation

**Python Concepts I Used:**

Variables, Boolean expressions, if-elif-else, while loops, for loops, break, continue, counters, accumulators, range(), input(), int(), float(), relational operators, logical operators, arithmetic operators, and f-strings.

**Most Difficult Logic:**

Implementing the placement readiness evaluation, detecting the first critical score, identifying the highest and lowest attempted scores without using lists, and displaying the first major blocker according to the required priority.

**Problem I Faced:**

Managing multiple conditions together while ensuring that all calculations, counters, validations, and final decision logic worked correctly for every possible test case.

**How I Solved It:**

I implemented the project step by step, tested each module individually, verified all boundary values and mandatory test cases, and corrected the logic until the application produced the expected output.

---

## Code Review Completed

| Reviewed Member                    | Repository Link | What Was Done Well | Issue Identified | Suggested Improvement |
| ---------------------------------- | --------------- | ------------------ | ---------------- | --------------------- |
| *(To be filled after peer review)* |                 |                    |                  |                       |

---

## Feedback Received

**Reviewed By:**

*To be filled after peer review.*

**Feedback Received:**

*To be filled after peer review.*

**Was the Feedback Valid?**

Yes / No

**Change Made:**

*To be filled after applying feedback.*

**Commit Message Used:**

*To be filled after committing the improvement.*

