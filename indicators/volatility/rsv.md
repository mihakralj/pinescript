# RSV: Rogers-Satchell Volatility

[Pine Script Implementation of RSV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/rsv.pine)

## Overview and Purpose

Rogers-Satchell Volatility (RSV) is a historical volatility estimator developed by L. C. G. Rogers and S. E. Satchell in 1991. It utilizes high, low, open, and close prices to estimate volatility. A key advantage of the Rogers-Satchell estimator is that it is unbiased even when the underlying asset price has a non-zero drift, unlike some other estimators like Parkinson Volatility which assume zero drift.

This makes RSV potentially more robust in trending markets. It aims to provide a more efficient estimate of volatility by incorporating more information from the price bar than simple close-to-close methods.

## Core Concepts

*   **OHLC Data:** Uses all four main price points of a period: Open, High, Low, and Close.
*   **Drift Independence:** The estimator is designed to be unbiased by the average trend (drift) of the asset price. This is a significant advantage over estimators that assume zero drift.
*   **Logarithmic Prices:** Calculations involve natural logarithms of price ratios.
*   **Efficiency:** Generally more efficient than close-to-close volatility and Parkinson volatility, especially in the presence of drift.
*   **Smoothing:** The per-period Rogers-Satchell variance is typically smoothed (e.g., using an SMA) over a lookback period before taking the square root to get volatility.
*   **Annualization:** The resulting per-period volatility is often annualized for comparability.

## Common Settings and Parameters

| Parameter       | Default | Function                                                                              | When to Adjust                                                                                                |
|-----------------|---------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `length`        | 20      | The lookback period for smoothing the Rogers-Satchell variance (e.g., using SMA).     | Shorter periods make RSV more reactive; longer periods provide a smoother, more stable measure.                 |
| `annualize`     | `true`  | Whether to annualize the volatility output.                                           | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                |
| `annualPeriods` | 252     | Number of trading periods in a year for annualization.                                | Adjust based on data frequency (e.g., 252 for daily, 52 for weekly, 365 for calendar day data if applicable). |

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  For each trading period, gather the High (H), Low (L), Open (O), and Close (C) prices.
2.  Calculate the following four terms using natural logarithms (ln):
    *   TermA = ln(High / Open)
    *   TermB = ln(High / Close)
    *   TermC = ln(Low / Open)
    *   TermD = ln(Low / Close)
    *(Note: The Pine Script implementation directly calculates these ratios. The original formula can also be expressed as differences of logs, e.g., ln(High) - ln(Open) for TermA).*
3.  Calculate the Rogers-Satchell variance for that single period:
    `RS_Variance_Period = (TermA * TermB) + (TermC * TermD)`
4.  Smooth this series of per-period variance estimates over the specified `length` (e.g., using a Simple Moving Average - SMA):
    `Smoothed_RS_Variance = SMA(RS_Variance_Period, length)`
5.  Take the square root of the smoothed variance to get the per-period Rogers-Satchell Volatility:
    `RSV_Period = SquareRoot(Smoothed_RS_Variance)`
6.  (Optional) If annualization is enabled, multiply the per-period volatility by the square root of the `annualPeriods`:
    `RSV_Annual = RSV_Period * SquareRoot(AnnualPeriods)`

**Conceptual Formula for a Single Period's Rogers-Satchell Variance:**

`RS_Variance = [ln(High) - ln(Open)] * [ln(High) - ln(Close)] + [ln(Low) - ln(Open)] * [ln(Low) - ln(Close)]`

Where:
*   `H` is the High price for the period.
*   `L` is the Low price for the period.
*   `O` is the Open price for the period.
*   `C` is the Close price for the period.
*   `ln` represents the natural logarithm.

**Indicator Calculation Steps:**
1.  Calculate `RS_Variance` for each period `i`.
2.  `Smoothed_RS_Variance = SMA(RS_Variance, length)`
3.  `RSV_Period = SquareRoot(Smoothed_RS_Variance)`
4.  `RSV_Annual = RSV_Period * SquareRoot(AnnualPeriods)` (if `annualize` is true)

## Interpretation Details

*   **Magnitude:** Higher RSV values indicate greater price volatility. Lower RSV values suggest less volatility.
*   **Comparison:** RSV can be compared to other volatility measures. Its strength lies in its robustness to drift.
*   **Trend in RSV:**
    *   **Rising RSV:** Suggests increasing volatility.
    *   **Falling RSV:** Suggests decreasing volatility.
*   **Comprehensive Bar Information:** By using O, H, L, and C, RSV captures more information about price movement within a bar than estimators relying on fewer points.

## Limitations and Considerations

*   **No Account for Gaps:** While it uses the open price, the original Rogers-Satchell estimator does not explicitly model or adjust for overnight gaps in the same way as the Yang-Zhang estimator. However, its use of open, high, low, and close makes it more robust to gaps than close-to-close or Parkinson.
*   **Data Quality:** Relies on accurate O, H, L, C prices. Errors in any of these can affect the estimate.
*   **Smoothing Lag:** The necessary smoothing introduces lag, common to most moving average-based indicators.
*   **Assumption of Continuous Trading:** The model implicitly assumes continuous trading within the bar (from Open to High/Low to Close).

## References

*   Rogers, L. C. G., & Satchell, S. E. (1991). Estimating Variance from High, Low, Open, and Closing Prices. *The Annals of Applied Probability, 1*(4), 504-512.
*   Yang, D., & Zhang, Q. (2000). Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices. *The Journal of Business, 73*(3), 477-491. (Often compared with Rogers-Satchell).
