# RMSE: Root Mean Squared Error

[Pine Script Implementation of RMSE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rmse.pine)

## Overview and Purpose

The Root Mean Squared Error (RMSE) is a standard statistical measure that quantifies the average magnitude of prediction errors. By taking the square root of the mean squared difference between predicted and actual values, RMSE provides a metric in the same units as the original data, making it intuitive to interpret. First widely adopted in statistical analysis in the early 20th century, RMSE has become a cornerstone of model evaluation across numerous fields including finance. It is particularly valued in financial forecasting for its sensitivity to large errors, which can be critical when evaluating models where occasional large misses may have significant implications for trading performance.

## Core Concepts

* **Error magnitude focus:** Measures the average size of errors without considering direction, providing a single value that summarizes prediction accuracy
* **Outlier sensitivity:** Penalizes large errors more heavily than small ones due to the squaring operation, making it particularly responsive to significant mispredictions
* **Market application:** Especially useful for evaluating prediction models where large errors are more concerning than small ones, such as in risk management or volatility forecasting

The distinguishing characteristic of RMSE is its quadratic scoring rule - by squaring errors before averaging, then taking the square root, it gives relatively high weight to large errors. This property aligns well with many financial applications where the cost of errors increases more than linearly with their size.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable error measurement, decrease for more responsive tracking |
| Source 1 | close | First signal for comparison | Typically the actual or target value |
| Source 2 | sma(close,20) | Second signal for comparison | Typically the predicted or modeled value |

**Pro Tip:** When optimizing prediction models, consider using multiple error metrics alongside RMSE - if your MAE is significantly lower than your RMSE, it indicates your model occasionally makes very large errors despite being generally accurate.

## Calculation and Mathematical Foundation

**Simplified explanation:**
RMSE squares the difference between predicted and actual values, averages these squared differences, then takes the square root to return to the original data's units. This process emphasizes larger errors more than smaller ones.

**Technical formula:**
RMSE = √[(1/p) * Σ(Y₁ - Y₂)²]

Where:
- Y₁, Y₂ are the two signals being compared
- p is the number of periods

> 🔍 **Technical Note:** The square root step in RMSE calculation is what differentiates it from MSE and brings the metric back to the original units, making it more interpretable than MSE which is in squared units.

## Interpretation Details

RMSE can be applied in various financial contexts:

* **Model selection:** Compare the accuracy of different predictive models
* **Parameter optimization:** Tune indicator parameters to minimize prediction error
* **Signal comparison:** Quantify how closely two indicators or signals track each other
* **Volatility measurement:** Assess prediction difficulty across different market regimes
* **System evaluation:** Evaluate the accuracy of trading system signals relative to ideal entries/exits

## Limitations and Considerations

* **Outlier sensitivity:** Can be disproportionately influenced by a few large errors
* **Scale dependency:** Values depend on the scale of the data, making comparisons across different instruments challenging
* **Directional blindness:** Does not distinguish between positive and negative errors
* **Statistical assumptions:** Optimal under the assumption that errors follow a normal distribution
* **Complementary metrics:** Best used alongside MAE or MAPE for a more comprehensive error assessment

## References

* Chai, T. and Draxler, R.R. "Root mean square error (RMSE) or mean absolute error (MAE)?", Geoscientific Model Development, 2014
* Willmott, C.J. and Matsuura, K. "Advantages of the mean absolute error (MAE) over the root mean square error (RMSE)", Climate Research, 2005
