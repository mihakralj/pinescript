# MAE: Mean Absolute Error

[Pine Script Implementation of MAE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mae.pine)

## Overview and Purpose

The Mean Absolute Error (MAE) is a fundamental statistical measure that quantifies the average magnitude of errors between paired observations. As one of the oldest and most intuitive error metrics, MAE has been used in statistical analysis since the early development of the field. In financial analysis, MAE provides traders with a straightforward way to evaluate prediction accuracy, compare indicators, or measure the similarity between different data series. By calculating the average absolute difference between two signals, MAE offers a robust error metric that maintains the same units as the original data and treats all error magnitudes with equal importance.

## Core Concepts

* **Linear error weighting:** Measures the average magnitude of errors without squaring, giving equal importance to all error sizes
* **Outlier robustness:** Less influenced by occasional large errors than squared error metrics, providing a more balanced assessment
* **Market application:** Particularly useful for evaluating prediction models where consistent accuracy is more important than occasional large misses

The distinguishing characteristic of MAE is its linear treatment of errors - by taking absolute differences rather than squares, it weighs all error magnitudes proportionally. This creates a more robust metric that isn't dominated by occasional large errors, making it especially valuable for evaluating models in markets with occasional extreme movements where squared error metrics might be overly influenced by a few outliers.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable error measurement, decrease for more responsive feedback |
| Source 1 | close | First signal for comparison | Typically the actual or target value |
| Source 2 | sma(close,20) | Second signal for comparison | Typically the predicted or modeled value |

**Pro Tip:** When optimizing trading models, compare MAE across different market regimes (trending, ranging, volatile) to ensure consistent performance rather than just low average error that might be skewed by favorable conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MAE simply takes the absolute difference between each pair of values (ignoring whether the error is positive or negative), and then averages these differences. This creates a direct measure of error magnitude in the same units as your original data.

**Technical formula:**
MAE = (1/p) * Σ|Y₁ - Y₂|

Where:
- Y₁, Y₂ are the values being compared
- p is the number of periods

> 🔍 **Technical Note:** Unlike MSE which squares errors, MAE is less sensitive to outliers and provides error measurements in the same units as the original data, making it more directly interpretable in many trading contexts.

## Interpretation Details

MAE can be applied in various financial contexts:

* **Model evaluation:** Compare the accuracy of different predictive models
* **Indicator tuning:** Optimize parameters by minimizing average prediction error
* **Signal comparison:** Measure how closely two indicators or price series track each other
* **System optimization:** Minimize the average deviation between actual and ideal entries/exits
* **Risk assessment:** Quantify the average error magnitude to estimate potential slippage or execution risk

## Limitations and Considerations

* **Scale dependency:** Values depend on the scale of the data, making comparisons across different instruments challenging
* **Gradient challenges:** Non-differentiable at zero, creating potential issues for gradient-based optimization methods
* **Directional blindness:** Does not distinguish between positive and negative errors
* **Subtlety insensitivity:** May not adequately penalize small but systematic errors that could compound over time
* **Complementary metrics:** Best used alongside other error measures like MSE or MAPE for comprehensive evaluation

## References

* Chai, T. and Draxler, R.R. "Root mean square error (RMSE) or mean absolute error (MAE)?", Geoscientific Model Development, 2014
* Willmott, C.J. and Matsuura, K. "Advantages of the mean absolute error (MAE) over the root mean square error (RMSE)", Climate Research, 2005
