# MAPE: Mean Absolute Percentage Error

[Pine Script Implementation of MAPE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mape.pine)

## Overview and Purpose

The Mean Absolute Percentage Error (MAPE) is a widely used statistical measure that expresses forecast accuracy as a percentage. Established in forecasting literature since the 1950s, MAPE has become a standard tool for evaluating prediction models across numerous fields including finance. By expressing errors as percentages of the actual values, MAPE provides a scale-independent metric that facilitates comparison across different data ranges. This makes it particularly valuable for financial analysts and traders who need to evaluate prediction accuracy across different instruments with widely varying price levels or when comparing performance across timeframes.

## Core Concepts

* **Relative error measurement:** Expresses errors as percentages rather than absolute values, creating a scale-independent metric
* **Intuitive interpretation:** Provides results in easily understood percentage terms that directly indicate prediction accuracy
* **Market application:** Particularly useful for comparing forecast accuracy across different securities with different price ranges

The core principle of MAPE is its focus on relative rather than absolute error. By expressing each error as a percentage of the actual value, MAPE creates a normalized metric that allows direct comparison regardless of the underlying scale. This is especially valuable in financial markets where assets trade at vastly different price levels but where similar percentage movements might have equal significance.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable error assessment, decrease for more responsive tracking |
| Source 1 | close | Actual value signal | Typically the target value you're trying to predict |
| Source 2 | sma(close,20) | Predicted value signal | The output of your forecasting model or indicator |

**Pro Tip:** When using MAPE to evaluate trading models, be cautious during periods when price approaches zero or during extreme volatility - these conditions can cause MAPE to produce misleadingly large values that don't necessarily reflect poor model performance.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MAPE calculates how large your prediction errors are compared to the actual values themselves. If your prediction is off by $1 on a $100 stock, that's a 1% error, but the same $1 error on a $10 stock would be a 10% error.

**Technical formula:**
MAPE = (100/p) * Σ|Y₁ - Y₂|/Y₁

Where:
- Y₁ is the actual value
- Y₂ is the predicted value
- p is the number of periods

> 🔍 **Technical Note:** MAPE weighs negative errors (underpredictions) more heavily than positive errors (overpredictions) of the same magnitude. For example, an actual value of 100 with a prediction of 50 gives a 50% error, while a prediction of 150 gives a 33.3% error.

## Interpretation Details

MAPE can be applied in various financial contexts:

* **Model evaluation:** Compare the accuracy of different forecasting approaches
* **Cross-market analysis:** Assess prediction performance across different instruments regardless of price
* **Indicator tuning:** Optimize indicator parameters to minimize percentage errors
* **Trading system assessment:** Evaluate how closely system signals track ideal entry/exit points
* **Performance tracking:** Monitor how prediction accuracy changes across different market regimes

## Limitations and Considerations

* **Zero handling:** Undefined when actual values are zero, requiring special handling
* **Asymmetric penalties:** Penalizes underprediction more heavily than overprediction
* **Small value bias:** Extremely sensitive when actual values approach zero
* **Infinite errors:** Can produce extremely large or infinite values with small denominators
* **Complementary metrics:** Best used alongside absolute error measures like MAE or RMSE

## References

* Hyndman, R.J. and Koehler, A.B. "Another look at measures of forecast accuracy," International Journal of Forecasting, 2006
* Makridakis, S. "Accuracy measures: theoretical and practical concerns," International Journal of Forecasting, 1993
