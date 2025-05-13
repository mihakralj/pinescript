# THEIL: Theil Index

[Pine Script Implementation of THEIL](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/theil.pine)

## Overview and Purpose

The Theil Index is a statistic primarily used to measure  inequality and other forms of concentration. It belongs to a class of entropy-based measures, meaning it quantifies the "evenness" or "spread-out-ness" of values, similar to how entropy measures disorder in other scientific fields. Specifically, this indicator calculates Theil's T Index.

A Theil Index of 0 indicates perfect equality (all values in the dataset are the same), while higher values signify greater inequality or concentration. This indicator computes Theil's T Index for a given input series over a specified lookback period, providing a dynamic measure of how concentrated or dispersed the data has been.

## Core Concepts

*   **Inequality Measure:** A statistical measure that quantifies the dispersion or spread of a distribution. In economics, it often refers to the distribution of income or wealth; in market analysis, it might refer to the distribution of trading volumes or market capitalizations.
*   **Entropy Connection:** The Theil Index is derived from the concept of entropy in information theory. In this context, a higher Theil Index corresponds to a distribution that is more "surprising" or "uneven," while a lower index suggests a more uniform or predictable distribution.
*   **Theil's T Index (T_T):** One of the two common forms of the Theil Index (the other being Theil's L, or Mean Log Deviation). The T Index is calculated as:
    `T_T = (1/N) * Σ (xᵢ / μ) * ln(xᵢ / μ)`
    Where:
    *   `N` is the number of valid data points (positive and non-`na`) in the sample.
    *   `xᵢ` is the value of the i-th data point.
    *   `μ` is the arithmetic mean of these `N` data points `xᵢ`.
    *   `ln` is the natural logarithm.
    *   The sum `Σ` is taken over all `i` from 1 to `N`.
    *   **Note:** This formula requires all `xᵢ` to be positive. If any `xᵢ` were zero, its corresponding term `(xᵢ / μ) * ln(xᵢ / μ)` is treated as 0, based on the mathematical limit: `lim (y * ln(y))` as `y → 0⁺` is 0. The Pine Script implementation filters for `xᵢ > 0`.

## Common Settings and Parameters

| Parameter       | Type         | Default | Function                                                                                                | When to Adjust                                                                                                                                                              |
| :-------------- | :----------- | :------ | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | series float | close   | The input data series (e.g., price, volume, market cap). **Must consist of positive values.**           | Choose the series whose inequality or concentration you want to measure. Ensure data is positive (e.g., prices, not price changes that can be negative or zero).                     |
| Lookback Period | int          | 14      | The number of bars (sample size `N`) used for calculating the mean and Theil Index. Min 1.              | A larger period provides a more stable estimate over a longer term but will be less responsive to recent changes. A shorter period is more reactive to shifts in distribution. |

**Pro Tip:** When comparing assets, the Theil Index can reveal differences in market character. For instance, if Stock A (e.g., a volatile penny stock) consistently shows a higher Theil Index for its daily trading volumes compared to Stock B (e.g., a blue-chip stock with similar average daily volume), it might suggest Stock A's trading activity is more concentrated in a few high-volume days (spikes), whereas Stock B's volume is more evenly distributed. This could imply differences in liquidity patterns or event-driven trading.

## Calculation and Mathematical Foundation

The Theil's T Index is calculated as follows for a given `source` series and `length`:

1.  **Data Collection:** A window of the most recent `length` data points from `source` is considered.
2.  **Data Validation:** Only positive (`> 0`) and non-`na` values from this window are included in the calculation. Let `N_valid` be the count of such values. If `N_valid` is 0, the index is `na`.
3.  **Mean Calculation (μ):** The arithmetic mean of these `N_valid` positive data points is calculated: `μ = (Σ xᵢ) / N_valid`. If `μ` is zero or negative (which should not occur if all `xᵢ` are positive and `N_valid > 0`), the index is `na`.
4.  **Ratio Calculation:** For each valid data point `xᵢ`, the ratio `rᵢ = xᵢ / μ` is computed.
5.  **Logarithm of Ratio:** The natural logarithm `ln(rᵢ)` is calculated for each ratio. Since `xᵢ` and `μ` are positive, `rᵢ` is positive, so `ln(rᵢ)` is well-defined.
6.  **Summation of Terms:** The sum of `rᵢ * ln(rᵢ)` is computed across all `N_valid` data points: `Sum_terms = Σ (rᵢ * ln(rᵢ))`.
7.  **Theil's T Index:** The index is then calculated: `T_T = Sum_terms / N_valid`.

