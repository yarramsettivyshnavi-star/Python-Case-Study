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
