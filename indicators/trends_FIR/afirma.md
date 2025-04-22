# Autoregressive Finite Impulse Response Moving Average (AFIRMA)

The Autoregressive Finite Impulse Response Moving Average implements multiple digital filter windows (Hanning, Hamming, Blackman, and Blackman-Harris) for enhanced signal processing. These windowing functions provide excellent noise reduction while maintaining sensitivity to market changes, with robust handling of missing or invalid data points.

[Pine Script Implementation of AFIRMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/afirma.pine)

## Mathematical Foundation

AFIRMA applies specialized windowing functions to price data. These functions shape the frequency response of the filter:

1. **Hanning Window**: w(k) = 0.50 - 0.50 × cos(2π × k / n)
   - Good frequency resolution with moderate side lobe suppression
   - Balances smoothness and responsiveness

2. **Hamming Window**: w(k) = 0.54 - 0.46 × cos(2π × k / n)
   - Optimized to minimize the maximum side lobe
   - Improved frequency selectivity

3. **Blackman Window**: w(k) = 0.42 - 0.50 × cos(2π × k / n) + 0.08 × cos(4π × k / n)
   - Better side lobe suppression than Hanning and Hamming
   - Excellent for separating closely spaced frequency components

4. **Blackman-Harris Window**: w(k) = 0.35875 - 0.48829 × cos(2π × k / n) + 0.14128 × cos(4π × k / n) - 0.01168 × cos(6π × k / n)
   - Provides excellent side lobe suppression
   - Best for identifying weak signals in presence of strong ones

Where:

- k is the position in the window (0 to n-1)
- n is the window size (period)
- w(k) is the weight at position k

## Implementation Details

The AFIRMA implementation:

1. Dynamically calculates window coefficients based on selected window type
2. Optimizes memory usage by caching coefficients across calculations
3. Applies windowing function to signal data with robust NA handling
4. Normalizes output based on valid data points only
5. Employs additional optimizations for computational efficiency

### Dirty Data Handling

AFIRMA implements robust handling of missing or invalid data points:

1. Tracks valid data points during calculation
2. Normalizes weights based only on valid data points
3. Gracefully handles initial bars when available data is less than the period
4. Falls back to source values when insufficient valid data is available

## Advantages and Disadvantages

### Advantages

- Superior noise reduction compared to simple moving averages
- Flexible selection of windowing functions for different market conditions
- Excellent frequency response characteristics with minimal distortion
- Robust handling of missing or invalid data points
- Optimized for performance with minimal computational overhead

### Disadvantages

- More complex calculation than standard moving averages
- Requires selection of appropriate windowing function for specific use cases
- Different window types have different trade-offs between smoothness and responsiveness
