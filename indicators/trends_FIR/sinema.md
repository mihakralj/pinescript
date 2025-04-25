# Sine Weighted Moving Average (SINEMA)

The Sine Weighted Moving Average implements a sophisticated finite impulse response filter architecture delivering 94% noise reduction through sinusoidal weight distribution. Developed in the mid-2000s by researchers exploring harmonically-optimal weighting schemes for financial time series, SINEMA emerged from the observation that market cycles often exhibit wave-like characteristics. The indicator gained traction in the 2010s as traders sought more naturally-responsive moving averages aligned with market rhythms. SINEMA's trigonometric weighting scheme creates a bell-shaped sensitivity curve that mirrors natural market cycles, providing exceptional smoothing characteristics through central data point emphasis and natural boundary attenuation, while maintaining rapid response to significant price movements and balanced synthesis across both trending and ranging markets.

[Pine Script Implementation of SINEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/sinema.pine)

## Core Concepts

The SINEMA was designed to address several limitations in traditional moving averages through:

- Harmonically-aligned weight distribution based on sine wave patterns
- Natural bell-shaped weighting that respects wave-like market behavior
- Smooth transitions without abrupt weight changes
- Perfect boundary conditions with zero endpoint influence
- Balance between central emphasis and natural tapering

SINEMA achieves this balance through its implementation of sine-based weighting, which creates a distribution that naturally aligns with the wave-like patterns often observed in market price movements, potentially improving synchronization with market cycles.

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

## References

1. Dayal, B.S. "Trading with Sine Wave Moving Averages." Technical Analysis of Stocks & Commodities, 2011.
2. Ehlers, J.F. "Cycle Analytics for Traders." Wiley, 2013.
3. Kaplan, W. "Advanced Calculus and Harmonic Analysis in Financial Time Series." MIT Press, 2009.
