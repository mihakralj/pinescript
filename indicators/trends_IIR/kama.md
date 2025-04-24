# Kaufman's Adaptive Moving Average (KAMA)

## Historical Background

Kaufman's Adaptive Moving Average was developed by Perry Kaufman in the 1990s and introduced in his 1995 book "Smarter Trading." Unlike traditional moving averages with fixed parameters, KAMA was designed to automatically adjust its sensitivity based on market conditions.

Kaufman created KAMA after years of studying various trading systems across different markets. His approach was inspired by earlier adaptive techniques but innovated by creating a formula that could automatically adjust to changing market conditions without manual intervention. Since its introduction, KAMA has become a popular technical indicator among traders who need a moving average that responds quickly to significant price movements while ignoring minor fluctuations.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/kama.pine)

## Core Concepts

KAMA addresses the limitations of fixed-parameter moving averages through:

- Efficiency Ratio (ER) to measure the directional movement relative to volatility
- Dynamic smoothing constant that adapts to market conditions
- Squared smoothing factor to emphasize the difference between trending and non-trending markets
- Self-adjusting time constants based on price behavior

## Mathematical Foundation

$KAMA = KAMA_{previous} + SC \times (source - KAMA_{previous})$

Where:
- $SC$ (Smoothing Constant) = $[ER \times (Fast_\alpha - Slow_\alpha) + Slow_\alpha]^2$
- $ER$ (Efficiency Ratio) = $Change / Volatility$
- $Change = |source - source[period]|$
- $Volatility = \sum|source - source[1]|$ for period

## Calculation Process

1. Calculate Efficiency Ratio:
   - Measure directional change: $|current\ price - price\ period\ bars\ ago|$
   - Measure volatility: Sum of $|price\ changes|$ over period
   - $ER = Change / Volatility$ (ranges from 0 to 1)

2. Calculate Smoothing Constant:
   - $SC = [ER \times (Fast_\alpha - Slow_\alpha) + Slow_\alpha]^2$
   - $Fast_\alpha$ typically = $2/(2+1) = 0.6667$ (responsive)
   - $Slow_\alpha$ typically = $2/(30+1) = 0.0645$ (stable)
   - SC dynamically adjusts between $Fast_\alpha$ and $Slow_\alpha$ based on ER

3. Apply KAMA formula:
   - $KAMA = KAMA_{previous} + SC \times (source - KAMA_{previous})$

The adaptive nature allows KAMA to be more responsive during trending markets (high ER) and more stable during sideways markets (low ER).

KAMA uses a squared smoothing factor to emphasize the difference between trending and non-trending markets:
- When ER = 1 (perfect trend): $SC = Fast_\alpha^2$
- When ER = 0 (pure noise): $SC = Slow_\alpha^2$
- The squared value creates a non-linear response curve that enhances adaptivity

## Advantages and Limitations

### Advantages
- Automatically adjusts to changing market conditions
- Responds quickly during genuine market movements
- Provides stability during sideways or choppy markets
- Valid from the first bar without extensive warm-up
- No need to change parameters as market conditions shift
- Less prone to false signals during consolidation phases

### Limitations
- More calculations required than simple moving averages
- Initial selection of fast/slow parameters impacts overall behavior
- May be slower to recognize the beginning of new trends
- ER calculation can be sensitive to the selected period
- More difficult to predict exact responses compared to traditional moving averages

## Sources

1. Kaufman, P. (1995). *Smarter Trading*. McGraw-Hill.
2. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
3. Kaufman, P. (1998). "Adaptive Moving Averages," *Technical Analysis of Stocks & Commodities*.
4. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons.
