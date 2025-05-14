# GKV: Garman-Klass Volatility

[Pine Script Implementation of GKV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/gkv.pine)

## Overview and Purpose

The Garman-Klass Volatility (GKV) is an estimator for historical volatility that utilizes high, low, open, and close prices (HLOC). Developed by Mark B. Garman and Michael J. Klass in 1980, it is designed to be more efficient than traditional close-to-close volatility estimators by incorporating more information from the price bar. It is particularly useful for estimating volatility when only daily HLOC data is available and aims to provide a better reflection of the true underlying volatility during a trading period.

The GKV estimator is based on the assumption that prices follow a geometric Brownian motion with zero drift. It provides a per-period variance estimate, which is then typically smoothed (e.g., using a moving average) and annualized to derive a volatility measure.

## Core Concepts

*   **HLOC Data Utilization:** Incorporates high, low, open, and close prices to capture more intraday price movement information than close-to-close methods.
*   **Efficiency:** Aims for higher statistical efficiency in estimating volatility compared to simpler methods.
*   **Logarithmic Prices:** Calculations are based on the natural logarithm of prices.
*   **Zero Drift Assumption:** The original model assumes no underlying trend or drift in the price series for the period being estimated.
*   **Smoothing:** The raw Garman-Klass estimator for each period is often noisy, so it's typically smoothed over a lookback period using a moving average (e.g., RMA/Wilder's MA in this implementation).

## Common Settings and Parameters

| Parameter     | Default | Function                                                                 | When to Adjust                                                                                                |
|---------------|---------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `length`      | 20      | The lookback period for smoothing the raw Garman-Klass estimates.        | Shorter periods make it more reactive; longer periods provide smoother but more lagging results.                |
| `annualize`   | `true`  | Whether to annualize the volatility output.                              | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                |
| `annualPeriods`| 252     | Number of trading periods in a year for annualization.                   | Adjust based on data frequency (e.g., 252 for daily, 52 for weekly, 12 for monthly).                          |

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  For each period, calculate a variance estimate using a formula that combines the logarithms of high, low, open, and close prices.
2.  Smooth this series of per-period variance estimates using a moving average (e.g., RMA).
3.  Take the square root of the smoothed variance to get the per-period volatility.
4.  (Optional) Annualize this per-period volatility.

**Technical formula:**

The Garman-Klass estimator for the variance ($\sigma_{GK}^2$) of a single period is:
$\sigma_{GK}^2 = 0.5 \cdot [\ln(H) - \ln(L)]^2 - [2\ln(2) - 1] \cdot [\ln(C) - \ln(O)]^2$

Where:
*   $H$ = High price for the period
*   $L$ = Low price for the period
*   $O$ = Open price for the period
*   $C$ = Close price for the period
*   $\ln$ = Natural logarithm
*   The constant $2\ln(2) - 1 \approx 0.386294$

This per-period $\sigma_{GK}^2$ is then typically smoothed. If using an RMA of `length` $N$:
Smoothed $\sigma_{GK,t}^2 = \text{RMA}_N(\sigma_{GK}^2)$

The Garman-Klass Volatility ($v_{GKV,t}$) is:
$v_{GKV,t} = \sqrt{\text{Smoothed }\sigma_{GK,t}^2}$

If annualizing:
Annualized $v_{GKV,t} = v_{GKV,t} \cdot \sqrt{\text{AnnualPeriods}}$

> 🔍 **Technical Note:** The Pine Script implementation uses a bias-corrected RMA for smoothing to ensure accurate values from the beginning of the series. The estimator can sometimes produce negative variance estimates, especially with noisy data or if the model assumptions are violated; in such cases, the square root would result in `na`.

## Interpretation Details

*   **Rising GKV:** Indicates increasing market volatility as estimated by the Garman-Klass method.
*   **Falling GKV:** Suggests decreasing market volatility.
*   **Comparison:** GKV can be compared to other volatility estimators (like close-to-close or ATR) to gain different perspectives on market risk. It often provides a more stable estimate than simple close-to-close volatility.

## Limitations and Considerations

*   **Zero Drift Assumption:** The model's assumption of zero drift might not hold in trending markets, potentially affecting accuracy. Extensions like the Yang-Zhang estimator attempt to address this.
*   **Opening/Closing Gaps:** While it uses open and close, its handling of overnight gaps might differ from estimators like ATR that explicitly incorporate previous close.
*   **Data Quality:** Sensitive to the quality of HLOC data. Erroneous price spikes can distort the estimate.
*   **Negative Variance:** The raw Garman-Klass formula can occasionally yield a negative variance estimate, especially for periods with very small high-low ranges but larger open-close ranges. The implementation handles this by returning `na` for volatility if the smoothed variance is negative.
*   **Smoothing Lag:** The necessary smoothing introduces lag, similar to other moving average-based indicators.

## References

*   Garman, M. B., & Klass, M. J. (1980). On the Estimation of Security Price Volatilities from Historical Data. *The Journal of Business, 53*(1), 67–78.
*   Rogers, L. C. G., & Satchell, S. E. (1991). Estimating Variance from High, Low, Open, and Closing Prices. *Annals of Applied Probability, 1*(4), 504-512. (Discusses related estimators)
