# MSE: Mean Squared Error

[Pine Script Implementation of MSE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mse.pine)

## Overview and Purpose

The Mean Squared Error (MSE) is a fundamental statistical measure that quantifies the average squared difference between predicted and actual values. As one of the most widely used error metrics in statistics and machine learning, MSE provides a robust measure of prediction accuracy that emphasizes larger errors. First formally established in statistical theory in the early 20th century, MSE has become a cornerstone of error measurement across multiple disciplines. In financial analysis, MSE offers traders a powerful tool for evaluating prediction models, comparing indicators, and optimizing trading systems, with its squared term making it particularly sensitive to occasional large prediction errors that might have significant financial implications.

## Core Concepts

* **Quadratic error weighting:** Penalizes larger errors more heavily than smaller ones due to the squaring operation
* **Outlier sensitivity:** Responds strongly to occasional large errors, making it useful when large deviations are particularly concerning
* **Market application:** Especially valuable for evaluating prediction models where large errors may have disproportionate financial consequences

The distinguishing characteristic of MSE is its quadratic nature - by squaring errors before averaging, it disproportionately penalizes large deviations compared to small ones. This aligns well with many financial applications where the cost of errors often increases non-linearly with their magnitude, such as in risk management, option pricing, or volatility prediction.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable error measurement, decrease for more responsive feedback |
| Source 1 | close | First signal for comparison | Typically the actual or target value |
| Source 2 | sma(close,20) | Second signal for comparison | Typically the predicted or modeled value |

**Pro Tip:** When optimizing trading models, compare MSE alongside MAE - a much larger MSE relative to MAE indicates your model is making occasional large errors that could significantly impact trading performance.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MSE squares the difference between each pair of values, then averages these squared differences. This squaring step ensures all values are positive and gives much more weight to large errors than to small ones.

**Technical formula:**
MSE = (1/p) * Σ(Y₁ - Y₂)²

Where:
- Y₁, Y₂ are the values being compared
- p is the number of periods

> 🔍 **Technical Note:** MSE has attractive mathematical properties for optimization, including convexity and differentiability. These make it particularly suitable as a loss function in machine learning models where gradient-based optimization is used.

## Interpretation Details

MSE can be applied in various financial contexts:

* **Model evaluation:** Compare the accuracy of different predictive models
* **Indicator tuning:** Optimize parameters by minimizing prediction error
* **Signal comparison:** Measure how closely two indicators track each other
* **System optimization:** Minimize the squared difference between actual and ideal entries/exits
* **Volatility analysis:** Higher MSE in certain market regimes can indicate increased prediction difficulty

## Limitations and Considerations

* **Unit interpretation:** Results are in squared units, making them less directly interpretable than metrics like MAE or RMSE
* **Scale dependency:** Values depend on the scale of the data, making comparisons across different instruments challenging
* **Outlier sensitivity:** Can be disproportionately influenced by a few large errors
* **Directional blindness:** Does not distinguish between positive and negative errors
* **Complementary metrics:** Best used alongside other error measures like MAE or MAPE for comprehensive evaluation

## References

* Chai, T. and Draxler, R.R. "Root mean square error (RMSE) or mean absolute error (MAE)?", Geoscientific Model Development, 2014
* Lehmann, E.L. and Casella, G. "Theory of Point Estimation," Springer, 1998
