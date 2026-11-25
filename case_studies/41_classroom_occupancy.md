# Case 41: Nested List Classroom Occupancy Analysis

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Represent classrooms and seating positions as nested lists; allocate students, preserve reserved seats, detect duplicate assignments, and calculate vacant capacity.

## Objectives
Count occupied, vacant, and reserved states in a nested matrix and identify repeated student IDs in a supplied assignment list.

## Assumptions
- The seating matrix is rectangular.
- 1 means occupied, 0 vacant, and -1 reserved.
- Student IDs are checked separately; this demonstration reports duplicates but does not perform allocation.

## Algorithm
1. Traverse each room row and count each seat state.
2. Compare each pair of student IDs.
3. Record repeated IDs once.
4. Print room counts and duplicates.

## Flowchart

```text
Start → Read matrix and IDs → Count 1/0/-1 per room → Compare ID pairs → Duplicate? record → Print summary → End
```

## Pseudocode

```text
FOR each room row
    count occupied, vacant, reserved
    PRINT counts
FOR each ID pair
    IF equal: add ID once to duplicates
PRINT duplicates
```

## Python source code

```python
classrooms = [[1, 0, -1, 1], [0, 1, 0, -1]]
assigned_ids = ["S01", "S02", "S01", "S03"]

for room_number in range(len(classrooms)):
    occupied = 0
    vacant = 0
    reserved = 0
    for seat in classrooms[room_number]:
        if seat == 1:
            occupied = occupied + 1
        elif seat == 0:
            vacant = vacant + 1
        elif seat == -1:
            reserved = reserved + 1
    print("Room", room_number + 1, "occupied:", occupied, "vacant:", vacant, "reserved:", reserved)
duplicates = []
for first in range(len(assigned_ids)):
    for second in range(first + 1, len(assigned_ids)):
        if assigned_ids[first] == assigned_ids[second] and assigned_ids[first] not in duplicates:
            duplicates.append(assigned_ids[first])
print("Duplicate assigned IDs:", duplicates)
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/41_classroom_occupancy.png`.

```text
Room 1 occupied: 2 vacant: 1 reserved: 1
Room 2 occupied: 1 vacant: 2 reserved: 1
Duplicate assigned IDs: ['S01']
```

## Conclusion
Nested lists enable seat-state counts and ID-pair comparisons. A real allocator needs explicit assignment and reserved-seat rules.
