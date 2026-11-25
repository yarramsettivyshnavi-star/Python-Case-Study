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
