# EWMA: Exponential Weighted Moving Average Volatility

[Pine Script Implementation of EWMA Volatility](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/ewma.pine)

## Overview and Purpose

The Exponential Weighted Moving Average (EWMA) Volatility, often referred to as RiskMetrics volatility, is a widely used model for forecasting financial market volatility. It assigns exponentially decreasing weights to past squared log returns, meaning more recent observations have a greater impact on the volatility estimate. This makes it more responsive to recent market shocks compared to a simple historical volatility calculated with equal weights.

The primary purpose of EWMA Volatility is to provide a dynamic measure of market risk. It's commonly used in risk management, derivatives pricing, and portfolio optimization. The model assumes that volatility is time-varying and tends to cluster, meaning periods of high volatility are often followed by more high volatility, and vice-versa.

## Core Concepts

*   **Log Returns:** Volatility is typically calculated based on the standard deviation of logarithmic returns, as log returns are time-additive and better approximate a normal distribution for asset prices.
*   **Squared Returns:** The model uses squared log returns as a proxy for variance.
*   **Exponential Smoothing (RMA/Wilder's MA):** An exponentially weighted moving average (specifically, a Recursive Moving Average or Wilder's MA in this implementation) is applied to the series of squared log returns. This gives more weight to recent data.
*   **Square Root:** The volatility is the square root of the EWMA of squared returns.
*   **Annualization:** The resulting volatility figure is often annualized by multiplying it by the square root of the number of trading periods in a year (e.g., 252 for daily data).

## Common Settings and Parameters

| Parameter     | Default | Function                                                                 | When to Adjust                                                                                                |
|---------------|---------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `src`         | `close` | Source price series for calculating log returns.                         | Use `hlc3` or `ohlc4` for a more comprehensive daily price measure if desired.                                |
| `length`      | 20      | The lookback period for the exponential smoothing (RMA).                 | Shorter periods (e.g., 10-20) make it more reactive; longer periods (e.g., 30-60) make it smoother.           |
| `annualize`   | `true`  | Whether to annualize the volatility output.                              | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                |
| `annualPeriods`| 252     | Number of trading periods in a year for annualization.                   | Adjust based on data frequency (e.g., 252 for daily, 52 for weekly, 12 for monthly, 365 for calendar days). |

**Pro Tip:** The `length` parameter in EWMA is analogous to the decay factor (lambda) often seen in RiskMetrics literature, where `lambda = (length - 1) / length`. A common `length` of 20 corresponds to a lambda of 0.95, and a `length` of 25 corresponds to lambda of 0.96.

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  Calculate the daily logarithmic return of the price series.
2.  Square these log returns.
3.  Apply an Exponential Moving Average (specifically, a Wilder's MA or RMA) to the series of squared log returns.
4.  Take the square root of this smoothed series of squared returns to get the per-period volatility.
5.  (Optional) Annualize by multiplying by the square root of the number of trading periods in a year.

**Technical formula:**

Let $r_t = \ln(P_t / P_{t-1})$ be the log return at time $t$.
Let $r_t^2$ be the squared log return.

The EWMA of squared returns (variance, $\sigma_t^2$) is calculated using a Recursive Moving Average (RMA), which is equivalent to an EMA with $\alpha = 1/\text{length}$:
$\sigma_t^2 = (1 - \alpha) \cdot \sigma_{t-1}^2 + \alpha \cdot r_t^2$
Or, using the `length` directly in RMA form:
$\sigma_t^2 = (\sigma_{t-1}^2 \cdot (\text{length} - 1) + r_t^2) / \text{length}$

The EWMA Volatility ($v_t$) is then:
$v_t = \sqrt{\sigma_t^2}$

If annualizing:
Annualized $v_t = v_t \cdot \sqrt{\text{AnnualPeriods}}$

> 🔍 **Technical Note:** The Pine Script implementation uses a bias-corrected RMA to ensure accurate values from the beginning of the series, mitigating the warm-up effect common in standard EMA/RMA calculations.

## Interpretation Details

*   **Rising EWMA Volatility:** Indicates increasing market risk and uncertainty. Price swings are expected to be larger.
*   **Falling EWMA Volatility:** Suggests decreasing market risk and more stable conditions. Price swings are expected to be smaller.
*   **Absolute Level:** The absolute value of EWMA Volatility can be used to set volatility-adjusted position sizes or stop-loss levels. For example, a stock with 30% annualized volatility is riskier than one with 15%.
*   **Volatility Clustering:** EWMA Volatility captures the phenomenon of volatility clustering, where high-volatility periods tend to be followed by high-volatility periods, and low by low.

## Limitations and Considerations

*   **Lag:** Being a moving average-based indicator, it will inherently lag behind very sudden spikes in volatility.
*   **Symmetry:** EWMA Volatility treats positive and negative returns symmetrically (due to squaring returns), so it doesn't distinguish between upside and downside volatility. For asymmetric effects, models like GJR-GARCH might be considered.
*   **No Mean Reversion:** The basic EWMA model (like RiskMetrics) assumes no long-term mean reversion in volatility, which might not always hold true. GARCH models incorporate mean reversion.
*   **Choice of `length` (Decay Factor):** The choice of `length` significantly impacts responsiveness. There's no universally optimal value; it often depends on the asset and analysis horizon.
*   **Assumption of Normality (for log returns):** While log returns are often closer to normal than simple returns, financial returns frequently exhibit fat tails (leptokurtosis), which EWMA might not fully capture.

## References

*   J.P. Morgan/Reuters (1996). *RiskMetrics™ — Technical Document*. Fourth Edition.
*   Hull, J. C. (2018). *Options, Futures, and Other Derivatives*. Pearson Education Limited. (Chapter on Estimating Volatilities and Correlations)
*   Poon, S.-H. (2005). *A Practical Guide to Forecasting Financial Market Volatility*. Wiley.
