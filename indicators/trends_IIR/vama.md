# VAMA: Volatility Adjusted Moving Average

[Pine Script Implementation of VAMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/vama.pine)

## Overview and Purpose

The Volatility Adjusted Moving Average (VAMA) is an adaptive indicator that automatically adjusts its calculation period based on current market volatility conditions. Unlike traditional moving averages with fixed periods, VAMA dynamically shortens during high volatility periods to respond more quickly to price changes, and lengthens during low volatility periods to provide greater smoothing and reduce false signals. This adaptive behavior makes VAMA particularly effective across different market conditions without requiring manual parameter adjustments from traders.

## Core Concepts

* **Volatility adaptation:** Automatically adjusts the effective MA length based on the ratio of long-term to short-term volatility
* **ATR-based measurement:** Uses Average True Range (ATR) to quantify market volatility objectively
* **Dynamic responsiveness:** More responsive during trending (high volatility) markets, smoother during ranging (low volatility) markets
* **Self-adjusting:** Eliminates the need for traders to manually change MA periods as market conditions shift

The fundamental principle behind VAMA is that different market conditions require different levels of smoothing. During high volatility periods when prices are moving rapidly, a shorter MA period captures trend changes more quickly. During low volatility or consolidation phases, a longer MA period filters out noise and reduces whipsaws.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Base Length | 20 | Starting point for length calculation | Increase for slower base response, decrease for faster |
| Short ATR Period | 10 | Current volatility measurement window | Decrease for more sensitive volatility detection |
| Long ATR Period | 50 | Reference volatility measurement window | Increase for more stable volatility baseline |
| Min Length | 5 | Minimum allowed adjusted length | Prevent over-responsiveness in extreme volatility |
| Max Length | 100 | Maximum allowed adjusted length | Cap smoothing during very low volatility |
| Source | close | Price data used for calculation | Consider using hlc3 for smoother input |

**Pro Tip:** The ratio between Short ATR Period and Long ATR Period determines sensitivity to volatility changes. A wider ratio (e.g., 10:50) provides more stable adaptation, while a narrower ratio (e.g., 10:20) makes VAMA more reactive to volatility shifts.

## Calculation and Mathematical Foundation

**Simplified explanation:**
VAMA compares recent volatility (short-term ATR) to longer-term volatility (long-term ATR). When current volatility is high relative to the baseline, it shortens the moving average period. When current volatility is low, it lengthens the period. The adjusted-length MA is then calculated on the price data.

**Technical formula:**

1. Calculate volatility ratio:
   ```
   Volatility_Ratio(t) = Long_Term_ATR(t) / Short_Term_ATR(t)
   ```

2. Calculate adjusted length:
   ```
   Adjusted_Length(t) = Base_Length × Volatility_Ratio(t)
   Adjusted_Length(t) = clamp(Adjusted_Length(t), Min_Length, Max_Length)
   ```

3. Calculate VAMA:
   ```
   VAMA(t) = SMA(Price, Adjusted_Length(t))
   ```

Where:
- Long_Term_ATR is calculated over a longer period (e.g., 50 bars)
- Short_Term_ATR is calculated over a shorter period (e.g., 10 bars)
- Base_Length is the nominal MA period (e.g., 20)
- clamp() constrains the value between Min_Length and Max_Length

> 🔍 **Technical Note:** When Short_Term_ATR > Long_Term_ATR (indicating increased volatility), the ratio becomes less than 1, reducing the adjusted length and making VAMA more responsive. Conversely, when Short_Term_ATR < Long_Term_ATR (decreased volatility), the ratio exceeds 1, increasing the adjusted length for greater smoothing.

## Interpretation Details

VAMA can be used in various trading strategies:

* **Adaptive trend following:** VAMA automatically adjusts to market conditions, staying close to price during trends and providing smoother signals during consolidation
* **Dynamic support/resistance:** The adaptive nature makes VAMA a more reliable dynamic support/resistance level across varying market conditions
* **Crossover signals:** Price crossovers with VAMA generate signals that are naturally filtered by volatility - more responsive in trending markets, fewer false signals in ranging markets
* **Multi-timeframe confirmation:** Using VAMA on multiple timeframes provides volatility-adjusted trend confirmation
* **Volatility regime identification:** The displayed adjusted length and volatility ratio help identify current market volatility regimes

## Practical Applications

* **High volatility periods:** When adjusted length is near Min_Length, VAMA signals that the market is in a high-volatility trending phase - signals are more responsive but may require wider stops
* **Low volatility periods:** When adjusted length approaches Max_Length, VAMA indicates ranging or consolidating conditions - expect fewer signals but with potentially higher reliability
* **Volatility transitions:** Sharp changes in the adjusted length can signal transitions between market regimes, alerting traders to adjust their strategies
* **Comparison with fixed MA:** Enabling "Show Base SMA" allows visual comparison between adaptive and fixed-period moving averages, highlighting VAMA's adaptive advantage

## Limitations and Considerations

* **Market conditions:** Like all MA-based indicators, VAMA may generate whipsaws during choppy markets, though less frequently than fixed-period MAs
* **Lagging indicator:** Despite its adaptive nature, VAMA still lags price action and won't predict reversals
* **Parameter sensitivity:** The choice of Short and Long ATR periods significantly affects behavior - testing is recommended for specific markets
* **Volatility definition:** VAMA's effectiveness depends on ATR accurately representing "true" market volatility for the asset being traded
* **Extreme conditions:** During flash crashes or extreme volatility spikes, the min/max length constraints may limit adaptability
* **Complementary tools:** Best used with momentum indicators, volume analysis, or other trend confirmation tools

## References

* Chande, Tushar S. and Kroll, Stanley. "The New Technical Trader." Wiley, 1994
* Kaufman, Perry J. "Trading Systems and Methods." Wiley, 2013
* Wilder, J. Welles. "New Concepts in Technical Trading Systems." Trend Research, 1978 (for ATR)
