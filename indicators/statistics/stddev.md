# StdDev: Standard Deviation

[Pine Script Implementation of StdDev](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/stddev.pine)

## Overview and Purpose

Standard Deviation (StdDev) is a statistical measure that quantifies the amount of variation or dispersion in a dataset. In trading, it serves as a fundamental volatility indicator that measures the average distance between each price point and the mean price over a specified period. Higher values indicate greater volatility (prices spread out from the mean), while lower values suggest lower volatility (prices closer to the mean).

## Core Concepts

* **Volatility measurement:** Standard Deviation directly quantifies market volatility by measuring how widely prices are dispersed from their average
* **Market application:** Particularly useful for identifying periods of consolidation versus expansion, helping traders gauge potential breakouts or trend reversals
* **Timeframe suitability:** **Medium to longer timeframes** typically provide more statistically significant readings, though StdDev can be applied across various timeframes depending on the trading strategy

Standard Deviation forms the foundation for numerous other technical indicators including Bollinger Bands, which use standard deviation to place bands around a moving average.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Controls the lookback window for calculation | Decrease for faster response to price changes, increase for smoother readings |
| Source | Close | Data point used for calculation | Change to High/Low for volatility extremes, or HL2/HLC3 for more balanced measurements |

**Pro Tip:** During trending markets, comparing current StdDev values to historical StdDev levels can help identify whether a trend is strengthening (increasing StdDev) or potentially weakening (decreasing StdDev).

## Calculation and Mathematical Foundation

**Simplified explanation:**
Standard Deviation measures how spread out price values are from their average. First, it calculates the average (mean) price over a specified period. Then, it determines how far each price is from that average, squares these differences, averages them, and finally takes the square root of that average.

**Technical formula:**
The formula for Standard Deviation is:

StdDev = √[Σ(x - μ)² / n]

Where:

* x is each individual price
* μ is the mean price over the period
* n is the number of prices in the period
* Σ represents the sum

> 🔍 **Technical Note:** The implementation uses a single-pass algorithm with a circular buffer for efficiency, avoiding the need to recalculate the entire sum for each new bar.

## Interpretation Details

Standard Deviation excels at quantifying volatility objectively. Traders can use StdDev to:

* Identify potential market reversals when volatility spikes
* Recognize consolidation phases when StdDev decreases
* Set more precise stop-loss levels based on current volatility conditions
* Adjust position sizes according to market volatility (smaller positions in higher volatility conditions)

Rising StdDev values often precede significant price movements, while falling values typically indicate diminishing volatility and potential consolidation.

## Limitations and Considerations

* **Market conditions:** Less effective during sideways markets with occasional spikes that can distort readings
* **Lag factor:** Like most indicators based on lookback periods, StdDev has inherent lag
* **False signals:** Sudden news events can cause temporary volatility spikes that may not indicate true trend changes
* **Complementary tools:** Best used alongside trend indicators, volume analysis, or other volatility measures for confirmation

## References

* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill Education.
* Bollinger, J. (2002). Bollinger on Bollinger Bands. McGraw-Hill Education.
