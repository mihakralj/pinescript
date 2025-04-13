# Triangular Moving Average (TRIMA)

The Triangular Moving Average (TRIMA) is a technical indicator that applies a triangular weighting scheme to signal within a calculation window. As a specialized form of weighted moving average, TRIMA puts the highest weight on the middle values and progressively lower weights towards both ends of the window, creating a symmetric, triangle-shaped weight distribution. This double-smoothing effect makes it particularly effective at filtering out signal noise while maintaining sensitivity to genuine trend changes.

[Pine Script Implementation of TRIMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/trima.pine)

## Mathematical Foundation

### Basic Formula

The TRIMA calculation applies a triangular weighting pattern to each data point:

TRIMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:
- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the triangular weights
- n is the number of periods (window size)

### Triangular Weighting Scheme

The weights form a symmetric triangular pattern:

| Position | Weight Formula | Example (n=5) | Example (n=4) |
|----------|---------------|---------------|---------------|
| i | min(i, n-1-i) + 1 | [1,2,3,2,1] | [1,2,2,1] |

The weight at position i increases linearly until the middle of the window, then decreases linearly to the end, creating a perfect triangle shape.

### Alternative Calculation

A TRIMA can also be expressed as a double application of SMA with adjusted period:

TRIMA(source, p) = SMA(SMA(source, (p+1)/2), (p+1)/2)

This relationship demonstrates why TRIMA provides better smoothing than a single SMA or WMA, as it effectively applies smoothing twice with optimal period adjustment.

## FIR Filter Characteristics

TRIMA is a Finite Impulse Response (FIR) filter with specific properties:

1. **Symmetric Response**: Equal weights on both sides of the center point
2. **Fixed Window**: Output depends only on a finite number of past inputs
3. **Zero Weight Outside Window**: No influence from data beyond the window
4. **Linear Phase**: Maintains waveform shape due to symmetrical weighting

### Transfer Function Properties

As a triangular-weighted FIR filter, TRIMA provides:
- Better high-frequency noise reduction than SMA or WMA
- Smoother frequency response than linear weighting
- Less phase distortion due to symmetric weights
- Approximately -18dB per octave roll-off

## Initialization Properties

### Full Window Requirement

TRIMA requires a minimum of n data points for a complete calculation. For a period of n, the implementation handles the first n-1 values by:
1. Using available data points with adjusted (smaller) triangular weights
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Superior Smoothing**: Better noise reduction than SMA or WMA
- **Symmetric Weighting**: No bias towards either recent or old data
- **Reduced Whipsaws**: Less prone to false signals than simpler averages
- **Linear Phase Response**: Preserves signal shape in the passband
- **Better Roll-off**: Steeper frequency response than linear weighting

### Disadvantages

- **Increased Lag**: More lag than WMA or EMA due to middle-weighted emphasis
- **Limited Adaptability**: Fixed weighting scheme cannot adapt to changing volatility
- **Slower Response**: Takes longer to reflect sudden signal changes
- **Complex Parameters**: Harder to optimize period length due to double-smoothing effect
