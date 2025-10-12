# OHL3: Open-High-Low Average

[Pine Script Implementation of OHL3](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/ohl3.pine)

## Naming Convention

**OHL3** is commonly known as **Mean Price** in technical analysis. This measure averages the opening price with the trading range extremes:

- **OHL3**: Programming/library notation (Open-High-Low average of 3)
- **Mean Price**: Common terminology emphasizing the arithmetic mean
- **Open-Range Average**: Descriptive name showing opening plus range
- **Three-Point Average**: Alternative name emphasizing the three components

## Overview and Purpose

The OHL3 indicator calculates the arithmetic average of the opening, high, and low prices for each bar. This price transformation provides a comprehensive view of the bar's price action by incorporating the session start price along with both range extremes. By including three key price points, OHL3 creates a more complete representation of price behavior than simpler two-point averages, while deliberately excluding the closing price to avoid closing bias.

This measure is particularly useful in markets where opening prices carry significance and where the full trading range provides valuable context. OHL3 offers a balanced perspective that considers where the period started and the full extent of price movement, making it valuable for analysis in markets with significant opening gaps or wide intrabar ranges.

## Core Concepts

* **Three-point balance:** Combines opening price with range extremes for comprehensive price representation
* **Closing exclusion:** Deliberately omits close price to focus on range and opening characteristics
* **Range incorporation:** Captures the full extent of intrabar price movement
* **Opening emphasis:** Gives weight to session start price alongside range boundaries

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Open | open | Opening price data | Typically not adjusted, uses standard open price |
| High | high | High price data | Typically not adjusted, uses standard high price |
| Low | low | Low price data | Typically not adjusted, uses standard low price |

**Pro Tip:** OHL3 is particularly effective in markets with significant opening gaps or where opening prices represent important institutional positioning. Use OHL3 when you want to incorporate opening information without the closing bias present in OHLC4.

## Calculation and Mathematical Foundation

**Simplified explanation:**
OHL3 calculates the arithmetic mean of three key price points: open, high, and low, providing a balanced view of price action excluding the close.

**Technical formula:**

```
OHL3 = (Open + High + Low) / 3
```

Where:
- Open is the price at the start of the period
- High is the highest price reached during the period
- Low is the lowest price reached during the period

> 🔍 **Technical Note:** This calculation maintains O(1) complexity with two additions and one division per bar. The formula is deterministic and requires no historical data, making it suitable for real-time computation.

## Interpretation Details

OHL3 provides several analytical perspectives:

* **Opening incorporation:** Includes session start price in the average, capturing gap information
* **Range representation:** Encompasses both trading range extremes in the calculation
* **Closing independence:** Removes closing bias, focusing on range and opening dynamics
* **Balanced weighting:** Gives equal weight to all three components
* **Gap visibility:** Opening price component makes gaps more visible in the average

## Limitations and Considerations

* **Closing omission:** Does not capture where the period actually finished
* **Time-weighted bias:** Treats all three prices equally regardless of time spent at each level
* **Volume independence:** Does not account for volume distribution across price levels
* **Extreme sensitivity:** Captures high and low extremes that may represent brief spikes
* **No directional bias:** Equal weighting of high and low neutralizes directional information

## References

* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2000). Technical Analysis from A to Z. McGraw-Hill.
