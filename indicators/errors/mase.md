# MASE: Mean Absolute Scaled Error

[Pine Script Implementation of MASE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mase.pine)

## Overview and Purpose

The Mean Absolute Scaled Error (MASE) is an advanced error metric that provides a scale-independent measure of forecast accuracy. Introduced by Rob Hyndman and Anne Koehler in 2006, MASE addresses limitations in traditional error metrics by scaling errors relative to a naive forecast benchmark. This creates a unitless measure that allows direct comparison across different time series and market conditions. For financial analysts and traders, MASE offers a robust way to evaluate prediction models regardless of price scale or volatility, providing clear insight into whether a forecasting method outperforms a simple naive approach.

## Core Concepts

* **Relative performance:** Measures prediction accuracy relative to a naive benchmark rather than in absolute terms
* **Scale independence:** Creates a unitless metric that allows fair comparison across different instruments and timeframes
* **Market application:** Particularly valuable for comparing forecast models across different securities where price scales and volatilities vary significantly

The core innovation of MASE is its normalization approach - by scaling the absolute error relative to the error of a naive forecast (typically a random walk), it creates a natural benchmark where values below 1.0 indicate the model outperforms the naive approach. This gives MASE a built-in interpretability that many other error metrics lack.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the window for error averaging | Increase for more stable benchmark comparison, decrease for more responsive evaluation |
| Source 1 | close | First signal (actual values) | Typically the target series you're trying to predict |
| Source 2 | sma(close,20) | Second signal (predictions) | The output of your forecasting model or indicator |

**Pro Tip:** When evaluating trading models, pay special attention to how MASE behaves during market regime changes - a model that maintains MASE < 1 across different volatility conditions demonstrates robust predictive power.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MASE compares your model's average error to the error you'd get from a very simple forecasting approach (just guessing that tomorrow's value will be the same as today's). If your model produces smaller errors than this simple approach, MASE will be less than 1.0.

**Technical formula:**
MASE = MAE(forecast) / MAE(naive)

Where:
- MAE(forecast) = Average of |Actual - Predicted|
- MAE(naive) = Average of |Actual - Previous Actual|

Implemented as: MASE₍ₙ₎ = SMA(|Y₁₍ₙ₎ - Y₂₍ₙ₎|, p) / SMA(|Y₁₍ₙ₎ - Y₁₍ₙ₋₁₎|, p)

> 🔍 **Technical Note:** The naive forecast used in MASE is essentially a random walk model. For financial time series that often exhibit near-random walk behavior, this creates a particularly challenging benchmark that many sophisticated models struggle to beat consistently.

## Interpretation Details

MASE can be applied in various financial contexts:

* **Model evaluation:** Compare the relative accuracy of different forecasting models
* **Strategy validation:** Determine if a trading strategy's signals outperform naive approaches
* **Cross-market analysis:** Compare prediction accuracy across different instruments regardless of price scale
* **Market regime detection:** Identify periods where predictability increases or decreases
* **Parameter optimization:** Tune model parameters to minimize MASE rather than absolute errors

## Limitations and Considerations

* **Benchmark dependency:** Performance assessment is relative to the naive forecast benchmark
* **Calculation complexity:** More involved computation than simple error metrics
* **Interpretation nuance:** Values around 1.0 require careful interpretation
* **Historical data requirement:** Needs prior period data to calculate the benchmark error
* **Complementary metrics:** Best used alongside absolute error measures for comprehensive evaluation

## References

* Hyndman, R.J. and Koehler, A.B. "Another look at measures of forecast accuracy," International Journal of Forecasting, 2006
* Hyndman, R.J. "Why every statistician should know about cross-validation," Hyndsight blog, 2010
