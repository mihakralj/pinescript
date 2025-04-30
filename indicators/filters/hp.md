# HP: Hodrick-Prescott Filter

[Pine Script Implementation of HP](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/hp.pine)

## Overview and Purpose

The Hodrick-Prescott Filter (HP) is a mathematical tool for time series decomposition that separates a time series into trend and cyclical components. Originally developed for analyzing business cycles in macroeconomics, the HP filter has become a valuable tool in technical analysis for identifying underlying trends while filtering out short-term price fluctuations. Unlike moving averages that simply smooth price data, the HP filter optimally balances the trade-off between trend smoothness and fidelity to the original data.

The implementation provided is a causal approximation of the standard HP filter, making it suitable for real-time trading applications. By using an optimized algorithm based on state-space representation, this version eliminates the look-ahead bias present in standard HP implementations while maintaining computational efficiency. The filter provides both the trend component (showing the long-term direction) and the cycle component (highlighting deviation from trend), offering traders comprehensive insights into price structure.

## Core Concepts

* **Decomposition approach:** Separates price into trend and cycle components rather than simply smoothing the data
* **Smoothing parameter:** Controlled by lambda, which determines the balance between smoothness and fit
* **Optimization framework:** Uses mathematical optimization to find the best trend component
* **Causal implementation:** Modified algorithm eliminates look-ahead bias while preserving essential filter properties

The HP filter stands apart from traditional technical indicators by approaching trend extraction as an optimization problem, finding the trend component that best balances two competing objectives: minimizing the deviation between the trend and the original data, and minimizing the curvature of the trend itself. This approach results in a more nuanced view of market structure than what standard moving averages can provide.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Lambda | 677 | Controls smoothness (higher = smoother trend) | Increase during volatile markets for clearer trend, decrease for more responsive tracking |
| Source | Close | Price data used for filtering | Rarely needs adjustment; can change to examine trends in other data series |

**Pro Tip:** The optimal lambda value depends on the data frequency. A good starting point is to use the square of the data frequency multiplied by 100. For daily data, try values around 1,600-6,400. For intraday charts, lower values around 100-900 are typically more appropriate.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The HP filter finds the trend component by minimizing a weighted sum of two terms: (1) the sum of squared deviations between the original series and the trend, and (2) the sum of squared second differences of the trend (measuring its curvature). The weight between these objectives is determined by lambda.

**Technical formula:**

The standard HP filter solves the following minimization problem:

min(∑(yₜ - τₜ)² + λ∑[(τₜ₊₁ - τₜ) - (τₜ - τₜ₋₁)]²)
  τ

Where:
- yₜ is the observed data (price)
- τₜ is the trend component
- λ is the smoothing parameter

The causal approximation implemented in Pine Script uses a state-space representation with an alpha parameter:

alpha = (√λ × 0.5 - 1.0) / (√λ × 0.5 + 1.0)

> 🔍 **Technical Note:** The implementation uses a recursive algorithm that processes data points sequentially, making it suitable for real-time applications. The alpha parameter is derived from lambda to approximate the filtering characteristics of the original HP filter while maintaining causality. The cycle component is calculated simply as the difference between the original price and the trend component.

## Interpretation Details

The HP filter provides several analytical perspectives:

* **Trend component analysis:**
  * Direction: Upward/downward sloping indicates the primary market direction
  * Slope changes: Potential shifts in the underlying trend strength
  * Curvature: Acceleration or deceleration in price momentum

* **Cycle component analysis:**
  * Zero line crossovers: Potential shift in short-term momentum
  * Amplitude: Larger cycles suggest higher volatility or strong price reactions
  * Narrowing cycles: Potential consolidation or decreasing volatility
  * Divergences: When price makes new highs/lows but cycles don't confirm

* **Combined analysis:**
  * Price above/below trend: Overbought/oversold conditions
  * Cycle extremes: Potential reversal zones when cycle reaches historical extremes
  * Cyclical patterns: Identifying recurring market behaviors

## Limitations and Considerations

* **End-point sensitivity:** Although mitigated in the causal version, still somewhat less reliable on recent data
* **Lambda selection:** Results highly dependent on lambda; no single "correct" value
* **Time series assumptions:** Works best on continuous, relatively stable time series
* **Complementary tool:** Most effective when combined with other forms of analysis
* **Non-stationary data challenges:** May struggle with highly non-stationary financial data
* **Causal approximation tradeoffs:** Some sacrifices in optimality for real-time applicability
* **Warm-up period:** Requires several bars to converge to optimal filtering behavior

## References

* Hodrick, R. J., & Prescott, E. C. (1997). Postwar U.S. Business Cycles: An Empirical Investigation. Journal of Money, Credit and Banking, 29(1), 1-16.
* Baxter, M., & King, R. G. (1999). Measuring Business Cycles: Approximate Band-Pass Filters for Economic Time Series. Review of Economics and Statistics, 81(4), 575-593.
* Phillips, P. C. B., & Jin, S. (2021). Business Cycles, Trend Elimination, and the HP Filter. International Economic Review, 62(2), 469-520.
* Ehlers, J. F. (2013). Cycle Analytics for Traders. John Wiley & Sons.
