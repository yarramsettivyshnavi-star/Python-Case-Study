# Case 84: Environmental Monitoring Data Analyzer

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Analyze nested lists of air- or water-quality readings, calculate averages and extremes, and classify observations using supplied threshold values.

## Objectives
Calculate each location’s average and maximum readings and count values above an example threshold.

## Assumptions
- Readings are hypothetical non-negative values arranged by location.
- Values above 50 are labeled high; 50 or below are within the example threshold. The PDF supplies no real threshold.
- No measurement represents actual air or water quality.

## Algorithm
1. Store location names and nested readings.
2. For each location sum readings and track the maximum.
3. Calculate average.
4. Count values above the example threshold.
5. Print summary.

## Flowchart

```text
Start → Read locations, nested data, threshold → Visit each value and update sum and maximum → Classify → Print summary → End
```

## Pseudocode

```text
FOR each location row
    total = 0; maximum = first reading
    FOR each reading: add total; update maximum; classify
    average = total / count
    PRINT average, maximum, high count
```

## Python source code

```python
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
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/84_environmental_data.png`.

```text
North average: 47.0 maximum: 51 readings above illustrative threshold: 1
Central average: 58.0 maximum: 61 readings above illustrative threshold: 3
South average: 35.0 maximum: 40 readings above illustrative threshold: 0
```

## Conclusion
The analyzer summarizes only the sample matrix. It does not make real-world claims about environmental quality.
