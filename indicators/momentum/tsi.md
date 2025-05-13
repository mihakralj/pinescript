# TSI: True Strength Index

[Pine Script Implementation of TSI](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/tsi.pine)

## Overview and Purpose

The True Strength Index (TSI) is a momentum oscillator developed by William Blau and introduced in *Technical Analysis of Stocks & Commodities* magazine. It is designed to show both the trend direction and overbought/oversold conditions of a market by applying a double smoothing of price momentum. The TSI fluctuates between +100 and -100.

The TSI uses exponential moving averages (EMAs) to smooth the momentum of price changes and the absolute momentum of price changes. The ratio of these two smoothed values forms the TSI. A signal line, which is an EMA of the TSI itself, is often plotted alongside the TSI to generate trading signals.

## Core Concepts

*   **Double Smoothed Momentum:** Measures the momentum of price changes and then smooths this momentum twice using EMAs.
*   **Absolute Momentum Smoothing:** Similarly smooths the absolute values of price changes.
*   **Ratio of Smoothed Values:** The TSI is the ratio of the double-smoothed momentum to the double-smoothed absolute momentum, scaled by 100.
*   **Trend Indication:** Values above zero generally indicate bullish momentum, while values below zero indicate bearish momentum.
*   **Overbought/Oversold Levels:** Extreme readings (e.g., above +25 or below -25) can indicate overbought or oversold conditions.
*   **Signal Line Crossovers:** Crossovers between the TSI and its signal line can generate buy or sell signals.
*   **Divergence Analysis:** Divergences between price and the TSI can signal potential trend reversals.

## Common Settings and Parameters

| Parameter   | Default | Function                                                                 | When to Adjust                                                                                                |
| :---------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| `src`       | `close` | The source price series for calculations.                                | Can be changed to `hlc3`, `ohlc4`, etc., for different price representations.                               |
| `longLen`   | 25      | The lookback period for the first EMA smoothing of momentum.             | Longer periods result in a smoother TSI with less sensitivity; shorter periods increase sensitivity and noise. |
| `shortLen`  | 13      | The lookback period for the second EMA smoothing of momentum.            | Affects the responsiveness of the TSI. Typically shorter than `longLen`.                                      |
| `signalLen` | 13      | The lookback period for the EMA smoothing of the TSI to create the signal line. | Adjusts the sensitivity of the signal line. Shorter for faster signals, longer for fewer signals.             |

**Pro Tip:** The default settings (25, 13, 13) are common. Traders may adjust these based on the asset's volatility and their trading timeframe. For instance, shorter settings like (15, 8, 8) might be used for faster markets or shorter timeframes.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The TSI measures the underlying strength of price movement by comparing the smoothed momentum of price changes to the smoothed absolute momentum of price changes. This helps to filter out insignificant noise and focus on the true direction and strength of the trend.

**Technical formula:**

1.  **Price Change (Momentum):**
    `Mom = Current Source Price - Previous Source Price`

2.  **Absolute Price Change (Absolute Momentum):**
    `AbsMom = abs(Mom)`

3.  **First EMA Smoothing (Long Period):**
    *   `EMA_Mom_Long = EMA(Mom, longLen)`
    *   `EMA_AbsMom_Long = EMA(AbsMom, longLen)`

4.  **Second EMA Smoothing (Short Period):**
    *   `Double_EMA_Mom = EMA(EMA_Mom_Long, shortLen)`
    *   `Double_EMA_AbsMom = EMA(EMA_AbsMom_Long, shortLen)`

5.  **True Strength Index (TSI):**
    `TSI = 100 * (Double_EMA_Mom / Double_EMA_AbsMom)`
    (If `Double_EMA_AbsMom` is zero, TSI is typically set to 0 or the previous TSI value).

6.  **Signal Line:**
    `SignalLine = EMA(TSI, signalLen)`

> 🔍 **Technical Note:** This implementation uses custom compensated Exponential Moving Averages (EMAs) for each smoothing step. This method ensures higher accuracy, especially in the initial bars of the calculation, compared to standard EMA functions that might have a longer warmup period or slight discrepancies.

## Interpretation Details

The TSI can be interpreted in several ways:

*   **Centerline (Zero Line) Crossovers:**
    *   TSI crossing above zero: Bullish signal, indicating increasing positive momentum.
    *   TSI crossing below zero: Bearish signal, indicating increasing negative momentum.

*   **Signal Line Crossovers:**
    *   TSI crossing above its signal line: Potential buy signal.
    *   TSI crossing below its signal line: Potential sell signal.
    These are generally considered more timely than centerline crossovers but can also produce more false signals.

*   **Overbought/Oversold Levels:**
    *   While TSI is unbounded, levels like +25 and -25 are often used as overbought and oversold thresholds, respectively.
    *   Extreme readings (e.g., +40/-40 or higher/lower) suggest strong momentum that might be unsustainable.
    *   Exiting these zones can signal a potential reversal.

*   **Divergence:**
    *   **Bullish Divergence:** Price makes lower lows while TSI makes higher lows, suggesting weakening selling pressure.
    *   **Bearish Divergence:** Price makes higher highs while TSI makes lower highs, suggesting weakening buying pressure.

## Limitations and Considerations

*   **Whipsaws:** Like other oscillators, TSI can generate false signals, especially in sideways or choppy markets. Signal line crossovers are particularly prone to this.
*   **Lag:** Due to the double smoothing, the TSI can lag behind price action, especially with longer period settings.
*   **Parameter Sensitivity:** The behavior of the TSI is highly dependent on the chosen length parameters. Optimal settings can vary significantly between different assets and timeframes.
*   **Extreme Readings in Strong Trends:** In strongly trending markets, the TSI can remain in overbought or oversold territory for extended periods, making these levels less reliable for pinpointing exact reversal points.
*   **Combined Analysis:** TSI is most effective when used in conjunction with other forms of technical analysis, such as price patterns, trendlines, and other indicators.

## References

*   Blau, W. (1991). "True Strength Index (TSI)". *Technical Analysis of Stocks & Commodities*, V. 9:5 (May).
*   Hartle, T. (1991). "Interview: William Blau - True Strength Index". *Technical Analysis of Stocks & Commodities*, V. 9:5 (May).
*   Colby, R. W. (2003). *The Encyclopedia of Technical Market Indicators*. McGraw-Hill.
