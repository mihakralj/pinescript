# RSI: Relative Strength Index

[Pine Script Implementation of RSI](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/rsi.pine)

## Overview and Purpose

The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and magnitude of recent price changes to evaluate overbought or oversold conditions. Developed by J. Welles Wilder Jr. and introduced in his 1978 book "New Concepts in Technical Trading Systems", RSI has become one of the most popular and widely used technical indicators.

This implementation uses Wilder's original smoothing method, which is equivalent to an exponential moving average with a smoothing factor of 1/length. The indicator oscillates between 0 and 100, with traditional overbought and oversold levels at 70 and 30 respectively.

## Core Concepts

* **Momentum measurement:** Compares upward and downward price movements
* **Overbought/Oversold levels:** Identifies potential reversal points
* **Wilder's smoothing:** Reduces noise while maintaining responsiveness
* **Divergence analysis:** Helps identify potential trend reversals
* **Centerline crossovers:** Indicates shift in momentum direction

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Lookback period for calculations | Lower for faster signals but more noise, higher for smoother readings |
| Source | Close | Price data used for calculation | Consider using hlc3 for more comprehensive price action |

**Pro Tip:** While the default 14-period setting works well for daily charts, consider:
- 9-11 periods for intraday trading
- 14-21 periods for daily charts
- 21-30 periods for weekly analysis
- Adjusting overbought/oversold levels based on market conditions (e.g., 80/20 for strong trends)

## Calculation and Mathematical Foundation

**Simplified explanation:**
RSI compares the magnitude of recent gains to recent losses to determine overbought/oversold conditions and momentum.

**Technical formula:**
1. Calculate upward (U) and downward (D) price changes:
   ```
   U = max(close - close[1], 0)
   D = max(close[1] - close, 0)
   ```

2. Apply Wilder's smoothing to both U and D:
   ```
   smoothU = prevU * (len-1)/(len) + U * 1/len
   smoothD = prevD * (len-1)/(len) + D * 1/len
   ```

3. Calculate the Relative Strength (RS) and RSI:
   ```
   RS = smoothU/smoothD
   RSI = 100 - (100 / (1 + RS))
   ```

> 🔍 **Technical Note:** The implementation uses Wilder's smoothing method, which is similar to an EMA but with a specific alpha calculation (1/length). This provides a balance between responsiveness and noise reduction.

## Interpretation Details

RSI provides multiple analytical perspectives:

* **Overbought/Oversold:**
  - Above 70: Potentially overbought
  - Below 30: Potentially oversold
  - Extreme readings suggest increased reversal probability

* **Centerline (50) Analysis:**
  - Above 50: Generally bullish momentum
  - Below 50: Generally bearish momentum
  - Crossovers can signal trend changes

* **Divergence Patterns:**
  - Bullish: Price makes lower lows while RSI makes higher lows
  - Bearish: Price makes higher highs while RSI makes lower highs
  - Hidden divergences can confirm trend continuation

* **Failure Swings:**
  - Bullish: RSI falls into oversold, bounces, pulls back above oversold, then breaks resistance
  - Bearish: RSI rises into overbought, drops, pulls back below overbought, then breaks support

## Limitations and Considerations

* **Lag Component:** Uses smoothed data, introducing some delay in signals
* **False Signals:** Can remain in extreme territories during strong trends
* **Timeframe Dependency:** Different periods needed for different timeframes
* **Trend Context:** Best used alongside trend identification tools
* **Range Bound:** May not capture absolute momentum magnitude
* **Market Conditions:** More reliable in ranging markets than strong trends

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.