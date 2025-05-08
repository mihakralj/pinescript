# ROC: Rate of Change

[Pine Script Implementation of ROC](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/roc.pine)

## Overview and Purpose

The Rate of Change (ROC) indicator measures the absolute change in price between the current price and the price N periods ago. This momentum oscillator helps identify the magnitude of price changes in absolute terms.

## Core Concepts

* **Absolute Change:** Measures raw price difference over time
* **Momentum:** Indicates strength and speed of price movements
* **Oscillator:** Fluctuates above and below zero
* **Trend Analysis:** Helps identify trend strength and reversals

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
ROC calculates the absolute difference between current price and historical price.

**Technical formula:**
```
ROC = Price(t) - Price(t-n)
```

> 🔍 **Technical Note:** The absolute calculation shows actual price movement magnitude in the asset's price units.

## Interpretation Details

ROC provides multiple analytical perspectives:

* **Trend Direction:**
  - Positive: Price increasing
  - Negative: Price decreasing
  - Zero line: No change

* **Momentum Strength:**
  - Higher values: Stronger momentum
  - Lower values: Weaker momentum
  - Divergence: Potential trend reversal

* **Signal Types:**
  - Zero line crossovers
  - Divergence patterns
  - Extreme readings
  - Trend confirmation

## Advantages

1. **Analytical Benefits:**
   - Direct price change measurement
   - Easy to interpret
   - Versatile application
   - Trend confirmation

2. **Trading Applications:**
   - Trend identification
   - Entry/exit timing
   - Divergence trading
   - Momentum analysis

3. **Technical Benefits:**
   - Simple calculation
   - Flexible parameters
   - Multiple timeframes
   - Clear signals

## Limitations and Considerations

* **Lagging Indicator:** Signals occur after price moves
* **Scale Dependent:** Values vary with price scale
* **Timeframe Dependent:** Different periods show different patterns
* **Market Context:** Works best in trending markets

## Related Indicators

* **ROCP:** Percentage version of ROC
* **ROCR:** Ratio version of ROC
* **Momentum:** Similar concept but different scaling
* **Velocity:** Rate of change with additional smoothing

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2001). Technical Analysis from A to Z. McGraw Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
