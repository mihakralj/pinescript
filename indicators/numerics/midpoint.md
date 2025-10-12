# MIDPOINT: Period Midpoint

[Pine Script Implementation of MIDPOINT](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/midpoint.pine)

## Overview and Purpose

The MIDPOINT indicator calculates the arithmetic average of the highest high and lowest low values over a specified lookback period. Unlike the simple HL2 which uses only the current bar's high and low, MIDPOINT examines a range of historical bars to find the extreme values over that period and then averages them. This creates a dynamic center line that represents the midpoint of the price range over the specified timeframe, providing a reference level that adapts to recent price action.

This indicator is particularly useful for identifying the central tendency of price movement over a given period, serving as a dynamic support/resistance level or as a baseline for mean reversion strategies. The MIDPOINT naturally adjusts to changing market conditions by recalculating based on the rolling highest and lowest values, making it more responsive to trend changes than fixed-period moving averages.

## Core Concepts

* **Period extremes:** Identifies the highest and lowest prices over the lookback period
* **Dynamic center:** Creates an adaptive midpoint that moves with price range changes
* **Range reference:** Provides the mathematical center of recent price action
* **Mean reversion baseline:** Serves as natural equilibrium point for oscillations

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Source | Close | Price data used for finding extremes | Consider using high/low for true range extremes instead of close |
| Length | 14 | Lookback period for finding highest/lowest | Increase for longer-term center line; decrease for more responsive reference |

**Pro Tip:** MIDPOINT is particularly effective when combined with other indicators for confluence. Consider using different timeframes simultaneously - a short-period MIDPOINT (7-10 bars) for immediate support/resistance and a longer-period MIDPOINT (20-30 bars) for major equilibrium levels.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MIDPOINT calculates the center point between the highest and lowest values over a specified period, creating a dynamic reference level that adapts to price movements.

**Technical formula:**

```
MIDPOINT = (Highest(Source, Length) + Lowest(Source, Length)) / 2
```

Where:
- Highest(Source, Length) finds the maximum value of Source over Length bars
- Lowest(Source, Length) finds the minimum value of Source over Length bars
- The result is the arithmetic mean of these two extremes

> 🔍 **Technical Note:** This implementation uses built-in `ta.highest()` and `ta.lowest()` functions for efficiency. While the calculation itself is O(1) per bar, the underlying highest/lowest functions maintain O(n) complexity where n is the length parameter, though they are optimized internally for performance.

## Interpretation Details

MIDPOINT provides several analytical perspectives:

* **Dynamic support/resistance:** The midpoint often acts as a natural pivot level where price tends to oscillate around
* **Range equilibrium:** Represents the mathematical center of recent price range, useful for mean reversion analysis
* **Trend strength indicator:** When price consistently stays above/below midpoint, it suggests strong directional bias
* **Volatility context:** Distance between current price and midpoint indicates relative position within recent range
* **Breakout reference:** Significant moves beyond the midpoint can signal potential trend changes

## Limitations and Considerations

* **Lag component:** Uses historical data to calculate, introducing inherent lag in the reference level
* **Extreme sensitivity:** Sensitive to outlier highs and lows that may not represent sustained price levels
* **No directional bias:** Simply represents midpoint without indicating trend direction
* **Period dependency:** Results heavily dependent on chosen length parameter
* **Whipsaw potential:** Can generate false signals in choppy, range-bound markets
* **Not predictive:** Shows where center was, not necessarily where it will be

## References

* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
