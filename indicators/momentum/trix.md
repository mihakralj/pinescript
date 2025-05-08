# TRIX: Triple Exponential Average ROC

[Pine Script Implementation of TRIX](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/trix.pine)

## Overview and Purpose

The TRIX (Triple Exponential Average ROC) indicator is a momentum oscillator that shows the percentage rate of change of a triple exponentially smoothed moving average. By using triple smoothing, TRIX filters out insignificant price movements and helps identify stronger trends.

## Core Concepts

* **Triple Smoothing:** Three EMA calculations to reduce noise
* **Rate of Change:** Percentage change calculation
* **Momentum:** Indicates strength and speed of price movements
* **Oscillator:** Fluctuates above and below zero

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | close | Price data to analyze | Use high/low for range analysis |
| Length | 18 | Lookback period | Shorter for faster signals |

**Pro Tip:** Common lookback periods:
- 15 periods for short-term analysis
- 18 periods for medium-term trends
- 30 periods for long-term momentum

## Calculation and Mathematical Foundation

**Simplified explanation:**
1. Calculate EMA of price
2. Calculate EMA of first EMA
3. Calculate EMA of second EMA
4. Calculate percentage change of triple EMA

**Technical formula:**
```
EMA1 = EMA(price, length)
EMA2 = EMA(EMA1, length)
EMA3 = EMA(EMA2, length)
TRIX = 100 * (EMA3 - EMA3[1]) / EMA3[1]
```

> 🔍 **Technical Note:** Triple smoothing effectively filters out high-frequency noise while preserving the underlying trend.

## Interpretation Details

TRIX provides multiple analytical perspectives:

* **Trend Direction:**
  - Positive: Upward momentum
  - Negative: Downward momentum
  - Zero line: No momentum

* **Signal Strength:**
  - Higher values: Stronger momentum
  - Lower values: Weaker momentum
  - Divergence: Potential trend reversal

* **Signal Types:**
  - Zero line crossovers
  - Signal line crossovers
  - Divergence patterns
  - Overbought/oversold levels

## Advantages

1. **Analytical Benefits:**
   - Noise reduction
   - Trend identification
   - Momentum measurement
   - Signal clarity

2. **Trading Applications:**
   - Trend confirmation
   - Entry/exit timing
   - Divergence trading
   - Momentum analysis

3. **Technical Benefits:**
   - Triple smoothing
   - Early signal generation
   - Multiple timeframes
   - Clear signals

## Limitations and Considerations

* **Lagging Indicator:** Triple smoothing increases lag
* **Whipsaws:** Can produce false signals in choppy markets
* **Timeframe Dependent:** Different periods show different patterns
* **Market Context:** Works best in trending markets

## Related Indicators

* **ROC:** Simple rate of change
* **MACD:** Double smoothed momentum
* **EMA:** Single exponential average
* **RSI:** Relative strength index

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2001). Technical Analysis from A to Z. McGraw Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
