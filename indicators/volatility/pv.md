# PV: Parkinson Volatility

[Pine Script Implementation of PV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/pv.pine)

## Overview and Purpose

Parkinson Volatility (PV), also known as the Parkinson Number, is a historical volatility estimator that uses the high and low prices of an asset over a given period. It was introduced by Michael Parkinson in 1980. This estimator is particularly noted for its efficiency compared to traditional close-to-close volatility, especially when price movements follow a geometric Brownian motion with zero drift.

The core idea is that the high-low range of a period contains more information about volatility than just the closing price. PV assumes that prices do not have a significant trend (drift) during the estimation period.

## Core Concepts

*   **High-Low Range:** Utilizes the natural logarithm of the ratio of the high price to the low price ($\ln(H/L)$) for each period.
*   **Zero Drift Assumption:** The derivation of the Parkinson number assumes that the underlying asset price follows a random walk without a trend. If a strong trend is present, Parkinson Volatility can underestimate the true volatility.
*   **Efficiency:** Under its assumptions, it is a more efficient estimator of volatility than close-to-close methods, meaning it can provide a more accurate estimate with the same amount of data.
*   **Smoothing:** The squared log-ratio term is typically smoothed (e.g., using an RMA or SMA) over a lookback period before the final volatility calculation.
*   **Annualization:** The resulting per-period volatility is often annualized for comparability.

## Common Settings and Parameters

| Parameter       | Default | Function                                                                              | When to Adjust                                                                                                |
|-----------------|---------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `length`        | 20      | The lookback period for smoothing the squared Parkinson term (e.g., using RMA).       | Shorter periods make PV more reactive; longer periods provide a smoother, more stable measure.                  |
| `annualize`     | `true`  | Whether to annualize the volatility output.                                           | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                |
| `annualPeriods` | 252     | Number of trading periods in a year for annualization.                                | Adjust based on data frequency (e.g., 252 for daily, 52 for weekly, 365 for calendar day data if applicable). |

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  For each period, calculate the term: $P_i = \ln(\text{High}_i / \text{Low}_i)$.
2.  Square this term: $P_i^2$.
3.  Smooth these squared terms over the specified `length` (e.g., using RMA): $\text{Smoothed}(P^2)$.
4.  Calculate the Parkinson Volatility for the period: $\sigma_{\text{Parkinson, period}} = \sqrt{ \frac{\text{Smoothed}(P^2)}{4 \ln(2)} }$.
5.  (Optional) Annualize this per-period volatility: $\sigma_{\text{Parkinson, annual}} = \sigma_{\text{Parkinson, period}} \cdot \sqrt{\text{AnnualPeriods}}$.

**Technical formula for a single period's Parkinson Number variance ($\sigma_P^2$):**
$\sigma_P^2 = \frac{1}{4 \ln 2} \cdot [\ln(H) - \ln(L)]^2 = \frac{1}{4 \ln 2} \cdot [\ln(H/L)]^2$

The indicator typically calculates this for each bar, then smooths the $\sigma_P^2$ (or just the $[\ln(H/L)]^2$ part) over `length` periods, and then takes the square root.

Let $X_i = [\ln(H_i/L_i)]^2$.
Smoothed $X_S = \text{RMA}(X, \text{length})$
$\text{PV}_{\text{period}} = \sqrt{\frac{X_S}{4 \ln(2)}}$
$\text{PV}_{\text{annual}} = \text{PV}_{\text{period}} \cdot \sqrt{\text{AnnualPeriods}}$

The constant $4 \ln(2) \approx 2.7725887222$.

## Interpretation Details

*   **Magnitude:** Higher PV values indicate greater price volatility based on the high-low range. Lower PV values suggest less volatility.
*   **Comparison:** PV can be compared to other volatility measures (like close-to-close HV or Garman-Klass) to understand different aspects of price movement.
*   **Trend in PV:**
    *   **Rising PV:** Suggests increasing volatility.
    *   **Falling PV:** Suggests decreasing volatility.
*   **Regime Changes:** Significant shifts in PV levels can indicate changes in market regime (e.g., from low volatility to high volatility).

## Limitations and Considerations

*   **Zero Drift Assumption:** This is a key limitation. If the asset has a strong directional trend, PV will underestimate the true volatility.
*   **Opening/Closing Gaps:** PV does not explicitly account for overnight gaps or the relationship between open and close prices, unlike estimators like Garman-Klass or Yang-Zhang.
*   **Sensitivity to Outliers in High/Low:** Extreme, one-off spikes in high or low prices within a period can disproportionately affect the $\ln(H/L)$ term for that period.
*   **Choice of Lookback Period:** The `length` for smoothing significantly impacts the responsiveness and smoothness of the PV line.

## References

*   Parkinson, M. (1980). The Extreme Value Method for Estimating the Variance of the Rate of Return. *The Journal of Business, 53*(1), 61-65.
*   Garman, M. B., & Klass, M. J. (1980). On the Estimation of Security Price Volatilities from Historical Data. *The Journal of Business, 53*(1), 67-78. (Often discussed in conjunction with Parkinson).
