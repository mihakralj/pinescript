# MSLE: Mean Squared Logarithmic Error

[Pine Script Implementation of MSLE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/msle.pine)

## Overview and Purpose

The Mean Squared Logarithmic Error (MSLE) is a specialized error metric that measures differences between predicted and actual values in logarithmic space. By calculating the squared difference between logarithms rather than raw values, MSLE effectively emphasizes relative errors over absolute ones. This approach makes it particularly valuable for financial data with exponential growth patterns or when percentage differences are more significant than absolute differences. For traders and analysts, MSLE provides a way to evaluate models where proportional accuracy matters more than absolute precision, especially useful when working with rapidly growing metrics or when small values deserve similar attention to large ones.

## Core Concepts

* **Proportional accuracy focus:** Measures relative differences between values rather than absolute errors
* **Logarithmic transformation:** Compresses large values and expands smaller ones, giving more balanced attention across different scales
* **Market application:** Particularly valuable for evaluating predictions of metrics with exponential growth or when percentage accuracy is more important than absolute precision

The core innovation of MSLE is its logarithmic transformation, which effectively converts absolute differences into relative ones. By working in logarithmic space, a prediction that's off by a factor of 2 produces the same error whether the actual value is 10 or 1000. This creates a more appropriate error metric for many financial applications where relative performance often matters more than absolute differences.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable error evaluation, decrease for more responsive tracking |
| Source 1 | close | First signal (typically actual values) | The target or reference values being compared |
| Source 2 | sma(close,20) | Second signal (typically predictions) | The output of your model or the comparison signal |

**Pro Tip:** When evaluating models for percentage-based trading decisions, MSLE often provides more relevant error assessment than standard MSE - a low MSLE suggests your model captures relative movements effectively even if absolute errors seem large.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MSLE transforms your data using logarithms before calculating the squared error, which effectively changes absolute differences into relative ones. This makes it care more about percentage differences than absolute magnitude, so being off by 10% is treated the same whether you're predicting small or large values.

**Technical formula:**
MSLE = (1/p) * Σ(log(1 + Y₁) - log(1 + Y₂))²

Where:
- Y₁, Y₂ are the values being compared
- p is the number of periods
- log is the natural logarithm

> 🔍 **Technical Note:** Adding 1 before taking the logarithm (log(1+Y) rather than log(Y)) serves two purposes: it allows MSLE to handle zero values, and it reduces the penalty for errors on very small values while maintaining the desired proportional error property for larger values.

## Interpretation Details

MSLE can be applied in various financial contexts:

* **Growth prediction:** Evaluate models forecasting metrics with exponential growth patterns
* **Small value importance:** Ensure models pay attention to smaller values rather than focusing only on large ones
* **Percentage accuracy:** Focus on proportional accuracy rather than absolute error magnitude
* **Scale-free comparison:** Compare prediction accuracy across different instruments regardless of price scale
* **Risk assessment:** Penalize underestimation more heavily than overestimation when it carries greater risk

## Limitations and Considerations

* **Interpretation difficulty:** Less intuitive than direct error metrics as it measures error in log space
* **Asymmetric penalties:** Penalizes underprediction more heavily than overprediction of the same magnitude
* **Computational overhead:** More intensive calculation due to logarithm operations
* **Positive data requirement:** Works best with strictly positive data; requires adjustment for zero values
* **Complementary metrics:** Best used alongside other error measures for comprehensive evaluation

## References

* Chai, T. and Draxler, R.R. "Root mean square error (RMSE) or mean absolute error (MAE)?", Geoscientific Model Development, 2014
* Hyndman, R.J. and Koehler, A.B. "Another look at measures of forecast accuracy," International Journal of Forecasting, 2006
