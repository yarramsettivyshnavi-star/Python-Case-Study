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
