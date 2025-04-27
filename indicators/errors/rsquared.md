# RSQUARED: R-squared (Coefficient of Determination)

[Pine Script Implementation of RSQUARED](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rsquared.pine)

## Overview and Purpose

R-squared (Coefficient of Determination) is a statistical measure that quantifies how well one variable explains or predicts another. Unlike error metrics that focus on absolute deviations, R² expresses the proportion of variance in a dependent variable that is predictable from an independent variable or set of variables. Originating in regression analysis, R² has become a standard tool for evaluating model performance across statistics and financial analysis. For traders, it provides a normalized measure (typically 0-1) of how closely two signals track each other, making it particularly valuable for assessing how well indicators, price predictions, or trading systems capture market movements.

## Core Concepts

* **Variance explanation:** Quantifies the percentage of variance in one signal that is explained by another, providing a measure of explanatory power
* **Goodness-of-fit:** Offers a scale-free metric where values closer to 1 indicate stronger relationships between signals
* **Market application:** Particularly useful for evaluating how well technical indicators or prediction models capture overall market trends rather than point-by-point accuracy

The core principle of R² is its focus on explained variance rather than error magnitude. While metrics like MSE or MAE measure absolute differences between signals, R² measures relative predictive power by comparing prediction errors to the baseline variance of the target signal. This makes it especially valuable for understanding how much additional information a model or indicator provides beyond simply knowing the average value.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the window for variance calculation | Increase for more stable evaluation of long-term relationships, decrease for detecting changing relationships |
| Source 1 | close | Target signal (actual values) | Typically the value you're trying to predict or explain |
| Source 2 | sma(close,20) | Predicting signal (model values) | The indicator, model output, or comparative signal |

**Pro Tip:** When evaluating trading indicators, compare their R² values during different market regimes (trending vs. ranging) to identify which indicators provide more explanatory power in specific conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
R² compares how much error remains when using your model versus how much variation existed in the first place. If your model explains 80% of the original variation in the data, the R² is 0.80.

**Technical formula:**
R² = 1 - (Σ(Y₁ - Y₂)² / Σ(Y₁ - Y̅₁)²)

Where:
- Y₁ represents actual values
- Y₂ represents predicted values
- Y̅₁ represents the mean of actual values over the period

> 🔍 **Technical Note:** While R² typically ranges from 0 to 1, it can become negative when models perform worse than simply using the mean as a prediction, indicating a fundamentally flawed model.

## Interpretation Details

R² can be applied in various financial contexts:

* **Indicator evaluation:** Measure how much market movement is captured by technical indicators
* **System validation:** Quantify how well trading systems track the intended market behavior
* **Correlation strength:** Assess the relationship strength between different financial instruments
* **Model selection:** Compare different predictive models to select the one with highest explanatory power
* **Regime identification:** Track changes in R² to detect shifts in relationships between market variables

## Limitations and Considerations

* **Insensitivity to bias:** High R² can occur even with systematically biased predictions
* **Over-optimization risk:** Adding variables almost always increases R², even with irrelevant predictors
* **Non-linear relationships:** May not fully capture complex non-linear dependencies
* **Outlier sensitivity:** Can be heavily influenced by a few extreme values
* **Correlation vs. causation:** High R² doesn't necessarily imply causal relationships

## References

* Draper, N.R. and Smith, H. "Applied Regression Analysis," Wiley, 1998
* Alexander, C. "Market Models: A Guide to Financial Data Analysis," Wiley, 2001
