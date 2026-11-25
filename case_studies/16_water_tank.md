# Case 16: Multi-Day Water Tank Simulation

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Process changing inflow and outflow, update water levels, detect overflow and shortages, and determine the first interval reaching a specified threshold.

## Objectives
Update tank levels over supplied daily inflow and outflow, flag overflow and shortages, and report the first day reaching a target.

## Assumptions
- Inflow and outflow lists have equal length and describe one interval per item.
- Inflow is added before outflow; excess above capacity is overflow.
- If outflow exceeds available water, shortage is reported and the level becomes zero; unmet outflow is not carried forward.
- All values are hypothetical non-negative volume units.

## Algorithm
1. Set initial level, capacity, and target.
2. For each day add inflow and cap at capacity, recording overflow.
3. Subtract outflow or record shortage and set level to zero.
4. Record the first day ending at or above target.
5. Print daily balance.

## Flowchart

```text
Start → Initialize level → Add inflow → Overflow? cap at capacity → Outflow exceeds level? shortage and zero : subtract outflow → Target first reached? record day → Print → End
```

## Pseudocode

```text
FOR each day
    level = level + inflow[day]
    IF level > capacity: record overflow; level = capacity
    IF outflow[day] > level: record shortage; level = 0
    ELSE: level = level - outflow[day]
    IF level >= target and no day recorded: save day
    PRINT daily result
```

## Python source code

```python
starting_level = 40
capacity = 100
target_level = 60
inflows = [30, 70, 10, 0]
outflows = [20, 15, 30, 100]
level = starting_level
first_target_day = 0

for day in range(len(inflows)):
    level = level + inflows[day]
    overflow = 0
    shortage = 0
    if level > capacity:
        overflow = level - capacity
        level = capacity
    if outflows[day] > level:
        shortage = outflows[day] - level
        level = 0
    else:
        level = level - outflows[day]
    if level >= target_level and first_target_day == 0:
        first_target_day = day + 1
    print("Day", day + 1, "ending level:", level, "overflow:", overflow, "shortage:", shortage)
if first_target_day == 0:
    print("Target was not reached")
else:
    print("First day target reached:", first_target_day)
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/16_water_tank.png`.

```text
Day 1 ending level: 50 overflow: 0 shortage: 0
Day 2 ending level: 85 overflow: 20 shortage: 0
Day 3 ending level: 65 overflow: 0 shortage: 0
Day 4 ending level: 0 overflow: 0 shortage: 35
First day target reached: 2
```

## Conclusion
The balance uses the stated inflow-first assumption and reports overflow and unmet outflow. These values are examples, not real tank measurements.
