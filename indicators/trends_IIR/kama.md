# Kaufman's Adaptive Moving Average (KAMA)

Kaufman's Adaptive Moving Average was developed by Perry Kaufman in the 1990s and introduced in his 1995 book "Smarter Trading." Unlike traditional moving averages, KAMA adjusts its sensitivity based on market conditions.

Kaufman created KAMA after years studying various trading systems across different markets. His approach was inspired by earlier adaptive techniques but innovated by creating a formula that could automatically adjust to changing market conditions without manual intervention. KAMA has become a popular technical indicator among traders who need a moving average that responds quickly to significant price movements while ignoring minor fluctuations.

[Pine Script Implementation of KAMA](https://github.com/mihakralj/pinescript/blob/main/indicators/predictors/kama.pine)

## Mathematical Foundation

KAMA = KAMA_previous + SC × (source - KAMA_previous)

Where:

- SC (Smoothing Constant) = [ER × (Fast_α - Slow_α) + Slow_α]²
- ER (Efficiency Ratio) = Change / Volatility
- Change = |source - source[period]|
- Volatility = Σ|source - source[1]| for period

### Detailed Breakdown

1. Calculate Efficiency Ratio:
   - Measure directional change: |current price - price period bars ago|
   - Measure volatility: Sum of |price changes| over period
   - ER = Change / Volatility (ranges from 0 to 1)

2. Calculate Smoothing Constant:
   - SC = [ER × (Fast_α - Slow_α) + Slow_α]²
   - Fast_α typically = 2/(2+1) = 0.6667 (responsive)
   - Slow_α typically = 2/(30+1) = 0.0645 (stable)
   - SC dynamically adjusts between Fast_α and Slow_α based on ER

3. Apply KAMA formula:
   - KAMA = KAMA_previous + SC × (source - KAMA_previous)

The adaptive nature allows KAMA to be more responsive during trending markets (high ER) and more stable during sideways markets (low ER).

### Smoothing Factors

KAMA uses a squared smoothing factor to emphasize the difference between trending and non-trending markets:

- When ER = 1 (perfect trend): SC = Fast_α²
- When ER = 0 (pure noise): SC = Slow_α²
- The squared value creates a non-linear response curve that enhances adaptivity

### Adaptive Smoothing Mechanism

- Market-aware filtering through ER calculation
- Self-adjusting time constants based on price behavior
- Continuous adaptation without parameter changes
- Balance between trend following and noise reduction

## Advantages and Disadvantages

### Advantages

- **Market Adaptivity**: Automatically adjusts to changing market conditions
- **Reduced Lag in Trends**: Responds quickly during genuine market movements
- **Noise Filtering**: Provides stability during sideways or choppy markets
- **No Warm-up Required**: Valid from the first bar
- **Self-Optimizing**: No need to change parameters as market conditions shift
- **Reduced Whipsaws**: Less prone to false signals during consolidation phases

### Disadvantages

- **Computational Complexity**: More calculations required than simple moving averages
- **Parameter Sensitivity**: Initial selection of fast/slow parameters impacts overall behavior
- **Delayed Recognition of New Trends**: May be slower to recognize the beginning of new trends
- **Efficiency Ratio Limitations**: ER calculation can be sensitive to the selected period
- **Non-Linear Behavior**: More difficult to predict exact responses compared to traditional moving averages
