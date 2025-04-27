# RSE: Relative Squared Error

[Pine Script Implementation of RSE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rse.pine)

## Overview and Purpose

The Relative Squared Error (RSE) is a normalized error metric that provides context to squared errors by comparing them against a naive baseline model. Developed as an extension of traditional error metrics, RSE expresses prediction accuracy as a ratio rather than an absolute value, making it particularly valuable for comparative analysis. By dividing squared prediction errors by the squared errors of a simple baseline (typically using the mean as a constant prediction), RSE offers a clear benchmark for model performance. This allows traders and analysts to determine whether a prediction model or indicator provides genuine value beyond what could be achieved with minimal effort.

## Core Concepts

* **Normalized measurement:** Expresses error relative to a naive baseline model, providing context to raw error values
* **Performance benchmarking:** Creates a natural threshold (1.0) that distinguishes useful from non-useful models
* **Market application:** Particularly effective for comparing prediction models across different financial instruments or timeframes

The core innovation of RSE is its incorporation of a reference model that establishes a minimum performance threshold. Unlike absolute metrics like MSE or RMSE that can be difficult to interpret in isolation, RSE immediately reveals whether a model offers improvement over the simplest possible alternative. A value of 0.5, for instance, indicates the model reduces squared error by 50% compared to simply using the mean as a prediction.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the baseline and error averaging period | Increase for more stable benchmark comparison, decrease for more responsive evaluation |
| Source 1 | close | Actual value signal | Typically the target value you're trying to predict |
| Source 2 | sma(close,20) | Predicted value signal | The indicator or model output being evaluated |

**Pro Tip:** When RSE hovers near 1.0, your model is adding little value beyond using the mean as a prediction. Consider either refining your model or switching to a simpler approach during these periods.

## Calculation and Mathematical Foundation

**Simplified explanation:**
RSE compares how much error your model produces to how much error you'd get by just guessing the average. If your model's errors are half the size of this simple guessing approach, your RSE would be 0.5 - meaning your model is twice as good as the baseline.

**Technical formula:**
RSE = Σ(Y₁ - Y₂)² / Σ(Y₁ - Y̅₁)²

Where:
- Y₁ represents actual values
- Y₂ represents predicted values
- Y̅₁ represents the mean of actual values over the period

> 🔍 **Technical Note:** RSE is closely related to R-squared - in fact, RSE = 1 - R². This means an RSE of 0.25 corresponds to an R² of 0.75, indicating the model explains 75% of the variance.

## Interpretation Details

RSE can be applied in various financial contexts:

* **Model evaluation:** Determine if prediction models offer meaningful improvement over simple alternatives
* **Indicator assessment:** Measure whether technical indicators provide value beyond baseline strategies
* **Strategy validation:** Verify that trading systems outperform naive approaches
* **Market regime identification:** Track when predictive models gain or lose effectiveness
* **Parameter optimization:** Tune model parameters to minimize RSE rather than absolute error

## Limitations and Considerations

* **Baseline dependency:** Performance heavily influenced by the choice of baseline model
* **Instability with low variance:** Can approach infinity when the actual values show little variation
* **Computational overhead:** Requires calculating and tracking both model errors and baseline errors
* **Outlier vulnerability:** Squaring operation makes RSE sensitive to occasional large errors
* **Complementary metrics:** Best used alongside absolute error measures for comprehensive evaluation

## References

* Witten, I.H. and Frank, E. "Data Mining: Practical Machine Learning Tools and Techniques," Morgan Kaufmann, 2005
* Armstrong, J.S. and Collopy, F. "Error Measures for Generalizing About Forecasting Methods," International Journal of Forecasting, 1992
