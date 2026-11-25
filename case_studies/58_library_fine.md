# Case 58: Library Borrowing and Fine Reconciliation

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Analyze tuples representing book identifiers, borrowing periods, and return delays; calculate fines, identify overdue records, and reconcile availability.

## Objectives
Calculate example late fees from tuple records and identify books marked unavailable.

## Assumptions
- Each tuple is (book ID, days late, available).
- Example fee is 2 currency units per late day, capped at 20 per record; this is illustrative because no fee policy is supplied.
- Zero or negative late days incur no fine.

## Algorithm
1. Unpack each tuple.
2. Calculate a fee for positive late days and apply the cap.
3. Add to total and print the record.
4. Report unavailable books.

## Flowchart

```text
Start → Set example rate and cap → Unpack record → Positive late days? calculate : zero → Apply cap → Add total → Available? report → End
```

## Pseudocode

```text
FOR each (book_id, late_days, available)
    IF late_days > 0: fee = late_days * rate
    ELSE: fee = 0
    cap fee; add total
    report unavailable status
PRINT total fees
```

## Python source code

```python
records = [("B101", 3, True), ("B205", 0, False), ("B330", 15, True)]
fine_per_day = 2
maximum_fine = 20
total_fines = 0
for book_id, days_late, available in records:
    if days_late > 0:
        fine = days_late * fine_per_day
    else:
        fine = 0
    if fine > maximum_fine:
        fine = maximum_fine
    total_fines = total_fines + fine
    print(book_id, "days late:", days_late, "fine:", fine)
    if available == False:
        print(book_id, "is unavailable")
print("Total example fines:", total_fines)
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/58_library_fine.png`.

```text
B101 days late: 3 fine: 6
B205 days late: 0 fine: 0
B205 is unavailable
B330 days late: 15 fine: 20
Total example fines: 26
```

## Conclusion
The arithmetic follows a labeled example policy. A real library must replace the assumed rate and cap with its approved rules.
