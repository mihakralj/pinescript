# HURST: Hurst Exponent

[Pine Script Implementation of HURST](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/hurst.pine)

## Overview and Purpose

The Hurst Exponent (H) is a statistical measure developed by Harold Edwin Hurst while studying reservoir capacities on the Nile River. It quantifies the degree of long-term memory or persistence in a time series. In financial markets, the Hurst Exponent helps determine whether a series is trending (persistent), mean-reverting (anti-persistent), or a random walk. This makes it a valuable tool for market regime identification and strategy selection.

The indicator typically ranges between 0 and 1. A value of H close to 0.5 suggests a random walk, H > 0.5 indicates persistence, and H < 0.5 suggests anti-persistence.

## Core Concepts

*   **Long-Term Memory:** Measures the tendency of past price movements to influence future movements.
*   **Persistence (Trending):** An H value greater than 0.5 suggests that what happened in the past is likely to continue (e.g., an up-move is likely followed by another up-move).
*   **Anti-Persistence (Mean-Reversion):** An H value less than 0.5 suggests that what happened in the past is likely to reverse (e.g., an up-move is likely followed by a down-move).
*   **Random Walk:** An H value of approximately 0.5 indicates that past movements have no predictive power for future movements.
*   **Rescaled Range (R/S) Analysis:** The most common method for estimating the Hurst Exponent, which this implementation uses.

## Common Settings and Parameters

| Parameter | Type         | Default | Function                                       | When to Adjust                                                                 |
| :-------- | :----------- | :------ | :--------------------------------------------- | :----------------------------------------------------------------------------- |
| source    | series float | close   | Input time series (e.g., closing prices).      | Use other price points like `hlc3` for different perspectives if needed.       |
| length    | int          | 100     | Lookback period for Hurst Exponent calculation. | Shorter lengths (e.g., 50) are more responsive but noisier; longer lengths (e.g., 200) are smoother but lag more. Min 22 for this implementation. |

**Pro Tip:** While the Hurst Exponent provides insights into market memory, it's often beneficial to observe its behavior over time rather than relying on a single value. A rising H might indicate strengthening persistence, while a falling H could signal a shift towards randomness or mean-reversion.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Hurst Exponent is found by looking at how the range of price movements (adjusted for volatility) changes as we look at different time scales. If this "rescaled range" grows faster than it would for a random series, it indicates persistence (trending). If it grows slower, it indicates anti-persistence (mean-reversion). The exponent H quantifies this rate of growth.

**Technical formula (Rescaled Range - R/S - Analysis):**

1.  **Calculate Log Returns:** For the input `source` series of total length `L` (defined by the `length` parameter):
    `log_ret[t] = log(source[t] / source[t-1])`
2.  **Divide into Sub-periods:** The `log_ret` series is analyzed over various sub-period lengths `n`. This implementation uses `n` from `min_n = 10` up to `max_n = L / 2`.
3.  **For each sub-period of length `n`:**
    a.  Calculate the mean (`sub_mean`) of the `log_ret` values within this sub-period.
    b.  Create a mean-adjusted series: `dev[k] = log_ret[k] - sub_mean`.
    c.  Calculate the cumulative sum of these deviations (the "profile"): `Y[k] = Σ dev[j] for j=1 to k`.
    d.  Determine the Range (R) of this profile: `R = max(Y) - min(Y)`.
    e.  Calculate the Standard Deviation (S) of the `log_ret` values within this sub-period.
    f.  Compute the Rescaled Range: `R/S`.
4.  **Average R/S:** For each sub-period length `n`, average all `R/S` values obtained from the non-overlapping sub-periods of that length. This gives `(R/S)_n`.
5.  **Estimate H:** The Hurst Exponent H is estimated as the slope of the line when plotting `log((R/S)_n)` on the y-axis against `log(n)` on the x-axis. This is done via linear regression.
    The relationship is `(R/S)_n ≈ c * n^H`, so `log((R/S)_n) ≈ log(c) + H * log(n)`.

> 🔍 **Technical Note:** This implementation uses a direct calculation for the linear regression slope. The minimum `length` of 22 is required to ensure at least two distinct `n` values for the regression when `min_n` is 10. The quality of the Hurst estimate generally improves with longer `length` and a wider range of `n` values.

## Interpretation Details

The Hurst Exponent value provides insights into the nature of the time series:

*   **H > 0.5 (Persistent / Trending):**
    *   Indicates that the series has positive autocorrelation or long-term memory.
    *   Past trends are likely to continue. For example, if prices have been rising, they are more likely to continue rising.
    *   Values closer to 1.0 suggest stronger persistence.
    *   Trend-following strategies may be more effective in such regimes.
*   **H < 0.5 (Anti-persistent / Mean-Reverting):**
    *   Indicates negative autocorrelation. The series covers less "distance" than a random walk.
    *   Past trends are likely to reverse. If prices have been rising, they are more likely to fall, and vice-versa.
    *   Values closer to 0 suggest stronger anti-persistence.
    *   Mean-reversion strategies (e.g., using oscillators, trading ranges) may be more effective.
*   **H ≈ 0.5 (Random Walk):**
    *   Indicates that the series behaves like a geometric Brownian motion.
    *   Past price movements have no significant influence on future movements.
    *   Predicting future direction based on past trends is difficult. This aligns with the Efficient Market Hypothesis for many assets.

A common practice is to plot a horizontal line at H=0.5 to easily distinguish between these regimes.

## Common Applications

1.  **Market Regime Identification:** Helps traders understand if a market is currently trending, mean-reverting, or random.
2.  **Strategy Selection:** Guides the choice of trading strategies (e.g., trend-following if H > 0.55, mean-reversion if H < 0.45).
3.  **Risk Management:** Understanding the persistence of volatility or price trends can inform risk models.
4.  **Algorithmic Trading:** Can be used as an input for adaptive trading systems that switch strategies based on the estimated H value.
5.  **Detecting Market Inefficiencies:** Deviations from H=0.5 might suggest periods of predictability or inefficiency.

## Limitations and Considerations

*   **Estimation Challenges:** The Hurst Exponent is an estimate, and its accuracy can be affected by the length of the data series, the choice of sub-period divisions (`n`), and noise in the data.
*   **Sensitivity to `length`:** The calculated H value can vary significantly with the `length` parameter. It's often useful to test different lengths.
*   **Non-Stationarity:** Financial time series are often non-stationary (their statistical properties change over time). The Hurst Exponent assumes some level of underlying stationarity in the process generating the series, or at least that the "memory" characteristic is stable over the `length` period.
*   **Lag:** Being calculated over a lookback period, the Hurst Exponent will inherently lag in reflecting changes in market character.
*   **Computational Cost:** The R/S analysis method, especially with many sub-period divisions, can be computationally intensive.
*   **Interpretation Nuance:** An H value slightly above or below 0.5 doesn't guarantee strong trending or mean-reverting behavior. The deviation from 0.5 should be statistically significant, which is hard to assess in real-time trading.

## References

*   Hurst, H. E. (1951). "Long-term storage capacity of reservoirs". *Transactions of the American Society of Civil Engineers*, 116, 770-808.
*   Mandelbrot, B.B., & Wallis, J.R. (1969). "Some long-run properties of geophysical records". *Water Resources Research*, 5(2), 321-340. (Further development of R/S analysis).
*   Peters, E. E. (1994). *Fractal Market Analysis: Applying Chaos Theory to Investment and Economics*. John Wiley & Sons.
*   Lo, A. W. (1991). "Long-term memory in stock market prices". *Econometrica*, 59(5), 1279-1313. (Critiques and proposes a modified R/S statistic).
