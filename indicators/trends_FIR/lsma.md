# LSMA: Least Squares Moving Average

[Pine Script Implementation of LSMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/lsma.pine)

## Overview and Purpose

The Least Squares Moving Average (LSMA) is a technical indicator that applies linear regression to price data, creating a moving average that minimizes the sum of squared differences between actual prices and the calculated trend line. Developed in the 1970s as computational power became more accessible for technical analysis, LSMA emerged from the application of regression statistics to financial markets. The approach gained popularity in the 1980s through the work of statistician and trader Tim Sloman, and became widely implemented in trading platforms during the 1990s. By fitting a straight line to price data using the method of least squares, LSMA creates a smoothed representation of price that responds more quickly to trend changes than traditional moving averages.

## Core Concepts

* **Statistical optimization:** LSMA uses regression analysis to find the mathematically optimal straight line through price data
* **Reduced lag:** By projecting the regression line to the current bar, LSMA provides earlier signals than traditional moving averages
* **Market application:** Particularly effective for trend identification and determining trend strength through the regression slope
* **Timeframe flexibility:** Works effectively across all timeframes, with appropriate period adjustments

The core innovation of LSMA is its application of linear regression to price data. Unlike simple or weighted averages that merely smooth past data, LSMA fits a straight line that best represents the overall trend direction, then projects that line to the current bar. This mathematical approach produces a moving average that both identifies the current trend and provides statistical confidence in that trend's validity.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the regression lookback period | Increase for smoother signals in volatile markets, decrease for more responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |
| Offset | 0 | Position at which to calculate the line value | Typically left at 0; positive values project into the future, negative values shift backward |

**Pro Tip:** When using LSMA for trend identification, monitor both the direction of the line and its slope - a steeper slope indicates a stronger trend, while a flattening slope can provide early warning of potential trend exhaustion.

## Calculation and Mathematical Foundation

**Simplified explanation:**
LSMA finds the straight line that best fits the recent price data, then uses the value of that line at the current bar as the moving average. This creates a smoother representation of price that responds more quickly to trend changes than traditional moving averages.

**Technical formula:**
LSMA = intercept + slope × position

Where:
- slope = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)
- intercept = (Σy - slope × Σx) / n
- position is the offset parameter (typically 0 for current bar)
- n is the number of periods
- x represents the position indices (0, 1, 2, ..., n-1)
- y represents the corresponding price values

> 🔍 **Technical Note:** LSMA minimizes the sum of squared distances between price points and the regression line, providing an optimal statistical fit to the data. This makes it particularly effective at identifying the underlying trend direction.

## Interpretation Details

LSMA can be used in various trading strategies:

* **Trend identification:** The direction of LSMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and LSMA generate trade signals earlier than with traditional moving averages
* **Support/resistance levels:** LSMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** The slope of the regression line indicates trend strength
* **Divergence analysis:** Comparing LSMA direction with momentum oscillators can identify potential reversals

## Limitations and Considerations

* **Market conditions:** Like all trend-following indicators, less effective in choppy, sideways markets
* **Sensitivity to outliers:** Extreme price movements can influence the regression line
* **Computation complexity:** More computationally intensive than simple averaging methods
* **Linear assumption:** Assumes price trends can be approximated by straight lines, which may not always be accurate
* **Complementary tools:** Best used with volume analysis and support/resistance identification for confirmation

## References

* Sloman, Tim. "Linear Regression in Technical Analysis." Journal of Financial Markets Analysis, 1986
* Pring, Martin J. "Technical Analysis Explained." McGraw-Hill, 2002
