# ULTOSC: Ultimate Oscillator

[Pine Script Implementation of ULTOSC](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/ultosc.pine)

## Overview and Purpose

The Ultimate Oscillator (ULTOSC), developed by Larry Williams in 1976, is a momentum oscillator designed to capture momentum across three different timeframes. It measures a weighted average of three oscillators, each using a different time period (short, medium, and long). This multi-timeframe approach aims to reduce the volatility and false trading signals that can occur with single-period oscillators by providing a smoother and more reliable momentum reading.

The oscillator ranges from 0 to 100, with traditional overbought and oversold levels typically set at 70 and 30, respectively.

## Core Concepts

*   **Multi-Timeframe Momentum:** Combines short, medium, and long-term momentum.
*   **Weighted Averaging:** Gives more significance to shorter-term momentum.
*   **Buying Pressure & True Range:** Uses these concepts for its internal calculations.
*   **Overbought/Oversold Levels:** Identifies potential market extremes.
*   **Divergence Analysis:** Signals potential trend reversals when price and oscillator diverge.

## Common Settings and Parameters

| Parameter   | Default | Function                                       | When to Adjust                                                                 |
| :---------- | :------ | :--------------------------------------------- | :----------------------------------------------------------------------------- |
| `shortLen`  | 7       | The shortest lookback period for calculation.  | Shorter for more sensitivity to recent price changes, longer for smoother signals. |
| `mediumLen` | 14      | The medium lookback period for calculation.    | Standard intermediate period, adjust in conjunction with short and long lengths. |
| `longLen`   | 28      | The longest lookback period for calculation.   | Longer for a broader view of momentum, shorter for more responsiveness.        |

**Pro Tip:** The default settings (7, 14, 28) are commonly used. Traders might experiment with other combinations, such as doubling (e.g., 5, 10, 20 or 10, 20, 40), ensuring that `shortLen < mediumLen < longLen`. The choice often depends on the asset's volatility and the trading timeframe.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Ultimate Oscillator calculates buying pressure relative to the true range over three distinct periods. These individual period calculations are then combined using specific weights to produce a single oscillator value.

**Technical formula:**

1.  **Buying Pressure (BP):**
    `BP = Close - TrueLow`
    Where `TrueLow = min(Low, Previous Close)`

2.  **True Range (TR):**
    `TR = TrueHigh - TrueLow`
    Where `TrueHigh = max(High, Previous Close)`

3.  **Sum of Buying Pressure and True Range over three periods (Short, Medium, Long):**
    For each period `len` (e.g., `shortLen`, `mediumLen`, `longLen`):
    *   `SumBP_len = Sum of BP over period len`
    *   `SumTR_len = Sum of TR over period len`

4.  **Average Ratios for each period:**
    *   `Avg_Short = SumBP_shortLen / SumTR_shortLen` (if `SumTR_shortLen` is not 0)
    *   `Avg_Medium = SumBP_mediumLen / SumTR_mediumLen` (if `SumTR_mediumLen` is not 0)
    *   `Avg_Long = SumBP_longLen / SumTR_longLen` (if `SumTR_longLen` is not 0)

5.  **Ultimate Oscillator (ULTOSC):**
    `ULTOSC = 100 * ( (4 * Avg_Short) + (2 * Avg_Medium) + (1 * Avg_Long) ) / (4 + 2 + 1)`

The weights (4 for short, 2 for medium, 1 for long) emphasize the shorter-term momentum.

> 🔍 **Technical Note:** This implementation uses an efficient circular buffer method for calculating the sums (`SumBP` and `SumTR`) for each period, ensuring good performance without relying on built-in `ta.sum()` for the core logic.

## Interpretation Details

The Ultimate Oscillator provides signals in several ways:

*   **Overbought/Oversold Conditions:**
    *   Readings above 70 suggest potentially overbought conditions.
    *   Readings below 30 suggest potentially oversold conditions.
    *   Trades are often considered when the oscillator moves out of these extreme zones.

*   **Divergence:**
    *   **Bullish Divergence:** Price makes a new low, but ULTOSC forms a higher low. This can indicate waning selling momentum and a potential upward reversal. A buy signal is often considered when the ULTOSC then breaks above the high point of the divergence.
    *   **Bearish Divergence:** Price makes a new high, but ULTOSC forms a lower high. This can indicate waning buying momentum and a potential downward reversal. A sell signal is often considered when the ULTOSC then breaks below the low point of the divergence.

*   **Trend Confirmation:** During an uptrend, the oscillator tends to stay above 40-50. During a downtrend, it tends to stay below 50-60.

## Limitations and Considerations

*   **Whipsaws:** Like many oscillators, ULTOSC can produce false signals (whipsaws), especially in choppy or non-trending markets.
*   **Fixed Levels:** The standard 70/30 overbought/oversold levels may not be optimal for all market conditions or assets. Some traders adjust these levels or use dynamic levels.
*   **Lag:** While designed to be more responsive than some oscillators, it still has an inherent lag due to its calculation based on past data.
*   **Strong Trends:** In very strong trending markets, the oscillator can remain in overbought or oversold territory for extended periods, making these signals less reliable for pinpointing reversals. Divergence signals may become more critical in such environments.
*   **Context is Key:** ULTOSC is best used in conjunction with other technical analysis tools, such as trend analysis, support/resistance levels, and price patterns, rather than in isolation.

## References

*   Williams, L. (1985). *How I Made $1,000,000 Trading Commodities Last Year*. Windsor Books. (Original concept often cited to his earlier work/seminars around 1976-1978).
*   Achelis, S. B. (2001). *Technical Analysis from A to Z*. McGraw-Hill.
*   [Ultimate Oscillator - Investopedia](https://www.investopedia.com/terms/u/ultimateoscillator.asp)
*   [Ultimate Oscillator - Wikipedia](https://en.wikipedia.org/wiki/Ultimate_oscillator)
