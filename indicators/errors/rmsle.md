# RMSLE: Root Mean Squared Logarithmic Error

[Pine Script Implementation of RMSLE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rmsle.pine)

## Overview and Purpose

The Root Mean Squared Logarithmic Error (RMSLE) is a specialized error metric that measures the ratio error between predicted and actual values rather than their absolute difference. By calculating the square root of the mean squared difference between logarithms, RMSLE effectively measures error in terms of proportional differences. This approach makes it particularly valuable for financial data with exponential growth patterns or when percentage errors are more relevant than absolute errors. RMSLE provides traders with a tool to evaluate prediction models that focuses on relative performance rather than absolute magnitude, especially useful when large values might otherwise dominate error calculations.

## Core Concepts

* **Proportional error focus:** Measures relative differences between values rather than absolute magnitudes
* **Penalty asymmetry:** Penalizes underestimation more heavily than overestimation, reflecting the often greater cost of under-prediction in financial contexts
* **Market application:** Particularly valuable for evaluating predictions of rapidly growing metrics or when percentage accuracy is more important than absolute accuracy

The core principle of RMSLE is its logarithmic transformation, which effectively converts absolute differences into relative ones. By comparing the logs of values rather than the values themselves, RMSLE treats a prediction that's off by a factor of 2 the same whether the actual value is 10 or 1000. This creates a more appropriate error metric for many financial applications where relative performance often matters more than absolute differences.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable error assessment, decrease for more responsive feedback |
| Source 1 | close | First signal (typically actual values) | The target or reference values being compared |
| Source 2 | sma(close,20) | Second signal (typically predictions) | The output of your model or the comparison signal |

**Pro Tip:** RMSLE works best with strictly positive data - if your signals include values approaching zero, consider adding a small offset before applying RMSLE to avoid instability in the logarithmic calculations.

## Calculation and Mathematical Foundation

**Simplified explanation:**
RMSLE transforms your data using logarithms before calculating the error, which effectively changes absolute differences into relative ones. This makes it care more about percentage differences than absolute magnitude, so being off by 10% is treated the same whether you're predicting small or large values.

**Technical formula:**
RMSLE = √[(1/p) * Σ(log(1 + Y₁) - log(1 + Y₂))²]

Where:
- Y₁, Y₂ are the values being compared
- p is the number of periods
- log is the natural logarithm

> 🔍 **Technical Note:** Adding 1 before taking the logarithm (log(1+Y) rather than log(Y)) allows RMSLE to handle zero values and reduces the penalty for small values, while still maintaining the desired proportional error property for larger values.

## Interpretation Details

RMSLE can be applied in various financial contexts:

* **Growth prediction:** Evaluate models forecasting exponentially growing metrics
* **Percentage accuracy:** Focus on proportional accuracy rather than absolute error magnitude
* **Volatility forecasting:** Assess prediction models where percentage errors matter more than point errors
* **Scale-free comparison:** Compare prediction accuracy across different instruments regardless of price
* **Risk assessment:** Penalize underestimation more heavily than overestimation when it carries greater risk

## Limitations and Considerations

* **Interpretation difficulty:** Less intuitive than direct error metrics as it measures error in log space
* **Asymmetric penalties:** Penalizes underprediction more heavily than overprediction of the same magnitude
* **Computational complexity:** More intensive calculation due to logarithm and square root operations
* **Positive data requirement:** Works best with strictly positive data; requires special handling for zero values
* **Complementary metrics:** Best used alongside other error measures for comprehensive evaluation

## References

* Chai, T. and Draxler, R.R. "Root mean square error (RMSE) or mean absolute error (MAE)?", Geoscientific Model Development, 2014
* Willmott, C.J. and Matsuura, K. "Advantages of the mean absolute error (MAE) over the root mean square error (RMSE)", Climate Research, 2005
