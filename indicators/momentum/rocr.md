# ROCR: Rate of Change Ratio

[Pine Script Implementation of ROCR](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/rocr.pine)

## Overview and Purpose

The Rate of Change Ratio (ROCR) indicator measures the ratio between the current price and the price N periods ago. This momentum oscillator helps identify the relative magnitude of price changes as a ratio, making it particularly useful for multiplicative analysis.

## Core Concepts

* **Price Ratio:** Measures relative price relationship over time
* **Momentum:** Indicates strength and speed of price movements
* **Oscillator:** Fluctuates around one
* **Multiplicative Scale:** Useful for geometric analysis

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | close | Price data to analyze | Use high/low for range analysis |
| Length | 9 | Lookback period | Shorter for faster signals |

**Pro Tip:** Common lookback periods:
- 12 periods for short-term analysis
- 25 periods for medium-term trends
- 50+ periods for long-term momentum

## Calculation and Mathematical Foundation

**Simplified explanation:**
ROCR calculates the ratio between current price and historical price.

**Technical formula:**
```
ROCR = Price(t) / Price(t-n)
```

> 🔍 **Technical Note:** The ratio calculation provides a multiplicative view that's useful for geometric analysis and compound growth assessment.

## Interpretation Details

ROCR provides multiple analytical perspectives:

* **Trend Direction:**
  - Above 1: Price increasing
  - Below 1: Price decreasing
  - At 1: No change

* **Momentum Strength:**
  - Higher values: Stronger upward momentum
  - Lower values: Stronger downward momentum
  - Near 1: Weak momentum

* **Signal Types:**
  - Unity line crossovers
  - Divergence patterns
  - Extreme readings
  - Trend confirmation

## Advantages

1. **Analytical Benefits:**
   - Multiplicative measurement
   - Geometric interpretation
   - Cross-asset comparison
   - Compound growth analysis

2. **Trading Applications:**
   - Trend identification
   - Entry/exit timing
   - Divergence trading
   - Geometric progression analysis

3. **Technical Benefits:**
   - Simple calculation
   - Flexible parameters
   - Multiple timeframes
   - Clear signals

## Limitations and Considerations

* **Lagging Indicator:** Signals occur after price moves
* **Multiplicative Scale:** May need log transformation for analysis
* **Timeframe Dependent:** Different periods show different patterns
* **Market Context:** Works best in trending markets

## Related Indicators

* **ROC:** Absolute version of ROCR
* **ROCP:** Percentage version of ROCR
* **Momentum:** Similar concept but different scaling
* **Velocity:** Rate of change with additional smoothing

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2001). Technical Analysis from A to Z. McGraw Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
