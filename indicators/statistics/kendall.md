# KENDALL: Kendall Rank Correlation Coefficient

[Pine Script Implementation of KENDALL](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/kendall.pine)

## Overview and Purpose

Kendall's Rank Correlation Coefficient (often referred to as Kendall's Tau) is a non-parametric statistical measure that assesses the strength and direction of association between two ranked variables. Developed by Maurice Kendall in 1938, it measures ordinal association—that is, the similarity of the orderings of the data when ranked by each of the quantities. A coefficient of +1 indicates perfect agreement in rankings, -1 indicates perfect disagreement, and 0 indicates no association.

This implementation calculates Kendall's Tau-a coefficient. Tau-a is the simplest variant and does not make specific adjustments for tied ranks in the data, though pairs with ties do not contribute to concordant or discordant counts. It is suitable when ties are relatively infrequent or their impact is considered negligible for a general assessment of ordinal association.

## Core Concepts

*   **Rank Correlation:** Measures the relationship between the rankings of two variables rather than their actual values.
*   **Concordant and Discordant Pairs:** The calculation is based on counting pairs of observations that are either in agreement (concordant) or disagreement (discordant) in their rankings.
*   **Non-parametric:** Makes no assumptions about the distribution of the data, making it robust for non-normally distributed series.
*   **Ordinal Association:** Quantifies the degree to which the relationship between two variables can be described by a monotonic function (i.e., as one variable increases, the other tends to increase or decrease, but not necessarily linearly).

## Common Settings and Parameters

| Parameter        | Type         | Default | Function                                                                 | When to Adjust                                                                                                                               |
| :--------------- | :----------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Source 1         | series float | close   | The primary input series for comparison.                                 | Can be any numerical series (e.g., price, volume, another indicator).                                                                        |
| Source 2 Ticker  | symbol       | "SPY"   | The ticker symbol for the second series (e.g., "SPY", "AAPL", "BTCUSD"). | Change to any valid symbol to compare Source 1 against.                                                                                      |
| Source 2 Data Type | series float | close   | The data type (e.g., close, hlc3) to fetch from the Source 2 Ticker.   | Select the specific data series from the external symbol for comparison.                                                                     |
| Lookback Period  | int          | 14      | The number of bars over which to calculate the correlation. Min 2, Max 60. | Shorter periods are more responsive but can be noisy. Longer periods provide smoother results but lag more. Max 60 due to computational intensity. |

**Pro Tip:** Kendall's Tau is often considered more robust to outliers than Pearson's correlation. Use it when you suspect non-linear relationships or when data may not meet the assumptions for Pearson's (e.g., normality). A `Lookback Period` between 20 and 30 is common for daily charts.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Kendall's Tau works by comparing every possible pair of data points within the lookback period. For each pair of points `(x_i, y_i)` and `(x_j, y_j)`:
- If both `x` and `y` values for point `i` are greater (or both are smaller) than for point `j`, the pair is "concordant" (they agree in rank).
- If one variable is greater for point `i` while the other is smaller, the pair is "discordant" (they disagree in rank).
The Tau-a coefficient is then `(Number of Concordant Pairs - Number of Discordant Pairs) / (Total Number of Pairs)`.

**Technical formula (Kendall's Tau-a):**

Given two series, `X` and `Y`, over a `length` (n) period:
1.  Consider all unique pairs of observations `(x_i, y_i)` and `(x_j, y_j)` where `i < j`. The total number of such pairs is `N = n * (n - 1) / 2`.
2.  For each pair:
    *   If `(x_i - x_j) * (y_i - y_j) > 0`, the pair is **concordant** (P). This means if `x_i > x_j` then `y_i > y_j`, or if `x_i < x_j` then `y_i < y_j`.
    *   If `(x_i - x_j) * (y_i - y_j) < 0`, the pair is **discordant** (Q). This means if `x_i > x_j` then `y_i < y_j`, or if `x_i < x_j` then `y_i > y_j`.
    *   If `(x_i - x_j) * (y_i - y_j) = 0`, the pair is tied in at least one variable. Tau-a does not explicitly count these towards P or Q, and the denominator remains `N`.
3.  Kendall's Tau-a is calculated as:
    `Tau-a = (P - Q) / N`

> 🔍 **Technical Note:** This implementation iterates through all `n * (n - 1) / 2` pairs within the lookback window. Due to this O(n²) complexity per bar, the `Lookback Period` is capped at 60 to manage computational load in Pine Script. The script also handles `na` values within the window by returning `na` for the coefficient if any data point is missing.

## Interpretation Details

Kendall's Tau ranges from -1 to +1:

*   **Tau ≈ +1:** Strong positive ordinal association. As one variable's rank increases, the other variable's rank tends to increase.
*   **Tau ≈ -1:** Strong negative ordinal association. As one variable's rank increases, the other variable's rank tends to decrease.
*   **Tau ≈ 0:** Weak or no ordinal association between the ranks of the two variables.
*   **Magnitude:** The absolute value of Tau indicates the strength of the association. For example, 0.7 is a stronger association than 0.3. Values above |0.5| are often considered moderately strong, while values above |0.7| or |0.8| suggest strong association.

## Common Applications

1.  **Comparing Asset Relationships:** Assess if two assets tend to move in the same or opposite rank order (e.g., comparing a stock to an index like SPY).
2.  **Confirming Divergences:** Identify if an oscillator's rank movements align with price rank movements.
3.  **Non-Linear Relationship Detection:** Useful when the relationship between series is monotonic but not necessarily linear.
4.  **Model Evaluation:** Can be used to compare the rank-order predictions of a model against actual outcomes.

## Limitations and Considerations

*   **Computational Intensity:** The O(n²) nature of the calculation limits the practical `Lookback Period` in Pine Script.
*   **Tau-a and Ties:** This Tau-a implementation does not make specific adjustments for ties in the denominator (like Tau-b or Tau-c would). If many ties are present in the data, Tau-a might underestimate the true correlation strength compared to Tau-b.
*   **Interpretation of Magnitude:** While general guidelines exist (e.g., |0.5| as moderate), the practical significance of a given Tau value can be context-dependent.
*   **Causation:** Correlation (including rank correlation) does not imply causation.
*   **Sensitivity to Window Length:** The calculated Tau value can change with different `Lookback Period` settings.

## References

*   Kendall, M. G. (1938). "A New Measure of Rank Correlation". *Biometrika*, 30(1/2), 81–93.
*   Wikipedia contributors. (2023). *Kendall rank correlation coefficient*. Wikipedia, The Free Encyclopedia.
