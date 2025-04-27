# SMAPE: Symmetric Mean Absolute Percentage Error

[Pine Script Implementation of SMAPE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/smape.pine)

## Overview and Purpose

The Symmetric Mean Absolute Percentage Error (SMAPE) is an improved percentage-based error metric designed to address the limitations of traditional MAPE (Mean Absolute Percentage Error). Developed in the 1980s and popularized in the M3 forecasting competition, SMAPE provides a symmetrical approach to percentage errors, treating over-predictions and under-predictions equally. This makes it particularly valuable for financial analysis where both types of prediction errors can be equally problematic. By constraining results to a 0-200% range and improving stability near zero values, SMAPE offers a more reliable way to evaluate and compare prediction accuracy across different scales and market conditions.

## Core Concepts

* **Symmetrical error handling:** Treats over-predictions and under-predictions equally, unlike MAPE which is asymmetric
* **Improved zero handling:** Maintains stability when values approach zero, avoiding the infinite error problem in traditional MAPE
* **Market application:** Particularly useful for comparing forecast accuracy across different instruments or timeframes with varying price scales

The core innovation of SMAPE is using the sum of absolute values in the denominator rather than just the actual value (as MAPE does). This seemingly small change creates a more balanced metric that doesn't unfairly penalize under-predictions, making it much more suitable for financial forecasting where bias in either direction can be equally costly.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for smoother error measurements, decrease for more responsiveness |
| Source 1 | close | First signal for comparison | Typically your actual or target value |
| Source 2 | sma(close,20) | Second signal for comparison | Typically your forecast or model output |

**Pro Tip:** When comparing multiple forecasting models using SMAPE, focus on relative differences between models rather than absolute values - a 5% improvement in SMAPE often represents a significant enhancement in predictive power.

## Calculation and Mathematical Foundation

**Simplified explanation:**
SMAPE calculates the percentage difference between two signals, but uses the average of both values in the denominator instead of just one value. This creates a balanced measure that treats both signals equally and avoids problems when values get close to zero.

**Technical formula:**
SMAPE = (200%/p) * Σ|Y₁ - Y₂| / (|Y₁| + |Y₂|)

Where:
- Y₁, Y₂ are the signals being compared
- p is the averaging period

> 🔍 **Technical Note:** The 200% multiplier makes SMAPE report percentages in the 0-200% range rather than 0-100%. This is the standard formulation, though some implementations normalize to 0-100% by using a 100% multiplier instead.

## Interpretation Details

SMAPE can be applied in various financial contexts:

* **Forecast evaluation:** Compare prediction accuracy between different forecasting models
* **Indicator tuning:** Optimize parameters of technical indicators by minimizing SMAPE
* **Cross-market comparison:** Evaluate prediction accuracy across different instruments regardless of price scale
* **Trading system assessment:** Measure how closely system signals track intended targets
* **Signal consistency:** Monitor the stability of relationships between different market variables

## Limitations and Considerations

* **Range interpretation:** The 0-200% range can be counterintuitive compared to traditional 0-100% error metrics
* **Undefined values:** Formula becomes undefined when both values are exactly zero
* **Asymptotic behavior:** Approaches 200% when either value is zero, which may overstate error magnitude
* **Information loss:** Like most percentage metrics, obscures absolute magnitude of differences
* **Complementary metrics:** Best used alongside absolute error measures for comprehensive evaluation

## References

* Makridakis, S. "Accuracy measures: theoretical and practical concerns," International Journal of Forecasting, 1993
* Hyndman, R.J. and Koehler, A.B. "Another look at measures of forecast accuracy," International Journal of Forecasting, 2006
