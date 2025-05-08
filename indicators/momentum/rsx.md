# RSX: Jurik Relative Strength Quality Index

[Pine Script Implementation of RSX](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/rsx.pine)

## Overview and Purpose

Jurik Relative Strength Quality Index (RSX) is an enhanced version of the traditional RSI indicator that solves the common problem of signal noise and false triggers. By incorporating Jurik's JMA (Jurik Moving Average) smoothing algorithm, RSX provides cleaner, more accurate signals while maintaining excellent responsiveness to price changes.

This implementation combines the momentum measurement capabilities of RSI with the advanced adaptive smoothing of JMA, resulting in an indicator that excels at identifying trend reversals and market conditions with significantly reduced noise.

## Core Concepts

* **Enhanced Signal Quality:** Eliminates the jitter common in traditional RSI
* **Adaptive Smoothing:** Uses JMA to dynamically adjust to market conditions
* **Precise Reversals:** Clearer identification of trend reversals
* **Noise Reduction:** Minimizes false signals while maintaining responsiveness
* **Zero-lag Design:** Maintains timing accuracy despite smoothing

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Lookback period for calculations | Lower for faster signals, higher for longer-term trends |
| Source | Close | Price data used for calculation | Consider using hlc3 for more comprehensive price action |

**Pro Tip:** RSX's superior noise reduction allows for:
- Tighter stop levels without premature triggers
- More aggressive overbought/oversold thresholds
- Earlier entry signals with higher confidence
- Better trend acceleration analysis

## Calculation and Mathematical Foundation

**Simplified explanation:**
RSX combines RSI's momentum calculation with JMA's adaptive smoothing to produce cleaner signals.

**Technical formula:**
1. Calculate upward (U) and downward (D) price changes:
   ```
   U = max(close - close[1], 0)
   D = max(close[1] - close, 0)
   ```

2. Apply JMA smoothing to both U and D:
   ```
   smoothU = JMA(U, length)
   smoothD = JMA(D, length)
   ```

3. Calculate the Relative Strength (RS) and RSX:
   ```
   RS = smoothU/smoothD
   RSX = 100 - (100 / (1 + RS))
   ```

> 🔍 **Technical Note:** The JMA algorithm provides superior smoothing through:
> - Adaptive volatility measurement
> - Phase-shifting for minimal lag
> - Dynamic noise reduction
> - Automatic adjustment to market conditions

## Interpretation Details

RSX provides clearer signals across multiple analytical perspectives:

* **Trend Direction:**
  - Above 50: Uptrend with reduced noise
  - Below 50: Downtrend with reduced noise
  - Crossovers more reliable due to reduced whipsaws

* **Market Conditions:**
  - Overbought/Oversold levels more reliable
  - Cleaner divergence patterns
  - Better trend strength measurement
  - More accurate reversal signals

* **Signal Types:**
  - Centerline (50) crossovers for trend changes
  - Overbought/Oversold for reversals
  - Divergence patterns for trend exhaustion
  - Trend acceleration/deceleration analysis

## Advantages Over Traditional RSI

1. **Signal Quality:**
   - Reduced false triggers
   - Clearer trend direction
   - More reliable reversals
   - Better divergence identification

2. **Trading Benefits:**
   - Tighter stop placement
   - Earlier entry signals
   - More meaningful thresholds
   - Reduced whipsaw risk

3. **Analysis Improvements:**
   - Clearer market structure
   - Better trend quality assessment
   - More accurate momentum measurement
   - Enhanced reversal detection

## Limitations and Considerations

* **Learning Curve:** May require adjustment period for RSI users
* **Complexity:** More sophisticated than simple momentum measures
* **Resource Usage:** Higher computational requirements

## References

* Jurik Research. "RSX - Relative Strength Quality Index". http://jurikres.com/catalog1/ms_rsx.htm#top
* Jurik, M. "JMA - Jurik Moving Average". Jurik Research.
