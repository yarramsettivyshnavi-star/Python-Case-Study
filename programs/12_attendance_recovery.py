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
