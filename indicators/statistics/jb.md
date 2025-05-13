# JB: Jarque-Bera Test

[Pine Script Implementation of JB](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/jb.pine)

## Overview and Purpose

The Jarque-Bera (JB) test is a goodness-of-fit test used in statistics to determine if sample data exhibit skewness and kurtosis that are consistent with a normal distribution. The test statistic is a measure of how far the sample's skewness and kurtosis deviate from the values expected from a normal distribution (which has a skewness of 0 and a kurtosis of 3, or excess kurtosis of 0).

A large Jarque-Bera statistic indicates that the data are not normally distributed. Conversely, a small statistic suggests that the data are consistent with a normal distribution. This indicator calculates the Jarque-Bera statistic for a given input series over a specified lookback period.

## Core Concepts

*   **Normality Test:** A statistical test to assess if a dataset is well-modeled by a normal distribution.
*   **Skewness (S):** A measure of the asymmetry of the probability distribution. A normal distribution has S=0.
    *   Calculated as the third standardized moment: `m3 / σ³`, where `m3` is the third central moment (`Σ(xᵢ - μ)³/n`) and `σ` is the standard deviation.
*   **Kurtosis (K):** A measure of the "tailedness" of the probability distribution. A normal distribution has K=3.
    *   Calculated as the fourth standardized moment: `m4 / σ⁴`, where `m4` is the fourth central moment (`Σ(xᵢ - μ)⁴/n`).
*   **Excess Kurtosis (EK):** Kurtosis minus 3 (i.e., `EK = K - 3`). A normal distribution has EK=0.
*   **Jarque-Bera Statistic (JB):** The test statistic is calculated as: `JB = (n/6) * (S² + (EK²/4))`, where `n` is the sample size (lookback period), S is the sample skewness, and EK is the sample excess kurtosis.
*   **Chi-squared Distribution:** Under the null hypothesis (H₀) that the data are normally distributed, the Jarque-Bera statistic asymptotically (for large samples) has a chi-squared (χ²) distribution with 2 degrees of freedom.

## Common Settings and Parameters

| Parameter       | Type         | Default | Function                                                                                                | When to Adjust                                                                                                                                                              |
| :-------------- | :----------- | :------ | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | series float | close   | The input data series (e.g., price, returns, indicator values).                                         | Choose the series whose normality you want to test.                                                                                                                         |
| Lookback Period | int          | 20      | The number of bars (sample size `n`) used for calculating skewness, kurtosis, and the JB statistic. Min 10, Max 200. | A larger period provides more stable estimates but lags more and smooths out recent changes. A minimum of 10 is set for meaningful results. Max 200 due to array processing. |

**Pro Tip:** The Jarque-Bera test is often applied to the residuals of a regression model to check if the normality assumption for errors is met. In trading, it can be applied to returns series or oscillator values to understand their distribution characteristics.

## Calculation and Mathematical Foundation

The Jarque-Bera statistic is derived from the sample skewness and sample excess kurtosis. The calculation steps for a given `source` series and `length` (n) are as follows:

1.  A window of the most recent `n` data points from `source` is taken.
2.  The **mean (μ)** of this window is calculated: `μ = Σxᵢ / n`.
3.  The **second central moment (m2, variance σ²)** is calculated: `m2 = Σ(xᵢ - μ)² / n`.
4.  The **standard deviation (σ)** is `sqrt(m2)`.
5.  The **third central moment (m3)** is calculated: `m3 = Σ(xᵢ - μ)³ / n`.
6.  **Skewness (S)** is calculated: `S = m3 / σ³`.
7.  The **fourth central moment (m4)** is calculated: `m4 = Σ(xᵢ - μ)⁴ / n`.
8.  **Raw Kurtosis (K_raw)** is calculated: `K_raw = m4 / σ⁴`.
9.  **Excess Kurtosis (EK)** is calculated: `EK = K_raw - 3`.
10. The **Jarque-Bera statistic (JB)** is then computed using the formula:
    `JB = (n/6) * (S² + (EK²/4))`

> 🔍 **Technical Note:** This implementation calculates skewness and kurtosis using their moment-based definitions with population standard deviation. Different statistical packages might use sample-corrected versions, which can lead to slightly different results, especially for small sample sizes. The `maxval` for `Lookback Period` is set to 200 to manage computational load from array operations in Pine Script.

## Interpreting the Jarque-Bera Statistic

