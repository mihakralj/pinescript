# Blackman Moving Average (BLMA)

The Blackman Moving Average implements an optimized weight distribution using the Blackman window function to achieve superior frequency domain characteristics. Developed by Ralph Beebe Blackman at Bell Labs in the 1950s as an improvement over earlier window functions, the Blackman window was originally designed for spectral analysis in telecommunications. Its application to financial markets emerged in the late 1990s as digital signal processing techniques became more prevalent in technical analysis. By the mid-2000s, it had been incorporated into advanced trading platforms for its exceptional noise-filtering properties. BLMA's cosine-based weighting algorithm provides excellent side-lobe suppression while preserving signal structure, reducing noise and false signals while maintaining accuracy during trend transitions through its symmetrical FIR implementation.

[Pine Script Implementation of BLMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/blma.pine)

## Core Concepts

The BLMA was designed to address several limitations in traditional moving averages through:

- Enhanced spectral leakage control with triple-cosine weighting
- Superior side-lobe suppression compared to other window functions
- Balanced main-lobe width for optimal time-frequency resolution
- Preservation of important market signals while eliminating noise
- Symmetrical design for zero phase distortion

BLMA achieves this balance through its sophisticated three-term cosine series that creates a weight distribution optimized for separating meaningful price movements from market noise, particularly valuable in choppy or consolidating markets.

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

## References

1. Ehlers, J.F. (2013). "Cycle Analytics for Traders," Wiley, Chapter 8: "Filtering Methods for Trend Enhancement."
2. Mulloy, P. (1994). "Smoothing Techniques for More Accurate Signals," Technical Analysis of Stocks & Commodities
