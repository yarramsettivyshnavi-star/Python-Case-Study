appliance_names = ["Lights", "Fan", "Computer"]
readings = [[2, 2, 2, 2, 2, 1, 1], [3, 3, 3, 3, 3, 2, 2], [5, 6, 5, 7, 6, 4, 3]]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
daily_limit = 10

for row in range(len(readings)):
    appliance_total = 0
    for value in readings[row]:
        appliance_total = appliance_total + value
    print(appliance_names[row], "weekly total:", appliance_total, "kWh")
for day in range(7):
    daily_total = 0
    for appliance in range(len(readings)):
        daily_total = daily_total + readings[appliance][day]
    if daily_total > daily_limit:
        status = "ABOVE illustrative limit"
    else:
        status = "within illustrative limit"
    print(days[day], "total:", daily_total, "kWh -", status)
