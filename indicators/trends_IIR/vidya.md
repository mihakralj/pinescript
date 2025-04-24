# Variable Index Dynamic Average (VIDYA)

## Historical Background

The Variable Index Dynamic Average (VIDYA) was developed by Tushar Chande in the early 1990s as an adaptive moving average that adjusts its smoothing factor based on market volatility. Chande recognized that traditional moving averages with fixed parameters struggled to adapt to changing market conditions. VIDYA addressed this limitation by becoming more responsive during volatile periods and smoother during low volatility phases.

Since its introduction, VIDYA has gained significant recognition among technical analysts and has been incorporated into numerous algorithmic trading systems and professional platforms. Its approach to volatility-based adaptation has influenced the development of many other adaptive indicators in technical analysis.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/vidya.pine)

## Core Concepts

VIDYA addresses the limitations of fixed-parameter moving averages through:

- Volatility-based adaptation of the smoothing factor
- Standard deviation ratios to measure relative volatility
- Dynamic response to changing market conditions
- Automatic adjustment based on market behavior

## Mathematical Foundation

VIDYA uses a volatility index (VI) to adjust the smoothing factor:

$\alpha = \frac{2}{period + 1}$

$VI = \frac{StdDev(price, 5)}{StdDev(price, period)}$

$VI$ is clamped to $[0,1]$ range

$SC = \alpha \times VI$

$VIDYA_{today} = VIDYA_{yesterday} + SC \times (Price_{today} - VIDYA_{yesterday})$

Where:
- $\alpha$ is the base smoothing factor
- $VI$ is the volatility index
- $SC$ is the scaled smoothing constant

## Calculation Process

1. Calculate the base smoothing factor $\alpha$ using the specified period
2. Compute the volatility index (VI) as the ratio of short-term volatility to longer-term volatility
3. Ensure VI remains within the [0,1] range by clamping extreme values
4. Determine the scaled smoothing constant (SC) by multiplying $\alpha$ by VI
5. Calculate VIDYA using an EMA-like formula with the scaled smoothing constant

The implementation introduces adaptive behavior by scaling the EMA smoothing factor based on relative volatility. When volatility is high, VIDYA responds faster to price changes, while during low volatility periods, it produces a smoother line.

## Advantages and Limitations

### Advantages
- Automatically adapts to changing market volatility
- Reduces lag during volatile market conditions
- Provides smoother output during low volatility periods
- Maintains signal integrity across different market regimes
- Helps filter out noise while remaining responsive to significant movements

### Limitations
- Requires more computational resources than standard moving averages
- Sensitivity to volatility calculation parameters
- May be overly responsive during extreme volatility events
- Standard deviation calculations introduce additional complexity
- Performance depends on appropriate parameter selection

## Sources

1. Chande, T. (1992). "Adapting Moving Averages to Market Volatility," *Technical Analysis of Stocks & Commodities*
2. Chande, T. & Kroll, S. (1994). *The New Technical Trader*
3. Kaufman, P. (2013). "Adaptive Moving Averages," *Trading Systems and Methods*, 5th Edition
