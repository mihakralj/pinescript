# RVI: Relative Volatility Index

[Pine Script Implementation of RVI](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/rvi.pine)

## Overview and Purpose

The Relative Volatility Index (RVI), developed by Donald Dorsey, is an oscillator designed to gauge the **direction of volatility**. It operates similarly to the Relative Strength Index (RSI), but instead of analyzing the magnitude of price changes, the RVI focuses on the standard deviation of prices to determine if volatility is more pronounced on up-trending or down-trending days. The RVI typically oscillates between 0 and 100.

The primary goal of the RVI is to help traders identify periods where the market's volatility shows a clear directional bias. Values above 50 generally suggest that volatility is stronger during upward price movements, while values below 50 indicate that volatility is more dominant during downward price movements.

## Core Concepts

*   **Standard Deviation of Prices:** The RVI's core input is the standard deviation of the source prices (e.g., closing prices) over a user-defined lookback period. This measures the dispersion of prices around their mean for that period.
*   **Directional Volatility Assignment:** This calculated standard deviation value is then attributed directionally. If the current price is higher than the previous price, the standard deviation value is considered "upward volatility" for that bar. If the current price is lower, it's considered "downward volatility." If prices are unchanged, neither is assigned for that bar.
*   **Smoothing:** These raw upward and downward volatility values are then smoothed, typically using a Wilder's Moving Average (RMA), over another user-defined period. This smoothing helps to reduce noise and highlight the prevailing trend in directional volatility.
*   **Oscillator Output:** The final RVI value is derived from the ratio of the smoothed upward volatility to the total smoothed volatility (upward + downward), scaled to oscillate between 0 and 100.

## Common Settings and Parameters

| Parameter     | Default | Description                                                                                                | Typical Adjustments                                                                                                                            |
|---------------|---------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `src`         | `close` | The source price series used for all calculations.                                                         | Can be changed to `hlc3`, `ohlc4`, etc., based on trader preference for what constitutes the "price."                                         |
| `stdevLength` | 10      | The lookback period for calculating the standard deviation of the `src` prices.                              | Shorter periods (e.g., 5-7) make the standard deviation more reactive; longer periods (e.g., 14-20) make it smoother and less sensitive.         |
| `rmaLength`   | 14      | The lookback period for the Wilder's Moving Average (RMA) used to smooth the directional volatility components. | Similar to RSI, 14 is a common default. Shorter periods make the RVI more responsive; longer periods result in a smoother, slower RVI line. |

## Calculation Steps

The RVI is calculated as follows:

1.  **Calculate Price Change:**
    `PriceChange_i = src_i - src_{i-1}`
    (where `_i` denotes the current bar and `_{i-1}` the previous bar)

2.  **Calculate Standard Deviation of Prices:**
    `StdDev_i = StandardDeviation(src, stdevLength)`
    (This is the standard deviation of the `src` series over the last `stdevLength` bars)

3.  **Determine Directional Standard Deviation for the Current Bar:**
    *   If `PriceChange_i > 0`:
        `UpStd_i = StdDev_i`
        `DownStd_i = 0`
    *   Else if `PriceChange_i < 0`:
        `DownStd_i = StdDev_i`
        `UpStd_i = 0`
    *   Else (`PriceChange_i = 0`):
        `UpStd_i = 0`
        `DownStd_i = 0`

4.  **Smooth Directional Standard Deviations:**
    `AvgUpStd = RMA(UpStd, rmaLength)`
    `AvgDownStd = RMA(DownStd, rmaLength)`
    (where `RMA` is Wilder's Moving Average)

5.  **Calculate the Relative Volatility Index:**
    `SumAvgStd = AvgUpStd + AvgDownStd`
    If `SumAvgStd` is not equal to 0:
    `RVI = 100 * (AvgUpStd / SumAvgStd)`
    Else (if `SumAvgStd` is 0, which is rare but possible if prices are flat for an extended period):
    `RVI = 50` (neutral value)

## Interpretation Details

*   **Oscillator Range:** RVI values fluctuate between 0 and 100.
*   **Center Line (50):**
    *   **Above 50:** Suggests that volatility has been predominantly on the upside. This can indicate bullish sentiment or stronger conviction in upward price movements.
    *   **Below 50:** Suggests that volatility has been predominantly on the downside. This can indicate bearish sentiment or stronger conviction in downward price movements.
    *   **Crossing 50:** A cross of the 50-line can signal a potential shift in the directional bias of volatility. A decisive cross above 50 might support a bullish outlook, while a cross below 50 might support a bearish one.
*   **Overbought/Oversold Levels (Subjective):**
    *   **High Readings (e.g., > 70 or > 80):** Traditionally considered "overbought" in terms of upward volatility dominance. It suggests that upward volatility has been strong and might be due for a consolidation or reversal. However, in strong uptrends, RVI can remain high.
    *   **Low Readings (e.g., < 30 or < 20):** Traditionally considered "oversold" in terms of downward volatility dominance. It suggests that downward volatility has been strong and might be exhausted. In strong downtrends, RVI can remain low.
    *   *Note: These levels are not definitive and should be adapted to the specific asset and market conditions.*
*   **Divergence:**
    *   **Bullish Divergence:** Price makes a new low, but RVI forms a higher low. This can indicate weakening bearish momentum and a potential upward reversal.
    *   **Bearish Divergence:** Price makes a new high, but RVI forms a lower high. This can indicate weakening bullish momentum and a potential downward reversal.
*   **Trend Confirmation:**
    *   In an established uptrend, RVI tends to remain above 50.
    *   In an established downtrend, RVI tends to remain below 50.
    *   Movement away from extreme levels towards 50 can sometimes signal a weakening trend.

## Limitations and Considerations

*   **Lag:** Being based on moving averages (RMA for smoothing), the RVI will inherently lag behind price action, especially with longer `rmaLength` settings.
*   **Whipsaws:** In non-trending, choppy, or sideways markets, the RVI can generate frequent and potentially misleading signals as it oscillates around the 50 level.
*   **Nature of Standard Deviation Used:** The RVI, as per Dorsey's refined method, uses the standard deviation of *prices* over the `stdevLength` period. This measures price dispersion around a mean. It's then assigned directionally. This is different from using the standard deviation of *price changes (returns)*, which some might intuitively expect for a volatility measure.
*   **Not a Pure Volatility Magnitude Indicator:** While "volatility" is in its name, the RVI is primarily an oscillator indicating the *direction* or *bias* of volatility, rather than its absolute level or magnitude (like ATR or Historical Volatility would show).
*   **Parameter Sensitivity:** The RVI's behavior is sensitive to the `stdevLength` and `rmaLength` parameters. Traders should experiment to find settings that suit their trading style and the characteristics of the traded asset.

## References

*   Dorsey, D. (1993). The RVI: A New Oscillator. *Technical Analysis of Stocks & Commodities Magazine, 11*(1), 26-30.
*   Dorsey, D. (1995). Refining the RVI. *Technical Analysis of Stocks & Commodities Magazine, 13*(9), 380-384. (The implemented script aligns with this refined version).
