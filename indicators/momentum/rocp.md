# ROCP: Rate of Change Percentage

[Pine Script Implementation of ROCP](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/rocp.pine)

## Overview and Purpose

The Rate of Change Percentage (ROCP) indicator measures the percentage change in price between the current price and the price N periods ago. This momentum oscillator helps identify the magnitude of price changes in percentage terms, making it comparable across different price scales.

## Core Concepts

* **Percentage Change:** Measures relative price difference over time
* **Momentum:** Indicates strength and speed of price movements
* **Oscillator:** Fluctuates above and below zero
* **Scale Independence:** Comparable across different price ranges

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
ROCP calculates the percentage difference between current price and historical price.

**Technical formula:**
```
ROCP = 100 * (Price(t) - Price(t-n)) / Price(t-n)
```

> 🔍 **Technical Note:** The percentage calculation provides a normalized view that's comparable across different price scales.

## Interpretation Details

ROCP provides multiple analytical perspectives:

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
   - Scale-independent measurement
   - Easy to interpret
   - Cross-asset comparison
   - Trend confirmation

2. **Trading Applications:**
   - Trend identification
   - Entry/exit timing
   - Divergence trading
   - Cross-market analysis

3. **Technical Benefits:**
   - Simple calculation
   - Flexible parameters
   - Multiple timeframes
   - Clear signals

## Limitations and Considerations

* **Lagging Indicator:** Signals occur after price moves
* **Base Effect:** Large changes from low base values
* **Timeframe Dependent:** Different periods show different patterns
* **Market Context:** Works best in trending markets

## Related Indicators

* **ROC:** Absolute version of ROCP
* **ROCR:** Ratio version of ROCP
* **Momentum:** Similar concept but different scaling
* **Velocity:** Rate of change with additional smoothing

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2001). Technical Analysis from A to Z. McGraw Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