> 🔍 **Technical Note:**
> *   The implementation strictly requires positive data (`xᵢ > 0`). Non-positive or `na` values in the source series are excluded from the calculation.
> *   The term `(xᵢ / μ) * ln(xᵢ / μ)` is 0 if `xᵢ / μ = 1` (i.e., `xᵢ = μ`, meaning the value is exactly average).
> *   The Theil Index value is influenced by the number of valid data points `N_valid` in the lookback period, as this affects both the mean and the maximum possible value of the index.

## Interpreting the Theil Index

*   **Range:** The Theil's T Index is non-negative.
    *   `T_T = 0`: Indicates perfect equality. This means all `xᵢ` values in the sample are identical (and therefore equal to the mean `μ`).
    *   `T_T > 0`: Indicates some level of inequality. The larger the Theil Index, the greater the inequality or concentration in the dataset.
*   **Maximum Value:** The maximum possible value for Theil's T is `ln(N_valid)`. This theoretical maximum occurs in a situation of perfect inequality where one data point accounts for the total sum of values, and all other `N_valid - 1` data points are infinitesimally small (approaching zero). For example, if `N_valid = 14`, the maximum Theil T would be `ln(14) ≈ 2.639`. A value close to this would signify extreme concentration.
*   **Changes Over Time:**
    *   An **increasing** Theil Index suggests that the distribution of the source data is becoming more unequal or concentrated over time.
    *   A **decreasing** Theil Index suggests that the distribution is becoming more equal or dispersed.

## Common Applications

1.  **Economics:** Its primary application is measuring income inequality or wealth distribution within a population or region.
2.  **Market Analysis:**
    *   **Market Share Concentration:** Can be applied to the market shares of companies within an industry to assess market dominance.
    *   **Trading Volume/Value Concentration:** Analyze if trading volume or value is concentrated in a few specific periods (e.g., opening/closing hours, specific days) or among a few assets in a portfolio/market.
    *   **Portfolio Analysis:** Assess the concentration of value or risk contribution among assets in a portfolio.
3.  **Sociology & Demography:** Measuring disparities in various social indicators, resource allocation, or population distributions.
4.  **Information Theory:** The index has roots in information theory and relates to measures of redundancy or information content in a system.

## Limitations and Considerations

*   **Positive Data Requirement:** The standard Theil Index formula is defined for positive values only. Applying it to data that can be zero or negative (like price changes or returns) requires careful data preparation, such as using absolute values, focusing on a specific subset of positive data, or choosing a different inequality measure. This implementation filters out non-positive data.
*   **Sensitivity to Small Values:** The logarithm component means the index can be influenced by very small positive values, especially if they coexist with much larger values in the dataset.
*   **Not Normalized (0 to ln(N)):** Unlike some indices bounded between 0 and 1 (like the Gini coefficient), Theil's T ranges from 0 to `ln(N_valid)`. When comparing Theil indices across datasets of significantly different sizes (`N_valid`), this difference in maximum potential value should be kept in mind. Normalization (e.g., `T_T / ln(N_valid)`) can be performed for such comparisons but is not part of the standard Theil T definition.
*   **Interpretation Nuance:** While it quantifies overall inequality, the Theil Index (like other single-number inequality measures) doesn't reveal *where* in the distribution the inequality is most pronounced (e.g., driven by a few extremely high values vs. many very low values) without further decomposition techniques (which are advanced features not implemented here).

## References

*   Theil, H. (1967). *Economics and information theory*. North-Holland Publishing Company.
*   Wikipedia contributors. (2023). *Theil index*. Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Theil_index](https://en.wikipedia.org/wiki/Theil_index)
