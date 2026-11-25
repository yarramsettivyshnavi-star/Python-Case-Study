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
