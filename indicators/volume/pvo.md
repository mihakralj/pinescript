# PVO: Percentage Volume Oscillator

[Pine Script Implementation of PVO](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/pvo.pine)

## Overview and Purpose

The Percentage Volume Oscillator (PVO) is a momentum indicator that measures the relationship between short-term and long-term volume moving averages, expressed as a percentage. Similar to the Price Percentage Oscillator (PPO) but applied to volume data, PVO helps traders identify changes in volume momentum and potential trend confirmations or divergences. Developed as an extension of traditional volume analysis, PVO provides a normalized view of volume trends that can be compared across different securities and time periods.

## Core Concepts

* **Volume momentum measurement:** Compares short-term volume activity to long-term volume trends using percentage calculations
* **Trend confirmation:** Rising PVO suggests increasing volume momentum supporting price moves
* **Divergence analysis:** PVO divergences from price can signal potential trend changes
* **Normalized comparison:** Percentage format allows comparison across different securities and volume scales
* **Signal line crossovers:** Optional signal line provides additional entry/exit signals

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Fast Period | 12 | Short-term volume moving average period | Decrease for more sensitive signals, increase for smoother readings |
| Slow Period | 26 | Long-term volume moving average period | Adjust based on analysis timeframe - longer for position trading |
| Signal Period | 9 | Signal line smoothing period | Shorter for faster signals, longer for confirmation |
| MA Type | EMA | Moving average type for calculations | SMA for equal weighting, EMA for recent emphasis |

**Pro Tip:** PVO works best when combined with price momentum indicators. Look for PVO confirmation of price breakouts - rising PVO during price breakouts suggests strong volume support.

## Calculation and Mathematical Foundation

**Simplified explanation:**
PVO calculates the percentage difference between a fast volume moving average and a slow volume moving average, then optionally adds a signal line for crossover signals.

**Technical formula:**
```
Fast MA = MA(Volume, Fast Period)
Slow MA = MA(Volume, Slow Period)
PVO = ((Fast MA - Slow MA) / Slow MA) × 100
Signal Line = MA(PVO, Signal Period)
Histogram = PVO - Signal Line
```

Where MA can be SMA, EMA, or other moving average types.

> 🔍 **Technical Note:** The implementation uses exponential moving averages by default for responsiveness, with proper handling of zero volume periods to avoid division errors. The percentage calculation normalizes the oscillator, making it comparable across different securities regardless of their average volume levels.

## Interpretation Details

PVO provides multiple analytical perspectives:

* **Centerline analysis:**
  - Above 0: Short-term volume momentum is stronger than long-term average
  - Below 0: Short-term volume momentum is weaker than long-term average
  - Crossovers indicate shifts in volume momentum

* **Signal line crossovers:**
  - PVO crossing above signal line: Potential bullish volume momentum
  - PVO crossing below signal line: Potential bearish volume momentum
  - Histogram helps visualize the convergence/divergence

* **Divergence patterns:**
  - Bullish: Price makes lower lows while PVO makes higher lows
  - Bearish: Price makes higher highs while PVO makes lower highs
  - Volume divergences often precede price reversals

* **Trend confirmation:**
  - Rising PVO during uptrends confirms volume support
  - Falling PVO during downtrends confirms selling pressure
  - Diverging PVO may signal weakening trends

## Limitations and Considerations

* **Volume dependency:** Effectiveness depends on consistent and reliable volume data
* **Market structure:** More effective in liquid markets with regular volume patterns
* **False signals:** Can generate whipsaws during low-volume or consolidation periods
* **Lag component:** Moving averages introduce some delay in signals
* **Context dependency:** Should be used alongside price analysis and other technical indicators
* **Time horizon:** Different period settings needed for different trading timeframes

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Appel, G. (2005). Technical Analysis: Power Tools for Active Investors. Financial Times Prentice Hall.
* Granville, J. E. (1963). Granville's New Key to Stock Market Profits. Prentice-Hall.
