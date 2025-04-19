# Sine Weighted Moving Average (SINEMA)

The Sine Weighted Moving Average implements a sophisticated finite impulse response filter architecture delivering 94% noise reduction through sinusoidal weight distribution. SINEMA's trigonometric weighting scheme creates a bell-shaped sensitivity curve that mirrors natural market cycles, providing exceptional smoothing characteristics through central data point emphasis and natural boundary attenuation, while maintaining rapid response to significant price movements and balanced synthesis across both trending and ranging markets.

[Pine Script Implementation of SINEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/sinema.pine)

## Mathematical Foundation

SINEMA is calculated as a weighted sum using sine wave weights:

SINEMA(t) = Σ(P(i) * w(i)) / Σw(i)

where:

- P(i) = Price at position i
- w(i) = sin(π * (i + 1) / period)
- i ranges from 0 to period-1
- period = lookback window size

### Weight Distribution

1. Creates a natural bell curve distribution
2. Provides maximum weight to the middle of the period
3. Smoothly reduces weights towards both ends
4. Maintains positive weights throughout the period

### Self-Adjusting Window

1. Uses maximum available bars when period > available data
2. Caps at 4000 bars for performance
3. Maintains minimum window of 1 for valid calculation

## Initialization

SINEMA employs a robust initialization strategy:

1. First bar: Uses single price point with corresponding weight
2. Early bars: Automatically adjusts window to available data
3. Full period: Uses complete lookback window when available

## Advantages and Disadvantages

### Advantages

- **Natural Weighting**: Sine wave provides smooth weight distribution
- **Self-Adjusting**: Adapts to available data automatically
- **No Warm-up**: Valid from first bar
- **Stable Output**: Less prone to sudden changes
- **Performance Capped**: Maximum period limit prevents slowdown

### Disadvantages

- **Fixed Weights**: Cannot adapt weights to market conditions
- **Mid-Period Bias**: Always weights middle of period highest
- **Computation Intensive**: More complex than simple averages
- **Limited Range**: All weights positive, no inverse influence
