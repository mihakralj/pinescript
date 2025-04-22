# Hanning Moving Average (HANMA)

The Hanning Moving Average implements an optimized bell-shaped weight distribution architecture using the Hanning window function to achieve noise reduction through frequency domain optimization. HANMA's cosinusoidal weighting algorithm delivers excellent frequency roll-off with minimal side-lobes while maintaining signal integrity during trend transitions, reducing whipsaw signals while preserving waveform fidelity through its symmetrical FIR implementation and linear phase response.

[Pine Script Implementation of HANMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/hanma.pine)

## Mathematical Foundation

The HANMA calculation applies a Hanning window weighting pattern to each data point:

HANMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:

- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the Hanning window weights
- n is the number of periods (window size)

### Hanning Window Weighting Scheme

The weights follow the Hanning window function:

w(n) = 0.5 × (1 - cos(2π × n / (N - 1)))

This creates a bell-shaped weighting curve that gives more weight to the center values and smoothly tapers off toward the edges, resulting in excellent frequency domain characteristics.

## Initialization Properties

### Full Window Requirement

HANMA requires a minimum of n data points for a complete calculation. For a period of n, the implementation handles the first n-1 values by:

1. Using available data points with adjusted Hanning window weights
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Excellent Frequency Response**: Better side-lobe suppression than rectangular or triangular windows
- **Symmetric Weighting**: No bias towards either recent or old data
- **Reduced Whipsaws**: Less prone to false signals than simpler averages
- **Linear Phase Response**: Preserves signal shape in the passband
- **Smooth Transitions**: Bell-shaped weighting provides natural smoothing

### Disadvantages

- **Increased Lag**: More lag than linear weighting due to center-weighted emphasis
- **Limited Adaptability**: Fixed weighting scheme cannot adapt to changing volatility
- **Moderate Main-lobe Width**: Slightly wider main lobe than some other windows
- **Complex Parameters**: Single period parameter belies sophisticated frequency characteristics
