# Case 12: Attendance Recovery Computation

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Calculate current attendance percentages and determine the minimum consecutive classes required to reach an eligibility threshold under different future attendance scenarios.

## Objectives
For each supplied record, calculate current attendance and the smallest number of additional classes that must all be attended to reach the stated threshold.

## Assumptions
- Each future class is attended; missed future classes are not included.
- Threshold percentages are supplied per record; an already eligible student needs zero additional classes.
- Inputs are non-negative whole numbers and total classes are greater than zero.

## Algorithm
1. Read attended classes, total classes, and threshold.
2. Calculate current attendance percentage.
3. Increase future attended classes one at a time until projected attendance reaches the target.
4. Print current percentage and minimum required classes.

## Flowchart

```text
Start → Read records → Calculate current % → Set extra = 0 → Meets threshold? → No: add one future attended class → Yes: display result → More records? → End
```

## Pseudocode

```text
FOR each (attended, total, threshold)
    current = attended / total * 100
    extra = 0
    WHILE (attended + extra) / (total + extra) * 100 < threshold
        extra = extra + 1
    PRINT current and extra
```

## Python source code

```python
records = [(28, 40, 75), (35, 40, 75), (20, 30, 75)]

for attended, total, threshold in records:
    current_percent = attended / total * 100
    extra_classes = 0
    while (attended + extra_classes) / (total + extra_classes) * 100 < threshold:
        extra_classes = extra_classes + 1
    print("Attendance:", attended, "of", total)
    print("Current percentage:", round(current_percent, 2))
    print("Target:", threshold, "%")
    print("Additional consecutive attended classes:", extra_classes)
    print()
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/12_attendance_recovery.png`.

```text
Attendance: 28 of 40
Current percentage: 70.0
Target: 75 %
Additional consecutive attended classes: 8

Attendance: 35 of 40
Current percentage: 87.5
Target: 75 %
Additional consecutive attended classes: 0

Attendance: 20 of 30
Current percentage: 66.67
Target: 75 %
Additional consecutive attended classes: 10
```

## Conclusion
The repeated calculation finds the minimum all-attended future classes needed for each supplied threshold. It does not infer an institutional attendance policy.
