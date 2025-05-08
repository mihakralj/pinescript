# PMO: Price Momentum Oscillator

[Pine Script Implementation of PMO](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/pmo.pine)

## Overview and Purpose

The Price Momentum Oscillator (PMO) is a momentum indicator that measures the rate of change in price and applies double exponential smoothing to reduce noise. It combines the trend-following capabilities of Rate of Change (ROC) with the smoothing benefits of exponential moving averages, resulting in a cleaner momentum signal.

This implementation uses a three-step calculation process: initial ROC computation followed by two stages of EMA smoothing. The indicator also includes a signal line for generating crossover signals.

## Core Concepts

* **Rate of Change:** Measures price momentum as percentage change
* **Double Smoothing:** Reduces noise while maintaining responsiveness
* **Signal Line:** Provides crossover signals for trade timing
* **Zero Line:** Acts as trend direction reference
* **Momentum Divergence:** Helps identify potential reversals

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| ROC Length | 35 | Base momentum calculation period | Lower for faster signals, higher for longer-term trends |
| First Smoothing | 20 | Initial EMA smoothing period | Affects primary noise reduction |
| Second Smoothing | 10 | Final EMA smoothing period | Fine-tunes signal smoothness |
| Signal Line | 10 | Signal line EMA period | Adjust for optimal crossover signals |

**Pro Tip:** Consider these combinations:
- Short-term: ROC(20), Smooth1(10), Smooth2(5)
- Medium-term: ROC(35), Smooth1(20), Smooth2(10)
- Long-term: ROC(50), Smooth1(30), Smooth2(15)

## Calculation and Mathematical Foundation

**Simplified explanation:**
PMO applies double exponential smoothing to a percentage rate of change calculation.

**Technical formula:**
1. Calculate Rate of Change:
   ```
   ROC = 100 * (price - price[length]) / price[length]
   ```

2. Apply first EMA smoothing:
   ```
   alpha1 = 2 / (smooth1_length + 1)
   EMA1 = EMA1[1] * (1 - alpha1) + ROC * alpha1
   ```

3. Apply second EMA smoothing:
   ```
   alpha2 = 2 / (smooth2_length + 1)
   PMO = EMA2[1] * (1 - alpha2) + EMA1 * alpha2
   ```

4. Calculate Signal Line:
   ```
   Signal = EMA(PMO, signal_length)
   ```

> 🔍 **Technical Note:** The double smoothing process helps eliminate noise while maintaining the indicator's responsiveness to significant price movements. The signal line provides additional confirmation through crossovers.

## Interpretation Details

PMO provides multiple analytical perspectives:

* **Trend Direction:**
  - Above zero: Bullish momentum
  - Below zero: Bearish momentum
  - Slope indicates trend strength

* **Signal Line Crossovers:**
  - PMO crosses above Signal: Bullish signal
  - PMO crosses below Signal: Bearish signal
  - More reliable near extremes

* **Divergence Analysis:**
  - Bullish: Price makes lower lows while PMO makes higher lows
  - Bearish: Price makes higher highs while PMO makes lower highs
  - Most effective at market extremes

* **Overbought/Oversold:**
  - Extreme readings suggest potential reversals
  - More reliable with divergence confirmation
  - Consider market context

## Advantages

1. **Signal Quality:**
   - Reduced noise through double smoothing
   - Clear trend direction identification
   - Reliable momentum measurement

2. **Trading Applications:**
   - Multiple signal generation methods
   - Trend confirmation capability
   - Divergence identification
   - Timing optimization

3. **Versatility:**
   - Works across different timeframes
   - Adaptable to various markets
   - Configurable for different trading styles

## Limitations and Considerations

* **Lag Component:** Double smoothing introduces some delay
* **Parameter Sensitivity:** Results vary with different settings
* **False Signals:** Can occur during ranging markets
* **Context Required:** Best used with other indicators
* **Timeframe Dependent:** Different settings needed for different timeframes

## References

* Swannell, P. "Technical Analysis Using Multiple Timeframes". Marketplace Books.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
