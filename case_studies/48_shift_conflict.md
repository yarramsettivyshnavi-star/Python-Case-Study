# Case 48: Tuple-Based Employee Shift Conflict Detection

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Represent employee shifts as tuples, compare time intervals, detect overlapping assignments, and identify employees with conflicting schedules.

## Objectives
Compare pairs of same-employee shifts and report overlapping intervals.

## Assumptions
- Times use one same-day 24-hour numeric scale; overnight shifts are outside this model.
- Intervals are half-open [start, end); adjacent shifts do not overlap.
- Every shift satisfies start < end.

## Algorithm
1. Store shifts as (employee, start, end) tuples.
2. Compare each unique pair.
3. Unpack both tuples.
4. For the same employee, report overlap if start1 < end2 and start2 < end1.

## Flowchart

```text
Start → Read tuples → Select unique pair → Unpack → Same employee and overlapping? print conflict → More pairs? → End
```

## Pseudocode

```text
FOR i from 0 to last shift
    FOR j from i+1 to last shift
        unpack both tuples
        IF names match AND start1 < end2 AND start2 < end1
            PRINT conflict
```

## Python source code

```python
shifts = [("Asha", 9, 13), ("Asha", 12, 16), ("Ravi", 9, 12), ("Asha", 16, 18)]
conflict_count = 0
for first in range(len(shifts)):
    for second in range(first + 1, len(shifts)):
        employee1, start1, end1 = shifts[first]
        employee2, start2, end2 = shifts[second]
        if employee1 == employee2 and start1 < end2 and start2 < end1:
            print("Conflict:", employee1, "shift", start1, "-", end1, "overlaps", start2, "-", end2)
            conflict_count = conflict_count + 1
print("Total conflicts:", conflict_count)
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/48_shift_conflict.png`.

```text
Conflict: Asha shift 9 - 13 overlaps 12 - 16
Total conflicts: 1
```

## Conclusion
Tuple unpacking and pairwise comparisons detect overlaps under the same-day rule. Overnight shifts need a separate time model.
