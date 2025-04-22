# Savitzky-Golay Moving Average (SGMA)

The Savitzky-Golay Moving Average implements polynomial-based smoothing that optimally preserves the higher moments of the data while filtering noise. SGMA uses least-squares polynomial fitting across a sliding window to enhance signal features such as maxima, minima, and width without introducing significant distortion. This advanced technique is particularly valuable for preserving rapid changes in trends while effectively removing noise.

[Pine Script Implementation of SGMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/sgma.md)

## Mathematical Foundation

The SGMA calculation applies a specialized set of convolution coefficients derived from fitting polynomials to data points:

SGMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:

- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the Savitzky-Golay filter coefficients
- n is the number of periods (window size, must be odd)

### Savitzky-Golay Filter Coefficient Determination

The weights are derived by fitting a polynomial of degree d to a set of n points in a least-squares sense, then evaluating the resulting polynomial at the center point:

For each point in the window, a local polynomial approximation is computed:
f(x) = c₀ + c₁x + c₂x² + ... + cₚxᵖ

The implementation uses pre-computed coefficients for common combinations of window sizes and polynomial degrees, with approximations for other cases to optimize performance while maintaining accuracy.

## Initialization Properties

### Full Window and Polynomial Order Requirements

SGMA requires:
- An odd number of data points (window size)
- A polynomial degree less than the window size
- At least window size data points for a complete calculation

The implementation handles the initialization period by:
1. Using available data points with appropriate weighting
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Feature Preservation**: Superior preservation of peaks, valleys, and inflection points
- **Higher-Order Moment Retention**: Maintains statistical properties of the original signal
- **Noise Reduction**: Effectively eliminates random noise while preserving signal structure
- **Tunable Parameters**: Adjustable polynomial degree and window size for different scenarios
- **Linear Phase Response**: Maintains phase relationships, avoiding distortion
- **Enhanced Extrema Detection**: Helps identify turning points more accurately

### Disadvantages

- **Computational Complexity**: More computationally intensive than simpler moving averages
- **Parameter Selection**: Requires understanding of polynomial fitting principles
- **Reduced Smoothing**: Higher polynomial degrees can under-smooth noisy data
- **Over-fitting Risk**: High polynomial degrees with small windows may fit noise
- **Edge Effects**: Performance can degrade near the edges of the data series
- **Odd-Length Requirement**: Window size must be odd
