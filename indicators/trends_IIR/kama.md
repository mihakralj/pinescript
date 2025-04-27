# KAMA: Kaufman's Adaptive Moving Average

[Pine Script Implementation of KAMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/kama.pine)

## Overview and Purpose

Kaufman's Adaptive Moving Average (KAMA) is an intelligent technical indicator that automatically adjusts its sensitivity based on market conditions. Developed by Perry Kaufman in the 1990s and introduced in his 1995 book "Smarter Trading," KAMA was designed to solve the fundamental problem of traditional moving averages: their inability to adapt to changing market conditions.

KAMA provides a solution by becoming more responsive during trending markets and more stable during sideways or choppy conditions. This self-adjusting behavior makes it particularly valuable for traders who need a single moving average that can effectively handle different market environments without manual parameter changes.

## Core Concepts

* **Efficiency Ratio:** Measures the directional movement relative to volatility, determining how much the indicator should adapt to price changes
* **Market adaptation:** Automatically adjusts sensitivity based on current price behavior rather than using fixed parameters
* **Non-linear response:** Uses squared smoothing constant to emphasize differences between trending and non-trending market states
* **Timeframe flexibility:** Performs effectively across multiple timeframes with the same parameter settings

KAMA achieves its adaptive nature by calculating an "Efficiency Ratio" (ER) that measures how efficiently price is moving in one direction compared to overall volatility. When price is trending strongly (high ER), KAMA becomes more responsive; when price is moving sideways (low ER), KAMA becomes more stable.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 10 | Controls the lookback window for the Efficiency Ratio | Increase for less sensitivity to short-term trends, decrease for more reactive signals |
| Fast EMA | 2 | Sets the responsiveness during strong trends | Ranges from 2-4, lower values create faster response |
| Slow EMA | 30 | Sets the stability during weak trends | Ranges from 20-50, higher values create more smoothing |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** Unlike with other indicators, most professional traders rarely adjust KAMA parameters significantly from the defaults, as the adaptive nature of KAMA is designed to handle different market conditions automatically.

## Calculation and Mathematical Foundation

**Simplified explanation:**
KAMA works by measuring how efficiently price is moving in one direction compared to overall volatility. It then adjusts its smoothing factor accordingly - becoming more responsive during clear trends and more stable during choppy conditions.

**Technical formula:**
1. Calculate Efficiency Ratio (ER):
   - Directional Change = |Price(current) - Price(current - period)|
   - Volatility = Sum of |Price(i) - Price(i-1)| for i from (current - period + 1) to current
   - ER = Directional Change / Volatility

2. Calculate Smoothing Constant (SC):
   - SC = [ER × (FastSC - SlowSC) + SlowSC]²
   - FastSC = 2/(Fast+1)
   - SlowSC = 2/(Slow+1)

3. Apply KAMA formula:
   - KAMA(current) = KAMA(previous) + SC × (Price - KAMA(previous))

> 🔍 **Technical Note:** The squared smoothing factor creates a non-linear response curve that enhances adaptivity. When ER = 1 (perfect trend), SC = FastSC²; when ER = 0 (pure noise), SC = SlowSC². This non-linear scaling significantly amplifies the difference between trending and non-trending states.

## Interpretation Details

KAMA provides several key insights for traders:

- When price consistently stays above KAMA, it confirms an uptrend
- When price consistently stays below KAMA, it confirms a downtrend
- When KAMA's slope is steep, it indicates a strong trend
- When KAMA flattens, it suggests the trend is weakening or consolidation is occurring
- KAMA crossovers with price often signal potential trend changes
- When KAMA barely moves despite price fluctuations, it indicates the market is in a choppy, non-trending state

KAMA is particularly valuable for trend-following strategies in markets that alternate between trending and consolidating phases. Its adaptive nature helps filter out minor fluctuations during sideways markets while remaining responsive to genuine breakouts.

## Limitations and Considerations

* **Market conditions:** Despite its adaptive nature, KAMA may still produce whipsaws during highly volatile, directionless markets
* **Lag factor:** While more responsive than traditional MAs during trends, KAMA can be slower to recognize new trends after extended consolidation
* **Parameter sensitivity:** The initial selection of fast/slow parameters influences overall behavior despite its adaptive design
* **Calculation complexity:** More computationally intensive than simple moving averages
* **Complementary tools:** Works best when combined with volume analysis and momentum indicators for confirmation

## References

1. Kaufman, P. (1995). *Smarter Trading*. McGraw-Hill.
2. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
3. Kaufman, P. (1998). "Adaptive Moving Averages," *Technical Analysis of Stocks & Commodities*.
