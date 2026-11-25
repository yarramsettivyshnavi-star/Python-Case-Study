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
