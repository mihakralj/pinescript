# Blackman Moving Average (BLMA)

The Blackman Moving Average implements an optimized weight distribution using the Blackman window function to achieve superior frequency domain characteristics. BLMA's cosine-based weighting algorithm provides excellent side-lobe suppression while preserving signal structure, reducing noise and false signals while maintaining accuracy during trend transitions through its symmetrical FIR implementation.

[Pine Script Implementation of BLMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/blma.md)

## Mathematical Foundation

The BLMA calculation applies a Blackman window weighting pattern to each data point:

BLMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:

- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the Blackman window weights
- n is the number of periods (window size)

### Blackman Window Weighting Scheme

The weights follow the Blackman window function:

w(n) = a₀ - a₁cos(2πn/(N-1)) + a₂cos(4πn/(N-1))

Where:

- n is the position in the window
- N is the window size
- a₀ = 0.42, a₁ = 0.5, a₂ = 0.08 are the Blackman coefficients

This creates a bell-shaped weighting curve with excellent spectral characteristics, including significantly reduced side lobes compared to other window functions. The Blackman window achieves -58dB side-lobe attenuation, making it particularly effective at removing noise while preserving trend signals.

## Initialization Properties

### Full Window Requirement

BLMA requires a minimum of n data points for a complete calculation. For a period of n, the implementation handles the first n-1 values by:

1. Using available data points with adjusted Blackman window weights
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Superior Side-lobe Suppression**: -58dB side-lobe attenuation compared to -42dB in Hamming and -32dB in Hanning windows
- **Excellent Noise Filtering**: Advanced filtering characteristics over simpler moving averages
- **Symmetric Weighting**: No bias towards either recent or old data
- **Reduced Whipsaws**: Less prone to false signals than simpler averages
- **Linear Phase Response**: Preserves signal shape in the passband
- **Spectral Leakage Control**: Better elimination of noise artifacts than most window functions

### Disadvantages

- **Increased Lag**: More lag than linear weighting schemes due to center-weighted emphasis
- **Limited Adaptability**: Fixed weighting scheme cannot adapt to changing volatility
- **Main-lobe Width**: Wider main lobe than some other windows, leading to reduced frequency resolution
- **Fixed Parameterization**: Standard Blackman window uses fixed coefficients
