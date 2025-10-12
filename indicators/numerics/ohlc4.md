# OHLC4: OHLC Average

[Pine Script Implementation of OHLC4](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/ohlc4.pine)

## Naming Convention

**OHLC4** is commonly referred to as **Average Price** in technical analysis. This comprehensive measure includes all four standard price components:

- **OHLC4**: Programming/library notation (Open-High-Low-Close average of 4)
- **Average Price**: Most common name in technical analysis
- **Four-Price Average**: Descriptive name emphasizing all components
- **Complete Price Average**: Alternative terminology

## Overview and Purpose

The OHLC4 indicator calculates the arithmetic average of all four standard price points: open, high, low, and close. This comprehensive price transformation provides the most complete single-value representation of a bar's price action by incorporating the session start, both range extremes, and the final settlement price. OHLC4 offers the most balanced view of price behavior among common price transformations, giving equal weight to all major price components.

This measure is particularly valuable when you want a thoroughly averaged price that considers every key aspect of the bar's price action. By including all four OHLC prices, this transformation creates a highly smoothed price series that reduces the impact of any single price component while maintaining sensitivity to overall price behavior.

## Core Concepts

* **Complete representation:** Incorporates all four standard price points for comprehensive averaging
* **Maximum balance:** Gives equal weight to opening, range extremes, and closing prices
* **Smoothest transformation:** Creates the most averaged price series among standard transformations
* **Full bar context:** Captures where period started, traded, and finished

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Open | open | Opening price data | Typically not adjusted, uses standard open price |
| High | high | High price data | Typically not adjusted, uses standard high price |
| Low | low | Low price data | Typically not adjusted, uses standard low price |
| Close | close | Closing price data | Typically not adjusted, uses standard close price |

**Pro Tip:** OHLC4 provides the most smoothed price series among standard transformations, making it ideal for noise reduction in very volatile markets. Use OHLC4 when you want maximum averaging effect while maintaining representation of all price components.

## Calculation and Mathematical Foundation

**Simplified explanation:**
OHLC4 calculates the arithmetic mean of all four standard price points, providing the most complete averaged price representation.

**Technical formula:**

```
OHLC4 = (Open + High + Low + Close) / 4
```

Where:
- Open is the price at the start of the period
- High is the highest price reached during the period
- Low is the lowest price reached during the period
- Close is the closing price at the end of the period

> 🔍 **Technical Note:** This calculation maintains O(1) complexity with three additions and one division per bar. The formula is deterministic and computationally efficient, suitable for real-time applications.

## Interpretation Details

OHLC4 provides several analytical perspectives:

* **Comprehensive averaging:** Most complete single-value price representation available
* **Maximum smoothing:** Creates smoothest price series among standard transformations
* **Balanced weighting:** Treats all four price components with equal importance
* **Noise reduction:** Most effective at filtering out price spikes and extremes
* **Full bar representation:** Captures opening, range, and closing information simultaneously

## Limitations and Considerations

* **Over-smoothing:** May lag price action due to averaging all four components
* **Equal weighting assumption:** Treats all prices equally regardless of time spent at each level
* **Volume independence:** Does not account for volume distribution across price levels
* **Extreme inclusion:** Still captures high and low extremes that may represent brief spikes
* **Responsiveness trade-off:** Maximum averaging reduces sensitivity to rapid price changes

## References

* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2000). Technical Analysis from A to Z. McGraw-Hill.
