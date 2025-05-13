# SPEARMAN: Spearman Rank Correlation Coefficient

[Pine Script Implementation of SPEARMAN](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/spearman.pine)

## Overview and Purpose

Spearman's Rank Correlation Coefficient (Spearman's Rho, denoted by ρ or rs) is a non-parametric measure of statistical dependence between the rankings of two variables. It assesses how well the relationship between two variables can be described using a monotonic function. If there are no repeated data values, a perfect Spearman correlation of +1 or −1 occurs when each of the variables is a perfect monotone function of the other.

Unlike Pearson's correlation, which measures linear relationships, Spearman's correlation can capture monotonic non-linear relationships. It also does not require the variables to be normally distributed, making it suitable for ordinal data or for continuous data that deviates from normality.

This implementation calculates Spearman's Rho by:
1.  Taking two input time series (`source1` and `source2`) over a specified `length`.
2.  For each series, converting the values within the current lookback window into ranks. Ties in ranks are handled by assigning the average of the ranks that would have been assigned had there been no ties.
3.  Calculating Pearson's correlation coefficient on these two sets of ranks.

## Core Concepts

*   **Rank Correlation:** Measures the relationship between the rankings of two variables rather than their actual values.
*   **Monotonic Relationship:** Assesses if, as one variable increases, the other variable tends to consistently increase (positive monotonic) or consistently decrease (negative monotonic), but not necessarily at a constant rate.
*   **Non-parametric:** Makes no assumptions about the underlying distribution of the data.
*   **Pearson on Ranks:** The calculation is mathematically equivalent to applying Pearson's correlation formula to the ranked values of the two series.

## Common Settings and Parameters

| Parameter          | Type         | Default | Function                                                                    | When to Adjust                                                                                                                                  |
| :----------------- | :----------- | :------ | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| Source 1           | series float | close   | The primary input series for comparison.                                    | Can be any numerical series (e.g., price, volume, another indicator).                                                                           |
| Source 2 Ticker    | symbol       | "SPY"   | The ticker symbol for the second series (e.g., "SPY", "AAPL", "BTCUSD").    | Change to any valid symbol to compare Source 1 against.                                                                                         |
| Source 2 Data Type | series float | close   | The data type (e.g., close, hlc3) to fetch from the Source 2 Ticker.      | Select the specific data series from the external symbol for comparison.                                                                        |
| Lookback Period    | int          | 20      | The number of bars over which to calculate the correlation. Min 2, Max 60.  | Shorter periods are more responsive but can be noisy. Longer periods provide smoother results but lag more. Max 60 due to ranking complexity. |

**Pro Tip:** Use Spearman correlation when you suspect a non-linear but monotonic relationship between two series, or when the data contains significant outliers or is not normally distributed. A `Lookback Period` between 20 and 50 is common for daily charts.

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  For a given lookback period, take the values of `Source 1` and `Source 2`.
2.  Independently for each source, convert the actual values into ranks. For example, if `Source 1` values in the window are `[10, 30, 5]`, their ranks would be `[2, 3, 1]`. If there are ties (e.g., `[10, 20, 10]`), average ranks are assigned (e.g., `[1.5, 3, 1.5]`).
3.  Once you have two series of ranks (one for `Source 1` and one for `Source 2`), calculate the standard Pearson correlation coefficient between these two rank series.

**Technical formula:**
Let `X` and `Y` be two series of length `n`.
1.  Convert `X` into ranks `R(X) = (R(x_1), R(x_2), ..., R(x_n))`.
2.  Convert `Y` into ranks `R(Y) = (R(y_1), R(y_2), ..., R(y_n))`.
    *   Ties are handled by assigning each tied value the average of the ranks they would have occupied. For example, if values at ranks 3, 4, 5 are tied, they all get rank `(3+4+5)/3 = 4`.
3.  Spearman's Rho (ρ) is then the Pearson correlation coefficient between `R(X)` and `R(Y)`:
    `ρ = Cov(R(X), R(Y)) / (σ_R(X) * σ_R(Y))`
    where `Cov` is the covariance and `σ` is the standard deviation.

    Alternatively, if all `n` ranks are distinct integers, it can be computed using the popular formula:
    `ρ = 1 - (6 * Σ d_i^2) / (n * (n^2 - 1))`
    where `d_i = R(x_i) - R(y_i)` is the difference between the ranks of each observation.
    However, this simplified formula is not accurate when ties are present. This Pine Script implementation uses the Pearson formula on ranks, which is robust to ties.

> 🔍 **Technical Note:** The ranking process itself has a complexity of O(n²) per bar within the lookback window because each value is compared against all other values in the window to determine its rank. This is why the `Lookback Period` is capped at 60 to manage computational load in Pine Script. The Pearson correlation calculation on ranks is O(n).

## Interpretation Details

Spearman's Rho ranges from -1 to +1:

*   **ρ ≈ +1:** Strong positive monotonic relationship. As one variable's rank increases, the other variable's rank tends to increase.
*   **ρ ≈ -1:** Strong negative monotonic relationship. As one variable's rank increases, the other variable's rank tends to decrease.
*   **ρ ≈ 0:** Weak or no monotonic relationship between the ranks of the two variables.
*   **Magnitude:** The absolute value of ρ indicates the strength of the monotonic association. Values above |0.5| are often considered moderately strong, while values above |0.7| or |0.8| suggest strong association.

**Comparison with Pearson's Correlation:**
*   Pearson measures the strength of a *linear* relationship.
*   Spearman measures the strength of a *monotonic* relationship (which can be linear or non-linear).
*   Spearman is less sensitive to outliers than Pearson because it uses ranks.

## Common Applications

1.  **Identifying Non-Linear Monotonic Trends:** Useful for detecting relationships where variables move in the same/opposite direction but not necessarily at a constant rate (e.g., comparing an asset's price to its volume when the relationship isn't strictly linear).
2.  **Robust Correlation Analysis:** When data is skewed, contains outliers, or is not normally distributed, Spearman provides a more robust measure of association than Pearson.
3.  **Comparing Asset Relationships:** Assess if two assets tend to move in the same or opposite rank order, even if their price changes are not linearly proportional.
4.  **Validating Indicator Signals:** Check if an indicator's movements (e.g., an oscillator) have a monotonic relationship with price movements.

## Limitations and Considerations

*   **Computational Intensity:** The O(n²) ranking step limits the practical `Lookback Period` in Pine Script.
*   **Loss of Information:** By converting values to ranks, some information about the magnitude of differences between values is lost.
*   **Interpretation of Monotonicity:** A high Spearman correlation indicates a strong monotonic relationship, but it doesn't describe the *shape* of that relationship beyond being consistently increasing or decreasing.
*   **Causation:** Correlation (including rank correlation) does not imply causation.
*   **Sensitivity to Window Length:** The calculated ρ value can change with different `Lookback Period` settings.

## References

*   Spearman, C. (1904). "The proof and measurement of association between two things". *American Journal of Psychology*, 15(1), 72–101.
*   Wikipedia contributors. (2023). *Spearman's rank correlation coefficient*. Wikipedia, The Free Encyclopedia.
