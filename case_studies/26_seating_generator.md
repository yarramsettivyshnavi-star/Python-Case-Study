# Case 26: Nested Loop Examination Seating Generator

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Generate a seating arrangement with row and column identifiers, reserved positions, alternate seating restrictions, and fixed classroom capacities.

## Objectives
Generate a labeled seating grid and mark supplied positions as reserved and apply an explicitly assumed checkerboard alternating-seat pattern.

## Assumptions
- Rows and columns are positive and fit the room.
- Reserved positions use one-based (row, column) tuples.
- The sheet does not define which seats alternate. For this example only, seats where (row + column) is even are available; the other non-reserved positions are marked X. This is an explicit sample assumption, not a supplied rule.

## Algorithm
1. Set dimensions and reserved tuples.
2. Use nested loops to visit every seat.
3. Append R for reserved seats, S for available positions in the assumed pattern, and X for alternating blocked positions.
4. Print each row.

## Flowchart

```text
Start → Set dimensions and reserved tuples → Loop through each seat → Reserved? append R → Otherwise alternating position available? append S : append X → Print row → More rows? → End
```

## Pseudocode

```text
FOR each row and column
    IF reserved: append R
    ELSE IF row + column is even: append S
    ELSE: append X
    PRINT each row
```

## Python source code

```python
row_count = 3
column_count = 4
reserved_seats = [(1, 1), (3, 3)]

for row in range(1, row_count + 1):
    seat_labels = ""
    for column in range(1, column_count + 1):
        if (row, column) in reserved_seats:
            seat_labels = seat_labels + " R"
        elif (row + column) % 2 == 0:
            seat_labels = seat_labels + " S"
        else:
            seat_labels = seat_labels + " X"
    print("Row", row, ":", seat_labels)
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/26_seating_generator.png`.

```text
Row 1 :  R X S X
Row 2 :  X S X S
Row 3 :  S X R X
```

## Conclusion
Nested loops visit every seat exactly once, mark reserved positions, and apply the stated checkerboard example rule. The alternating pattern is an explicit assumption because the source sheet does not specify one.
