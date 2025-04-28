# Slope: Linear Regression Trend Measure

[Pine Script Implementation of Slope](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/slope.pine)

## Overview and Purpose

Slope is a statistical measure that quantifies the rate of change of price (or any data series) over a specified period using linear regression. It measures both the direction and steepness of a trend, providing valuable insights into market momentum. The slope directly indicates whether a trend is accelerating, maintaining consistent momentum, or weakening.

This indicator helps traders identify potential trend changes before they become apparent in price action alone. The slope value represents the average change in the source data per bar over the lookback period.

## Core Concepts

* **Trend Direction:** The sign of the slope (positive or negative) reveals the prevailing direction, with positive values indicating uptrends and negative values indicating downtrends.
* **Momentum Measurement:** The magnitude of the slope quantifies trend strength - larger absolute values indicate steeper, stronger trends.
* **Zero Line Crossings:** Transitions from positive to negative slope (or vice versa) can signal potential trend reversals.
* **Divergence Detection:** Discrepancies between price action and slope behavior may indicate weakening trends or impending reversals.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
| :-------- | :------ | :------- | :------------ |
| Period | 14 | Controls the lookback window for calculation | Decrease for faster response in volatile markets, increase for smoother readings in choppy markets |
| Source | Close | Data point used for calculation | Change to High/Low for range analysis, or Volume for volume trend analysis |

**Pro Tip:** Monitor the slope's own slope (rate of change of the slope itself) to identify acceleration or deceleration in trends. Decelerating slope often precedes trend reversals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Slope indicator uses linear regression to fit a straight line to the price data over the specified period. The slope of this line indicates how much the price changes, on average, for each one-bar increase in time.

**Technical formula:**
The slope of a linear regression line is calculated using:

Slope = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)

Where:

* n is the number of data points (period)
* x represents the time index (bar_index)
* y represents the source values (e.g., closing prices)
* Σ denotes summation

> 🔍 **Technical Note:** The Pine Script implementation uses dynamic arrays to store and process the source values and time indices efficiently. The calculation handles incomplete data during warmup periods gracefully by using only available bars until the full period is reached.

## Interpretation Details

The Slope indicator provides clear insights into trend dynamics:

* **Positive Values:** Indicate an uptrend, with larger values showing stronger upward momentum
* **Negative Values:** Indicate a downtrend, with larger negative values showing stronger downward momentum
* **Zero Line:** When the slope approaches zero, it suggests a flat or sideways market
* **Transitions:** Slope changing from steep to flat (while remaining positive/negative) can indicate trend deceleration
* **Divergences:** When price makes new highs but slope fails to follow, it may indicate weakening bullish momentum (and vice versa for bearish divergences)

## Limitations and Considerations

* **Lagging Element:** As with most trend indicators, slope contains inherent lag proportional to the period length
* **Sensitivity to Outliers:** Extreme price movements can disproportionately influence the slope calculation
* **Period Selection:** Too short periods produce noisy signals; too long periods increase lag
* **Market Type Dependency:** Works best in trending markets; generates frequent false signals in ranging markets
* **Complementary Tools:** Should be used alongside other indicators for confirmation, such as momentum oscillators or volume indicators

## References

* Ehlers, J. F. (2001). Rocket Science for Traders: Digital Signal Processing Applications. Wiley Trading.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
