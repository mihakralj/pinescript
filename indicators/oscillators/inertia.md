# Inertia: Linear Regression Deviation Oscillator

[Pine Script Implementation of Inertia](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/inertia.pine)

## Overview and Purpose

The Inertia oscillator is a momentum oscillator that measures trend strength by calculating the distance between the current price and its linear regression line over a specified period. Developed as a tool to quantify how far price has deviated from its statistical trend, Inertia provides insights into momentum acceleration, deceleration, and potential reversal points.

Unlike traditional oscillators that compare current price to historical extremes or averages, Inertia uses linear regression to establish a mathematical trend line and measures price deviation from this trend. This approach offers a more statistically rigorous method of assessing momentum, as it considers the overall directional bias of price movement rather than just relative positioning within a range.

## Core Concepts

* **Linear regression baseline:** Uses least squares regression to establish the underlying trend direction over the specified period, providing a mathematically optimal trend line
* **Deviation measurement:** Calculates the distance between current price and the regression line, with positive values indicating price above trend and negative values indicating price below trend
* **Trend strength quantification:** Larger absolute values suggest stronger momentum in the current direction, while values near zero indicate price moving in line with the statistical trend
* **Zero-centered oscillation:** The zero line represents perfect alignment with the regression trend, making directional bias immediately apparent

Inertia's mathematical foundation in linear regression theory makes it particularly effective for identifying when price momentum is strengthening or weakening relative to the established statistical trend, providing early signals of potential trend changes.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Period for linear regression calculation | Lower (10-15) for more sensitive signals in active markets, higher (30-50) for smoother trends in ranging markets |
| Source | Close | Data point used for regression analysis | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** Inertia works exceptionally well for divergence analysis - when price makes new highs but Inertia fails to reach new highs, it often indicates momentum exhaustion and potential trend reversal, as the price is moving further from its statistical trend line.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Inertia calculates a linear regression line through the recent price data, then measures how far the current price sits from this statistically-derived trend line. The regression line represents the "expected" price based on the recent trend, making deviations meaningful indicators of momentum strength.

**Technical formula:**
```
Linear Regression Line: y = mx + b
Where:
m (slope) = (n×Σ(xy) - Σ(x)×Σ(y)) / (n×Σ(x²) - (Σ(x))²)
b (intercept) = (Σ(y) - m×Σ(x)) / n

Regression Value = slope × (length - 1) + intercept
Inertia = Current Price - Regression Value
```

Where:
* n is the length period
* x represents the time index (0 to length-1)
* y represents the price values over the period
* Current Price is the most recent price value
* Regression Value is the expected price based on the trend line

> 🔍 **Technical Note:** The implementation uses the method of least squares to calculate the optimal linear regression line through the price data. The algorithm computes the necessary summations (Σx, Σy, Σxy, Σx²) over the specified period to derive the slope and intercept coefficients. This mathematical approach ensures the regression line minimizes the sum of squared deviations from all data points, providing the most statistically accurate representation of the underlying trend.

## Interpretation Details

Inertia offers several powerful approaches to momentum and trend analysis:

* **Zero-line analysis:** Values above zero indicate price is above the regression trend line (bullish momentum), while values below zero indicate price is below the trend line (bearish momentum)
* **Momentum strength:** Larger absolute values suggest stronger momentum, as price is deviating more significantly from the established statistical trend
* **Trend acceleration:** Increasing absolute values indicate accelerating momentum in the current direction
* **Momentum deceleration:** Decreasing absolute values toward zero suggest momentum is slowing and price is returning to the regression trend
* **Reversal signals:** Crossovers of the zero line can indicate changes in momentum direction relative to the underlying trend
* **Divergence patterns:** When price makes new extremes but Inertia fails to confirm with corresponding extremes, it suggests the trend may be losing statistical validity

The statistical foundation makes Inertia particularly reliable for identifying when price movements are becoming extended relative to the mathematical trend, often preceding corrections or reversals.

## Limitations and Considerations

* **Regression period dependency:** The choice of length period significantly affects the regression line calculation and thus the oscillator's behavior
* **Trending vs. ranging markets:** Most effective in trending markets where linear regression provides meaningful trend representation; less reliable in choppy, sideways conditions
* **Mathematical assumptions:** Assumes price follows a linear trend pattern, which may not hold during periods of acceleration, deceleration, or complex market structures
* **Lag characteristics:** Linear regression inherently includes some lag as it considers historical data to establish the trend line
* **Extreme value sensitivity:** Outlier price movements within the regression period can skew the trend line calculation
* **Complementary analysis:** Most effective when combined with trend indicators or volume studies to confirm the direction and strength of the underlying trend

## References

* Hamilton, J. D. (1994). *Time Series Analysis*. Princeton University Press.
* Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.