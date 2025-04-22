# Hamming Moving Average (HAMMA)

The Hamming Moving Average implements an optimized bell-shaped weight distribution architecture using the Hamming window function to achieve noise reduction through frequency domain optimization. HAMMA's modified cosinusoidal weighting algorithm delivers superior frequency roll-off with significantly reduced side-lobes while maintaining signal integrity during trend transitions, reducing whipsaw signals while preserving waveform fidelity through its symmetrical FIR implementation and linear phase response.

[Pine Script Implementation of HAMMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/hamma.pine)

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
