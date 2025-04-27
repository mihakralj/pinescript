# MPE: Mean Percentage Error

[Pine Script Implementation of MPE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mpe.pine)

## Overview and Purpose

The Mean Percentage Error (MPE) is a directional error metric that measures the average percentage difference between predicted and actual values, preserving the sign of each error. Unlike MAPE which focuses on error magnitude, MPE specifically measures systematic bias in forecasts by allowing positive and negative errors to offset each other. This makes it particularly valuable for detecting whether prediction models or trading indicators consistently over-predict or under-predict. By producing a signed percentage value, MPE helps traders identify and correct systematic bias in their forecasting approaches, even when other error metrics might suggest acceptable overall performance.

## Core Concepts

* **Directional bias detection:** Reveals systematic tendencies to over-predict or under-predict by preserving error direction
* **Scale-independent measurement:** Expresses bias in percentage terms, allowing comparison across different price scales
* **Market application:** Particularly useful for identifying and correcting systematic bias in trading systems and forecasting models

The core principle of MPE is its preservation of error direction while expressing errors in percentage terms. By allowing positive and negative percentage errors to cancel each other out, MPE creates a measure of systematic bias rather than overall accuracy. A value near zero might indicate either high accuracy or balanced errors, but significant non-zero values reveal a consistent directional bias that requires correction.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable bias assessment, decrease for detecting shifting bias patterns |
| Source 1 | close | Actual value signal | Typically the target value you're trying to predict |
| Source 2 | sma(close,20) | Predicted value signal | The output of your forecasting model or indicator |

**Pro Tip:** When MPE consistently shows the same sign (positive or negative) across different market conditions, this indicates a systemic bias in your model that should be addressed - positive MPE indicates consistent under-prediction, while negative MPE indicates over-prediction.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MPE calculates the percentage difference between predicted and actual values, keeping the positive and negative signs intact, then averages these percentages. If predictions are consistently too high, MPE will be negative; if they're consistently too low, MPE will be positive.

**Technical formula:**
MPE = (100/p) * Σ(Y₁ - Y₂)/Y₁

Where:
- Y₁ is the actual value
- Y₂ is the predicted value
- p is the number of periods

> 🔍 **Technical Note:** While MPE of zero might seem ideal, it can mask large offsetting errors. Always examine MPE alongside magnitude-based metrics like MAPE to get a complete picture of forecast performance.

## Interpretation Details

MPE can be applied in various financial contexts:

* **Bias identification:** Detect systematic tendencies to over-predict or under-predict
* **Model calibration:** Adjust forecasting models to correct for consistent bias
* **Indicator optimization:** Fine-tune technical indicators to reduce directional bias
* **Trend-specific analysis:** Determine if prediction bias changes during up vs. down trends
* **Strategy evaluation:** Assess whether trading systems have directional bias that could be exploited

## Limitations and Considerations

* **Error cancellation:** Positive and negative errors can offset each other, potentially masking large errors
* **Zero handling:** Undefined when actual values are zero, requiring special handling
* **Small value sensitivity:** Extremely sensitive when actual values approach zero
* **Infinite errors:** Can produce extremely large or infinite values with small denominators
* **Complementary metrics:** Should always be used alongside magnitude-based error measures like MAPE

## References

* Swanson, D.A., Tayman, J., and Bryan, T.M. "MAPE-R: A rescaled measure of accuracy for cross-sectional subnational population forecasts," Journal of Population Research, 2011
* Armstrong, J.S. and Collopy, F. "Error Measures for Generalizing About Forecasting Methods," International Journal of Forecasting, 1992
