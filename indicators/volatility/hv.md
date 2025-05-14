# HV: Historical Volatility (Close-to-Close)

[Pine Script Implementation of HV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/hv.pine)

## Overview and Purpose

Historical Volatility (HV), often referred to as statistical volatility, is a measure of the dispersion of returns for a given security or market index over a specified period. It is calculated by taking the standard deviation of logarithmic returns (typically close-to-close returns) over that period. The result is then often annualized to express volatility in yearly terms, making it comparable across different timeframes and assets.

HV quantifies how much the price of an asset has fluctuated in the past. It is a backward-looking measure and does not predict future volatility, but it provides a baseline understanding of an asset's price variability.

## Core Concepts

*   **Logarithmic Returns:** Uses logarithmic returns (natural log of the ratio of current price to previous price) as they are time-additive and have more desirable statistical properties for financial analysis.
*   **Standard Deviation:** The core of HV is the statistical standard deviation, which measures the dispersion of these returns around their average.
*   **Lookback Period:** HV is calculated over a defined historical window (e.g., 20 days, 90 days).
*   **Annualization:** The per-period standard deviation is typically multiplied by the square root of the number of periods in a year to get an annualized figure.

## Common Settings and Parameters

| Parameter     | Default | Function                                                                 | When to Adjust                                                                                                |
|---------------|---------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `src`         | `close` | The source price series for calculating returns.                         | Can be changed to `hlc3`, `ohlc4`, etc., but `close` is standard for traditional HV.                         |
| `length`      | 20      | The lookback period for calculating the standard deviation of returns.   | Shorter periods make HV more reactive to recent price changes; longer periods provide a smoother, more stable measure. |
| `annualize`   | `true`  | Whether to annualize the volatility output.                              | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                |
| `annualPeriods`| 252     | Number of trading periods in a year for annualization.                   | Adjust based on data frequency (e.g., 252 for daily, 52 for weekly, 365 for calendar day data if applicable). |

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  Calculate the logarithmic return for each period in the lookback window: $\ln(\text{Price}_t / \text{Price}_{t-1})$.
2.  Calculate the standard deviation of these logarithmic returns over the specified `length`.
3.  (Optional) Annualize this standard deviation by multiplying it by the square root of `annualPeriods`.

**Technical formula:**

Logarithmic Return ($R_t$):
$R_t = \ln \left( \frac{P_t}{P_{t-1}} \right)$
Where $P_t$ is the price at time $t$.

Standard Deviation ($\sigma_{\text{period}}$) of $N$ returns:
$\sigma_{\text{period}} = \sqrt{ \frac{1}{N-1} \sum_{i=1}^{N} (R_i - \bar{R})^2 }$
Where $N$ is the `length`, $R_i$ is the log return for period $i$, and $\bar{R}$ is the average log return over $N$ periods.
(Note: Pine Script's `ta.stdev` function handles this calculation.)

Annualized Historical Volatility ($HV_{\text{annual}}$):
$HV_{\text{annual}} = \sigma_{\text{period}} \cdot \sqrt{\text{AnnualPeriods}}$

## Interpretation Details

*   **Magnitude:** A higher HV value indicates that the asset's price has experienced larger fluctuations (higher volatility) over the lookback period. A lower HV suggests more price stability.
*   **Trend in HV:**
    *   **Rising HV:** Suggests that volatility is increasing.
    *   **Falling HV:** Suggests that volatility is decreasing.
*   **Context is Key:** HV should be interpreted in context. For example, an HV of 30% might be high for a utility stock but low for a biotech startup. Comparing current HV to its own historical range or to the HV of related assets can be more insightful.
*   **Implied vs. Historical:** HV is often compared with Implied Volatility (derived from option prices) to assess whether options are relatively cheap or expensive.

## Limitations and Considerations

*   **Backward-Looking:** HV only describes past price behavior and does not guarantee future volatility. Market conditions can change rapidly.
*   **Choice of Lookback Period:** The HV value can vary significantly depending on the `length` chosen. There's no single "correct" period.
*   **Sensitivity to Outliers:** Standard deviation can be sensitive to extreme price movements (outliers) within the lookback period.
*   **Assumes Normal Distribution (Often):** While not strictly required for calculation, interpretations often implicitly assume returns are somewhat normally distributed. Financial returns often exhibit fat tails (more extreme events than a normal distribution would suggest).
*   **Ignores Intraday Information:** Traditional close-to-close HV only uses closing prices, ignoring intraday price swings (highs, lows, opens). Range-based estimators like Garman-Klass or Parkinson attempt to address this.

## References

*   Hull, J. C. (2018). *Options, Futures, and Other Derivatives*. Pearson Education. (Standard textbook covering volatility concepts).
*   Natenberg, S. (1994). *Option Volatility and Pricing: Advanced Trading Strategies and Techniques*. McGraw-Hill.
