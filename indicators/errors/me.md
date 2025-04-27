# ME: Mean Error

[Pine Script Implementation of ME](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/me.pine)

## Overview and Purpose

The Mean Error (ME) is a fundamental statistical measure that calculates the average difference between two data series, preserving the sign of each difference. Unlike error metrics that focus on magnitude alone, ME specifically measures directional bias in predictions or indicators. This makes it particularly valuable for detecting systematic over-prediction or under-prediction in financial models and technical indicators. While simple in calculation, ME provides critical information about directional bias that more complex error metrics often obscure, helping traders identify and correct systematic tendencies in their forecasting approaches.

## Core Concepts

* **Bias detection:** Reveals systematic tendencies to over-predict or under-predict by preserving error direction
* **Directional sensitivity:** Distinguishes between positive and negative errors, with positive values indicating under-prediction and negative values indicating over-prediction
* **Market application:** Particularly useful for identifying and correcting bias in trading systems and forecasting models

The core principle of ME is its preservation of error direction. By allowing positive and negative errors to cancel each other out, ME creates a measure of systematic bias rather than overall accuracy. A value near zero might indicate either high accuracy or balanced errors, but significant non-zero values reveal a consistent directional bias that may require correction even when other error metrics appear acceptable.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the window for error averaging | Increase for more stable bias assessment, decrease for detecting shifting bias patterns |
| Source 1 | close | First signal for comparison | Typically the actual or target value |
| Source 2 | sma(close,20) | Second signal for comparison | Typically the predicted or model value |

**Pro Tip:** When ME persists significantly above or below zero across different market conditions, this indicates a systemic bias in your model that should be addressed, even if other error metrics like MAE or RMSE appear acceptable.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ME simply calculates the average difference between predicted and actual values, keeping the positive and negative signs intact. If predictions are consistently too high, ME will be negative; if they're consistently too low, ME will be positive.

**Technical formula:**
ME = (1/p) * Σ(Y₁ - Y₂)

Where:
- Y₁, Y₂ are the values being compared
- p is the number of periods

> 🔍 **Technical Note:** While a ME of zero might seem ideal, it can mask large offsetting errors. Always examine ME alongside magnitude-based metrics like MAE or RMSE to get a complete picture of prediction performance.

## Interpretation Details

ME can be applied in various financial contexts:

* **Bias identification:** Detect systematic tendencies to over-predict or under-predict
* **Model calibration:** Adjust forecasting models to correct for consistent bias
* **Indicator optimization:** Fine-tune technical indicators to reduce directional bias
* **Trend confirmation:** Assess whether prediction errors show a pattern related to market direction
* **System evaluation:** Determine if trading systems have directional bias that could be exploited

## Limitations and Considerations

* **Error cancellation:** Positive and negative errors can offset each other, potentially masking large errors
* **Scale dependency:** Values depend on the scale of the data, making comparisons across different instruments challenging
* **Incomplete assessment:** Does not measure error magnitude, only directional bias
* **Outlier vulnerability:** Can be heavily influenced by extreme values
* **Complementary metrics:** Should always be used alongside magnitude-based error measures like MAE or RMSE

## References

* Makridakis, S. "Accuracy measures: theoretical and practical concerns," International Journal of Forecasting, 1993
* Armstrong, J.S. "Evaluating forecasting methods," in Principles of Forecasting: A Handbook for Researchers and Practitioners, 2001
