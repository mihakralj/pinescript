# Hamming Moving Average (HAMMA)

The Hamming Moving Average implements an optimized bell-shaped weight distribution architecture using the Hamming window function to achieve noise reduction through frequency domain optimization. Developed by Richard Hamming at Bell Labs in 1959 for telecommunications signal processing, the Hamming window was adapted for financial market analysis in the 1990s as digital signal processing techniques gained traction in technical analysis. Its superior spectral characteristics made it particularly valuable for noisy market data, and by the early 2000s, it had become implemented in advanced trading platforms. HAMMA's modified cosinusoidal weighting algorithm delivers superior frequency roll-off with significantly reduced side-lobes while maintaining signal integrity during trend transitions, reducing whipsaw signals while preserving waveform fidelity through its symmetrical FIR implementation and linear phase response.

[Pine Script Implementation of HAMMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/hamma.pine)

## Core Concepts

The HAMMA was designed to address several limitations in traditional moving averages through:

- Optimal balancing of main-lobe width and side-lobe suppression
- Modified cosine weighting for superior frequency characteristics
- Center-weighted design for maximum noise rejection
- Minimized spectral leakage for clearer trend signals
- Preservation of signal phase relationships

The Hamming window's key innovation is the precise offset (0.54 - 0.46cos) that creates a near-optimal trade-off between frequency selectivity and side-lobe suppression, making it particularly effective at identifying meaningful market trends in noisy conditions.

## Mathematical Foundation

The HAMMA calculation applies a Hamming window weighting pattern to each data point:

HAMMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:

- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the Hamming window weights
- n is the number of periods (window size)

### Hamming Window Weighting Scheme

The weights follow the Hamming window function:

w(n) = 0.54 - 0.46 × cos(2π × n / (N - 1))

This creates a bell-shaped weighting curve that gives more weight to the center values and smoothly tapers off toward the edges, with an offset that minimizes side lobes in the frequency domain, resulting in excellent spectral characteristics.

## Initialization Properties

### Full Window Requirement

HAMMA requires a minimum of n data points for a complete calculation. For a period of n, the implementation handles the first n-1 values by:

1. Using available data points with adjusted Hamming window weights
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Superior Side-lobe Suppression**: Better side-lobe attenuation than Hanning and other windows
- **Symmetric Weighting**: No bias towards either recent or old data
- **Reduced Whipsaws**: Less prone to false signals than simpler averages
- **Linear Phase Response**: Preserves signal shape in the passband
- **Smooth Transitions**: Bell-shaped weighting provides natural smoothing

### Disadvantages

- **Increased Lag**: More lag than linear weighting due to center-weighted emphasis
- **Limited Adaptability**: Fixed weighting scheme cannot adapt to changing volatility
- **Slightly Wider Main-lobe**: Wider main lobe than Hanning window, trading frequency selectivity for side-lobe suppression
- **Complex Parameters**: Single period parameter belies sophisticated frequency characteristics

## References

1. Hamming, R.W. (1977). "Digital Filters." Prentice-Hall
2. Ehlers, J.F. (2013). "Cycle Analytics for Traders."
3. Proakis, J.G. and Manolakis, D.G. (2006). "Digital Signal Processing."
