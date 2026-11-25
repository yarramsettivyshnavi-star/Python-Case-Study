locations = ["North", "Central", "South"]
readings = [[42, 48, 51], [55, 61, 58], [30, 35, 40]]
threshold = 50
for row in range(len(readings)):
    total = 0
    maximum = readings[row][0]
    high_count = 0
    for value in readings[row]:
        total = total + value
        if value > maximum:
            maximum = value
        if value > threshold:
            high_count = high_count + 1
    average = total / len(readings[row])
    print(locations[row], "average:", round(average, 2), "maximum:", maximum, "readings above illustrative threshold:", high_count)