*   **Null Hypothesis (H₀):** The data are normally distributed (i.e., skewness is 0 and excess kurtosis is 0).
*   **Alternative Hypothesis (H₁):** The data are not normally distributed.
*   **Test Statistic (JB Value):**
    *   A JB value close to 0 suggests that the sample data's skewness and kurtosis are similar to those of a normal distribution.
    *   Higher JB values indicate greater deviation from normality. The further the JB statistic is from 0, the stronger the evidence against the null hypothesis.
*   **Critical Values:** The JB statistic is compared against critical values from the chi-squared (χ²) distribution with 2 degrees of freedom.
    *   If `JB > χ²_critical(α)`, the null hypothesis of normality is rejected at the significance level `α`.
    *   Common critical values plotted by the indicator:
        *   `~4.605` for α = 10% (0.10) significance level.
        *   `~5.991` for α = 5% (0.05) significance level.
        *   `~9.210` for α = 1% (0.01) significance level.

**Example:** If the calculated JB statistic is 7.5:
*   It is greater than 4.605 (10% critical value), so we can reject H₀ at the 10% significance level.
*   It is greater than 5.991 (5% critical value), so we can reject H₀ at the 5% significance level.
*   It is less than 9.210 (1% critical value), so we cannot reject H₀ at the 1% significance level.
This suggests there is evidence against normality, particularly at the 5% and 10% levels.

## Common Applications

1.  **Financial Returns Analysis:** Test if daily, weekly, or monthly returns of an asset follow a normal distribution. Financial returns often exhibit "fat tails" (leptokurtosis, higher kurtosis than normal) and skewness, which the JB test can help identify.
2.  **Model Validation:** In quantitative modeling, if a model (e.g., regression) assumes normally distributed errors (residuals), the JB test can be applied to the residuals to check this crucial assumption.
3.  **Risk Management:** Understanding the distribution of returns is vital for risk assessment models like Value at Risk (VaR). Non-normality, as indicated by the JB test, can significantly impact risk calculations and model choices.
4.  **Strategy Development:** If a trading strategy's performance metrics or the signals it generates are assumed to be normally distributed for evaluation or optimization purposes, the JB test can verify this. Deviations might suggest the need for non-parametric statistical methods or adjustments to the strategy's assumptions.
5.  **Data Exploration:** As a general diagnostic tool to understand the characteristics of a time series before applying other statistical techniques that might assume normality.

## Limitations and Considerations

*   **Sample Size:** The Jarque-Bera test is an asymptotic test, meaning its reliance on the chi-squared distribution is most accurate for large sample sizes (e.g., n > 100 or 200). For small samples, the chi-squared approximation may not be reliable, and the test might over-reject the null hypothesis.
*   **Power of the Test:** The JB test might have low power in detecting deviations from normality if the true distribution is close to normal but not exactly normal, especially with small samples. It is generally more sensitive to large deviations in skewness and kurtosis.
*   **Alternative Tests:** Other normality tests exist, such as the Shapiro-Wilk test (often considered more powerful, especially for smaller samples, but computationally more intensive) or the Kolmogorov-Smirnov test (which tests against any specified distribution, not just normal).
*   **Interpretation Nuance:** Rejecting the null hypothesis of normality indicates that the data are unlikely to have come from a normal distribution. However, it doesn't specify *how* the data deviate (e.g., is it primarily skewness, kurtosis, or both? Is it unimodal or multimodal?). Further examination of descriptive statistics (skewness and kurtosis values themselves) and graphical tools like histograms or Q-Q plots is often necessary for a complete understanding.
*   **Moment Calculation:** The manual calculation of moments in this Pine Script implementation uses population-based formulas for central moments. Different statistical software packages might use sample-corrected versions (e.g., Bessel's correction for variance), which can lead to minor numerical differences, particularly for smaller sample sizes.

## References

*   Jarque, C. M., & Bera, A. K. (1980). "Efficient tests for normality, homoscedasticity and serial independence of regression residuals". *Economics Letters*, 6(3), 255–259.
*   Jarque, C. M., & Bera, A. K. (1987). "A Test for Normality of Observations and Regression Residuals". *International Statistical Review*, 55(2), 163–172.
*   Wikipedia contributors. (2023). *Jarque–Bera test*. Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Jarque–Bera_test](https://en.wikipedia.org/wiki/Jarque–Bera_test)
