# Gaussian-Weighted Moving Average (GWMA)

The Gaussian-Weighted Moving Average implements an optimized bell-shaped weight distribution architecture using the Gaussian (normal) distribution to achieve noise reduction through frequency domain optimization. Inspired by the fundamental Gaussian distribution first formalized by Carl Friedrich Gauss in the early 19th century, the GWMA emerged in financial markets during the 1990s as researchers explored statistically optimal smoothing methods. The approach gained widespread adoption in the early 2000s after several influential papers demonstrated its superior filtering characteristics compared to traditional moving averages. GWMA's exponential weighting algorithm delivers excellent frequency roll-off with minimal side-lobes while maintaining signal integrity during trend transitions, reducing whipsaw signals while preserving waveform fidelity through its symmetrical FIR implementation and linear phase response.

[Pine Script Implementation of GWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/gwma.pine)

## Core Concepts

The GWMA was designed to address several limitations in traditional moving averages through:

- Statistically optimal weight distribution based on the normal curve
- Infinitely differentiable smooth weighting function
- Tunable bell curve width via sigma parameter
- Superior spectral characteristics with minimal leakage
- Natural decay of influence from central point

GWMA achieves this balance through its implementation of the Gaussian window, which creates a weight distribution with theoretically optimal time-bandwidth product, making it particularly effective at separating market signals from noise while preserving important trend characteristics.

## Mathematical Foundation

The GWMA calculation applies a Gaussian window weighting pattern to each data point:

GWMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:

- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the Gaussian window weights
- n is the number of periods (window size)

### Gaussian Window Weighting Scheme

The weights follow the Gaussian window function:

w(n) = exp(-0.5 × ((n - c) / (σ × N))²)

Where:

- n is the position in the window
- c is the center of the window
- σ (sigma) is the parameter controlling the width of the Gaussian bell curve
- N is the window size

This creates a bell-shaped weighting curve that gives more weight to the center values and smoothly tapers off toward the edges, resulting in excellent frequency domain characteristics. The sigma parameter allows for fine-tuning the shape of the distribution—smaller sigma values create a narrower bell curve with greater emphasis on center values.

## Initialization Properties

### Full Window Requirement

GWMA requires a minimum of n data points for a complete calculation. For a period of n, the implementation handles the first n-1 values by:

1. Using available data points with adjusted Gaussian window weights
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Excellent Frequency Response**: Superior side-lobe suppression compared to most window functions
- **Tunable Weighting Distribution**: The sigma parameter allows customizing the bell curve shape
- **Symmetric Weighting**: No bias towards either recent or old data
- **Reduced Whipsaws**: Less prone to false signals than simpler averages
- **Linear Phase Response**: Preserves signal shape in the passband
- **Smooth Transitions**: Bell-shaped weighting provides natural smoothing

### Disadvantages

- **Increased Lag**: More lag than linear weighting due to center-weighted emphasis
- **Limited Adaptability**: Fixed weighting scheme cannot adapt to changing volatility
- **Additional Complexity**: The sigma parameter adds complexity but offers greater control
- **Computational Overhead**: Slightly higher computational requirements due to exponential calculations

## References

1. Harris, F.J. (1978). "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform." Proceedings of the IEEE.
2. Oppenheim, A.V. and Schafer, R.W. (2009). "Discrete-Time Signal Processing." Prentice Hall.
3. Ehlers, J.F. (2013). "Cycle Analytics for Traders." Wiley.
