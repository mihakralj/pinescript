# LOESS: Locally Weighted Scatterplot Smoothing

[Pine Script Implementation of LOESS](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/loess.pine)

## Overview and Purpose

Locally Weighted Scatterplot Smoothing (LOESS) is a non-parametric regression method that combines the simplicity of linear regression with the flexibility of non-linear regression. Unlike traditional moving averages that apply uniform weights across a window, LOESS fits a polynomial regression to each point in the series using a weighted subset of nearby data, with weights that decrease with distance. This approach creates an adaptive smoothing effect that follows the local structure of the data while filtering out noise, making it particularly valuable for identifying underlying trends in noisy financial time series.

The implementation provided uses a local linear regression with tricube weighting, providing a robust technique that preserves significant market patterns while removing random fluctuations. By fitting small segments of the data locally rather than trying to find a single global function, LOESS can handle complex, non-linear relationships that might be missed by traditional indicators.

## Core Concepts

* **Local regression:** Fits weighted linear regressions to small neighborhoods around each data point rather than applying a global model
* **Distance-based weighting:** Points closer to the target point receive higher weights, creating a smooth, locally adaptive function
* **Polynomial flexibility:** Uses polynomial functions (typically linear or quadratic) for local fitting, offering greater adaptability to underlying patterns
* **Non-parametric approach:** Makes minimal assumptions about the underlying data distribution, allowing it to capture complex patterns

LOESS stands apart from traditional technical indicators by treating price action as a statistical problem, using local regression to reveal the underlying signal within market noise. This approach is especially useful in financial markets where price movements combine both trend and noise components in ways that often confound simpler moving averages and filters.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 7 | Window size for local regression | Increase for smoother output, decrease for more responsive tracking |
| Source | Close | Price data used for smoothing | Modify to analyze different aspects of price action |

**Pro Tip:** Unlike traditional moving averages where longer periods always produce smoother outputs, LOESS maintains responsiveness even with larger window sizes. Try using a length of 9-15 for medium-term trend analysis, which often provides the optimal balance between noise reduction and signal preservation.

## Calculation and Mathematical Foundation

**Simplified explanation:**
LOESS calculates a smoothed value for each point by fitting a weighted linear regression using neighboring points. Points closer to the target receive higher weights based on a tricube function, which emphasizes nearby data while gradually reducing the influence of more distant points.

**Technical formula:**

For each point i, LOESS calculates:

1. For each point in the window, assign weight w using the tricube function:
   w(x) = (1 - |d|³)³ where d is the normalized distance between points

2. Using these weights, fit a weighted linear regression:
   y = a + bx

3. The smoothed value is the predicted value at the current point

> 🔍 **Technical Note:** The implementation uses an efficient approach that properly handles edge cases and maintains good performance characteristics despite the computational complexity of local regression. The tricube weighting function creates a smooth transition from highly influential nearby points to less influential distant points, avoiding the discontinuities that can occur with simpler weighting schemes.

## Interpretation Details

LOESS provides several analytical perspectives:

* **Trend direction:** The slope of the LOESS line at any point indicates the local trend direction
* **Turning points:** Changes in the LOESS line direction suggest potential reversals in price momentum
* **Smoothness assessment:** The difference between raw price and LOESS indicates market noise level
* **Support/resistance:** LOESS often acts as dynamic support in uptrends and resistance in downtrends
* **Multiple timeframe analysis:** Comparing LOESS across timeframes helps identify conflicting trends
* **Divergence detection:** Divergences between price extremes and LOESS can signal weakness in the current trend

## Limitations and Considerations

* **Computational intensity:** More resource-intensive than simple moving averages
* **End-point sensitivity:** Less reliable at the most recent data points (edge effect)
* **Parameter dependency:** Results can vary significantly based on window size
* **Lag component:** Introduces some lag, especially with larger window sizes
* **Overfitting risk:** Very small window sizes may fit noise rather than underlying trends
* **Sparse data handling:** Requires sufficient data points within the window for reliable regression
* **Non-causal filter:** The standard implementation uses both past and future data; the Pine Script version is adapted to be causal (using only past data)

## References

* Cleveland, W. S. (1979). Robust Locally Weighted Regression and Smoothing Scatterplots. Journal of the American Statistical Association, 74(368), 829-836.
* Cleveland, W. S., & Devlin, S. J. (1988). Locally Weighted Regression: An Approach to Regression Analysis by Local Fitting. Journal of the American Statistical Association, 83(403), 596-610.
* Siegel, A. F. (2016). Practical Business Statistics (7th ed.). Academic Press.
* Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning: Data Mining, Inference, and Prediction. Springer Science & Business Media.
