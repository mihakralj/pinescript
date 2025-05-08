# PPO: Percentage Price Oscillator

[Pine Script Implementation of PPO](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/ppo.pine)

## Overview and Purpose

The Percentage Price Oscillator (PPO) is a momentum indicator that measures the percentage difference between two exponential moving averages. Similar to the MACD, but expressed in percentage terms, making it more suitable for comparing assets with different price levels. The PPO helps identify trend direction, momentum, and potential reversal points.

This implementation calculates the percentage difference between fast and slow EMAs, along with a signal line and histogram for additional confirmation signals.

## Core Concepts

* **Percentage-Based:** Shows relative price changes as percentages
* **Trend Following:** Identifies trend direction and strength
* **Momentum Measurement:** Indicates acceleration/deceleration
* **Signal Line:** Provides trade timing signals
* **Histogram:** Shows momentum shifts visually

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Fast Length | 12 | Fast EMA period | Lower for faster signals |
| Slow Length | 26 | Slow EMA period | Higher for longer-term trends |
| Signal Length | 9 | Signal line smoothing | Affects crossover timing |

**Pro Tip:** Common combinations:
- Short-term: Fast(8), Slow(17), Signal(9)
- Default: Fast(12), Slow(26), Signal(9)
- Long-term: Fast(19), Slow(39), Signal(9)

## Calculation and Mathematical Foundation

**Simplified explanation:**
PPO expresses the difference between two EMAs as a percentage of the slower EMA.

**Technical formula:**
1. Calculate Fast and Slow EMAs:
   ```
   Fast_EMA = EMA(price, fast_length)
   Slow_EMA = EMA(price, slow_length)
   ```

2. Calculate PPO Line:
   ```
   PPO = 100 * (Fast_EMA - Slow_EMA) / Slow_EMA
   ```

3. Calculate Signal Line:
   ```
   Signal = EMA(PPO, signal_length)
   ```

4. Calculate Histogram:
   ```
   Histogram = PPO - Signal
   ```

> 🔍 **Technical Note:** The percentage calculation makes PPO values comparable across different securities, unlike MACD which uses absolute price differences.

## Interpretation Details

PPO provides multiple analytical perspectives:

* **Trend Direction:**
  - Positive PPO: Bullish trend
  - Negative PPO: Bearish trend
  - Zero line crossovers: Major trend changes

* **Signal Line Crossovers:**
  - PPO crosses above Signal: Bullish signal
  - PPO crosses below Signal: Bearish signal
  - More reliable near extremes

* **Histogram Analysis:**
  - Growing: Increasing momentum
  - Shrinking: Decreasing momentum
  - Zero crossings: Potential trend changes

* **Divergence Patterns:**
  - Bullish: Price lower lows, PPO higher lows
  - Bearish: Price higher highs, PPO lower highs
  - Most effective at extremes

## Advantages

1. **Comparison Benefits:**
   - Percentage-based calculation
   - Cross-asset comparison
   - Historical comparison
   - Portfolio analysis

2. **Trading Applications:**
   - Trend identification
   - Momentum confirmation
   - Reversal signals
   - Divergence trading

3. **Technical Benefits:**
   - Multiple signal types
   - Visual momentum display
   - Clear entry/exit points
   - Trend strength measurement

## Limitations and Considerations

* **Lag Component:** Moving average based calculations introduce delay
* **False Signals:** Can occur in ranging markets
* **Whipsaws:** Common around zero line in choppy conditions
* **Confirmation:** Best used with other indicators
* **Timeframe Dependent:** Different settings needed for different timeframes

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Appel, G. (2005). Technical Analysis: Power Tools for Active Investors. Financial Times Prentice Hall.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
