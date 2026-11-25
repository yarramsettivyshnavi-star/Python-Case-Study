# Case 45: Weekly Electricity Consumption Matrix

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Process appliance-wise electricity readings across seven days, calculate daily and appliance totals, and identify consumption exceeding specified limits.

## Objectives
Sum appliance-by-day readings by row and column and flag daily totals over an example limit.

## Assumptions
- Each appliance has seven non-negative illustrative kWh readings.
- The 10 kWh daily threshold is an example only; no actual readings, tariffs, or official limit are supplied.

## Algorithm
1. Store appliance names and readings.
2. Sum each row for appliance totals.
3. Sum each day column for daily totals.
4. Compare each daily total with the example limit and print status.

## Flowchart

```text
Start → Read matrix and limit → Sum rows → Sum each day column → Above limit? flag → Print → End
```

## Pseudocode

```text
FOR each appliance row: sum readings; print total
FOR each day column: sum across appliances
    IF total > limit: flag
    PRINT total and status
```

## Python source code

```python
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
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/45_weekly_electricity_matrix.png`.

```text
Lights weekly total: 12 kWh
Fan weekly total: 19 kWh
Computer weekly total: 36 kWh
Mon total: 10 kWh - within illustrative limit
Tue total: 11 kWh - ABOVE illustrative limit
Wed total: 10 kWh - within illustrative limit
Thu total: 12 kWh - ABOVE illustrative limit
Fri total: 11 kWh - ABOVE illustrative limit
Sat total: 7 kWh - within illustrative limit
Sun total: 6 kWh - within illustrative limit
```

## Conclusion
Totals are computed from the listed sample readings. The threshold is illustrative, not an actual tariff or official consumption limit.
