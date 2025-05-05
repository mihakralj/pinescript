# Var: Variance

[Pine Script Implementation of Var](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/variance.pine)

## Overview and Purpose

Variance is a fundamental statistical measure that quantifies the dispersion or spread of a data set from its mean (average). In trading and technical analysis, Variance serves as a volatility indicator that measures the average squared deviation of each price point from the mean price over a specified period. Higher variance values indicate greater market volatility (wider price dispersion), while lower values suggest lower volatility (prices clustering closer to the mean).

## Core Concepts

* **Volatility measurement:** Variance provides a raw measure of market volatility by calculating the squared average distance of prices from their mean
* **Market application:** Useful for identifying periods of extreme price movement versus consolidation, helping traders assess potential breakouts or reversals
* **Timeframe suitability:** **Medium to longer timeframes** typically provide more statistically meaningful readings, though Variance can be applied across various timeframes based on strategy requirements

Variance forms the mathematical foundation for other important statistical measures in trading, most notably Standard Deviation (which is simply the square root of Variance).

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Controls the lookback window for calculation | Decrease for more sensitivity to recent price changes, increase for more stable readings over time |
| Source | Close | Data point used for calculation | Change to High/Low for volatility extremes, or HL2/HLC3 for more balanced measurements |

**Pro Tip:** When comparing different markets or instruments, Variance can help identify which ones are experiencing higher volatility, potentially offering better trading opportunities or requiring adjusted position sizing.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Variance measures how spread out price values are from their average by taking the squared differences. It first calculates the average (mean) price over a specified period. Then it determines how far each price is from that average, squares these differences, and finally averages these squared differences.

**Technical formula:**
The formula for Variance is:

Variance = Σ(x - μ)² / n

Where:

* x is each individual price
* μ is the mean price over the period
* n is the number of prices in the period
* Σ represents the sum

> 🔍 **Technical Note:** The implementation uses a single-pass algorithm with a circular buffer for efficiency, avoiding the need to recalculate the entire sum for each new bar. This optimization is particularly important for variance calculation with longer lookback periods.

## Interpretation Details

Variance provides valuable insights into market behavior that traders can use to:

* Assess current market volatility compared to historical levels
* Identify potential turning points when variance spikes significantly
* Recognize consolidation phases when variance decreases over time
* Adjust position sizing according to market volatility (smaller positions during high variance periods)
* Set more informed stop-loss levels based on the current market's statistical behavior

Unlike Standard Deviation, Variance uses squared values, which means it gives more weight to outliers and extreme price movements. This can make it particularly useful for detecting exceptional market conditions.

## Limitations and Considerations

* **Market conditions:** Less reliable during rapidly changing market regimes or during transitions between trending and ranging conditions
* **Lag factor:** As a lookback-based indicator, Variance has inherent lag that increases with longer period settings
* **Scale sensitivity:** Unlike Standard Deviation, Variance is not expressed in the same units as the original data, making direct interpretations less intuitive
* **Complementary tools:** Best used alongside trend indicators, price action analysis, or other volatility measures like ATR for a complete market assessment
