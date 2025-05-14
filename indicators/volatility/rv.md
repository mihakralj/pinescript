# RV: Realized Volatility

[Pine Script Implementation of RV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/rv.pine)

## Overview and Purpose

Realized Volatility (RV) is an estimator of historical volatility calculated using high-frequency intraday data. Instead of relying on daily open, high, low, and close prices, RV sums the squared log returns of prices sampled at a higher frequency (e.g., every 5 minutes) within a given period (e.g., one day). The square root of this sum gives the realized volatility for that period.

This method is considered a more accurate measure of actual (realized) volatility compared to estimators based on lower-frequency data, as it captures more of the price path.

## Core Concepts

*   **High-Frequency Data:** Utilizes intraday price data (e.g., 1-minute, 5-minute closes) to calculate volatility for a higher timeframe bar (e.g., daily bar).
*   **Sum of Squared Log Returns:** The core of the calculation involves summing the squared logarithmic returns of the intraday prices.
*   **Model-Free (Theoretically):** In theory, as the sampling frequency approaches continuous time, realized volatility converges to the true integrated variance, making it a "model-free" estimator. In practice, market microstructure noise limits the usable sampling frequency.
*   **Smoothing:** The per-period realized volatility (e.g., daily RV) is often smoothed over a lookback period (e.g., using an SMA) to provide a more stable measure.
*   **Annualization:** The resulting smoothed volatility is typically annualized for comparability.

## Common Settings and Parameters

| Parameter           | Default | Function                                                                                                   | When to Adjust                                                                                                                               |
|---------------------|---------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `length`            | 20      | The lookback period for smoothing the per-period (e.g., daily) realized volatilities.                      | Shorter periods make RV more reactive; longer periods provide a smoother, more stable measure.                                                 |
| `intradayTimeframe` | "5"     | The lower timeframe string (e.g., "1", "5", "15", "60") from which to sample returns.                        | Choose based on data availability, liquidity, and desire to balance capturing true volatility vs. market microstructure noise. Common choices are 1-min to 15-min. Must be a lower timeframe than the chart. |
| `annualize`         | `true`  | Whether to annualize the volatility output.                                                                | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                                               |
| `annualPeriods`     | 252     | Number of main chart periods (e.g., days if chart is daily) in a year for annualization.                   | Adjust based on the main chart's timeframe (e.g., 252 for daily, 52 for weekly).                                                               |

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  For each bar on the main chart (e.g., a daily bar), obtain an array of close prices from the specified `intradayTimeframe` (e.g., 5-minute closes) that fall within that main chart bar.
2.  Calculate the logarithmic returns between consecutive intraday close prices:
    `log_return_intra = ln(intraday_close_current / intraday_close_previous)`
3.  Square each of these intraday log returns: `squared_log_return_intra = log_return_intra ^ 2`.
4.  Sum all these squared intraday log returns for the main chart bar. This sum is the realized variance for that period (e.g., day):
    `RealizedVariance_Period = Sum(squared_log_return_intra)`
5.  Take the square root of this `RealizedVariance_Period` to get the realized volatility for that period:
    `RealizedVolatility_Period = SquareRoot(RealizedVariance_Period)`
6.  Smooth this series of `RealizedVolatility_Period` values over the specified `length` (e.g., using SMA):
    `Smoothed_RV = SMA(RealizedVolatility_Period, length)`
7.  (Optional) If annualization is enabled, multiply the `Smoothed_RV` by the square root of `annualPeriods`:
    `RV_Annual = Smoothed_RV * SquareRoot(AnnualPeriods)`

**Conceptual Formula for a Single Period's Realized Variance:**

`RealizedVariance_T = Sum_from_i=1_to_N [ ln(P_i / P_{i-1}) ]^2`

Where:
*   `T` is the period of the main chart bar (e.g., one day).
*   `N` is the number of intraday intervals within period `T`.
*   `P_i` is the price at the end of the `i`-th intraday interval.
*   `ln` is the natural logarithm.

**Indicator Calculation Steps:**
1.  For each main chart bar, calculate `RealizedVolatility_Period` as described above.
2.  `Smoothed_RV = SMA(RealizedVolatility_Period, length)`
3.  `RV_Annual = Smoothed_RV * SquareRoot(AnnualPeriods)` (if `annualize` is true)

## Interpretation Details

*   **Magnitude:** Higher RV values indicate greater price volatility as captured by intraday price movements.
*   **Accuracy:** Generally considered a more accurate measure of actual volatility than methods based on daily OHLC data alone.
*   **Comparison:** Can be compared to implied volatility or other historical volatility measures to assess market expectations versus actual movements.
*   **Regime Identification:** Significant changes in RV levels can signal shifts in market volatility regimes.

## Limitations and Considerations

*   **Data Requirements:** Requires access to reliable intraday data. The quality and availability of this data are crucial.
*   **Market Microstructure Noise:** At very high sampling frequencies (e.g., tick data or sub-second), market microstructure effects (bid-ask bounce, price discreteness) can bias the RV estimator upwards. The choice of `intradayTimeframe` is a trade-off.
*   **Computational Intensity:** Can be more computationally intensive than simpler volatility measures due to fetching and processing intraday data.
*   **Limited Historical Data:** `request.security_lower_tf` in Pine Script™ has limitations on how much historical intraday data it can fetch, which might affect the indicator's history on very long charts or with very short intraday timeframes.
*   **Overnight Gaps:** This basic RV formulation sums intraday returns. It does not explicitly incorporate the overnight gap (close of previous main bar to open of current main bar) unless the intraday sampling starts from the open and ends at the close, effectively capturing the day's full range through intraday steps. Some advanced RV estimators add a term for the overnight return.

## References

*   Andersen, T. G., Bollerslev, T., Diebold, F. X., & Labys, P. (2001). The Distribution of Realized Exchange Rate Volatility. *Journal of the American Statistical Association, 96*(453), 42-55.
*   Barndorff-Nielsen, O. E., & Shephard, N. (2002). Econometric analysis of realized volatility and its use in estimating stochastic volatility models. *Journal of the Royal Statistical Society: Series B (Statistical Methodology), 64*(2), 253-280.
