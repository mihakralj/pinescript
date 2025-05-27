# UI: Ulcer Index

[Pine Script Implementation of UI](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/ui.pine)

## Overview and Purpose

The Ulcer Index (UI), developed by Peter Martin and Byron McCann, is a volatility indicator designed to measure downside risk. Unlike many other volatility measures that quantify total volatility (both upside and downside), the Ulcer Index specifically focuses on the depth and duration of price drawdowns from earlier highs. A higher Ulcer Index value indicates higher downside risk and suggests that the asset has experienced significant and/or prolonged price declines.

The primary purpose of the UI is to provide a measure of the "agony" or "ulcer-inducing" stress of holding an investment due to price declines. It's often used in portfolio management and risk assessment.

## Core Concepts

*   **Drawdown from Peak:** For each period, the index calculates how far the current price has fallen from the highest price observed over a preceding lookback period.
*   **Percentage Drawdown:** This drawdown is expressed as a percentage.
*   **Squared Drawdowns:** To emphasize larger drawdowns more significantly, these percentage drawdowns are squared.
*   **Averaging Squared Drawdowns:** The squared percentage drawdowns are then averaged over the lookback period.
*   **Square Root:** The Ulcer Index is the square root of this average. This brings the measurement back to a scale comparable to percentage drawdown.

## Common Settings and Parameters

| Parameter | Default | Description                                      | Typical Adjustments                                                                                                |
|-----------|---------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `src`     | `close` | The source price series used for calculations.   | Can be changed to `hlc3`, `ohlc4`, etc., though `close` is standard.                                               |
| `period`  | 14      | The lookback period for all calculations.        | Shorter periods make the UI more reactive to recent drawdowns; longer periods provide a smoother, longer-term view of downside risk. |

## Calculation Steps

The Ulcer Index is calculated as follows for each bar, looking back over `N` periods:

1.  **Identify Highest Price:** For the current bar `i`, find the highest `src` price over the last `N` bars (from `i-N+1` to `i`):
    `HighestPrice_N = Highest(src, N)`

2.  **Calculate Percentage Drawdown (D):**
    `D_i = ((src_i - HighestPrice_N) / HighestPrice_N) * 100`
    *(Note: This value will be negative or zero, representing the percentage drop from the N-period high.)*

3.  **Square the Percentage Drawdown:**
    `SquaredD_i = D_i^2`
    *(Squaring makes all values positive and gives greater weight to larger drawdowns.)*

4.  **Sum Squared Drawdowns:** Sum the `SquaredD_i` values over the last `N` periods:
    `SumSquaredD_N = Sum(SquaredD_i, N)` (for `i` from current bar back N-1 bars)

5.  **Calculate Average of Squared Drawdowns:**
    `AvgSquaredD_N = SumSquaredD_N / N`

6.  **Calculate Ulcer Index:**
    `UI = SquareRoot(AvgSquaredD_N)`

## Interpretation Details

*   **Magnitude:** The Ulcer Index is expressed as a percentage. A higher UI value indicates greater downside risk and more "ulcer-inducing" price behavior over the lookback period. For example, a UI of 10 suggests an average effective drawdown of 10% (considering the squaring and square root process).
*   **Low Values:** Low UI values (e.g., close to 0 or single digits) suggest that the asset has experienced minimal or very shallow drawdowns from its recent highs. This indicates low downside risk during the analyzed period.
*   **High Values:** High UI values (e.g., 20, 30, or more) indicate significant and/or prolonged drawdowns. This suggests a volatile investment on the downside and higher risk.
*   **Comparing Assets:** The UI can be used to compare the downside risk of different assets or investment strategies. An asset with a consistently lower UI might be preferred by risk-averse investors.
*   **Trend Analysis:**
    *   **Rising UI:** Indicates increasing downside risk and potentially a weakening trend or the beginning of a downtrend.
    *   **Falling UI:** Indicates decreasing downside risk, suggesting price stability or recovery from previous drawdowns. This can be seen in strengthening uptrends.
*   **Not an Overbought/Oversold Indicator:** Unlike oscillators like RSI, the Ulcer Index does not have typical overbought or oversold levels. Its absolute value is more important as a measure of risk.

## Limitations and Considerations

*   **Historical Measure:** The Ulcer Index is based on historical price data and does not predict future drawdowns.
*   **Focus on Downside Only:** It exclusively measures downside risk. An asset could have a low Ulcer Index but still be highly volatile on the upside.
*   **Sensitivity to Period:** The choice of the `period` significantly impacts the UI value. Shorter periods will make it more sensitive to short-term price dips, while longer periods will reflect longer-term drawdown characteristics.
*   **No Directional Signal for Entry/Exit:** While it quantifies risk, the UI itself doesn't typically provide direct buy or sell signals. It's more of a risk assessment tool to be used in conjunction with other indicators or strategies.

## References

*   Martin, P. G., & McCann, B. B. (1989). *The Investor's Guide to Fidelity Funds*. John Wiley & Sons.
*   The Ulcer Index was first described in their 1987 newsletter, *The Physician's Guide to Investing*.
