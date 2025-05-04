# Andrews' Pitchfork

[Pine Script Implementation of AP](https://github.com/mihakralj/pinescript/blob/main/indicators/channels/ap.pine)

Andrews' Pitchfork is a technical analysis tool consisting of three parallel trendlines created by selecting three points on a chart. The tool helps identify potential support and resistance levels, as well as trend direction.

## Calculation

The indicator creates three lines:
- Median Line: Drawn from the first point (P1) to the midpoint between points P2 and P3
- Upper Line: Parallel line through P2
- Lower Line: Parallel line through P3

```
MidPoint = (P2_price + P3_price) / 2
Slope = (MidPoint - P1_price) / (P1_time - MidPoint_time)
MedianLine = P1_price + Slope * (CurrentBar - P1_time)
UpperLine = P2_price + Slope * (CurrentBar - P2_time)
LowerLine = P3_price + Slope * (CurrentBar - P3_time)
```

## Parameters

- Point 1 (default: 45) - Leftmost pivot point, typically a significant high or low
- Point 2 (default: 30) - Second pivot point, typically a reaction high
- Point 3 (default: 15) - Third pivot point, typically a reaction low

Points must be in chronological order: P1 > P2 > P3 (oldest to newest)

## Interpretation

- The median line represents the primary trend
- Upper and lower lines form a channel that can act as support and resistance
- Price tends to oscillate between the outer lines while respecting the median line
- When price breaks out of the channel, it may signal a trend change
- The tool is most effective when the three points are chosen at significant pivots

## Implementation

The implementation uses optimized calculations with validation checks for:
- Chronological order of points
- Division by zero prevention
- Handling NA values
- Numerical stability for large time differences
- Prevention of extreme values that could cause rendering issues
