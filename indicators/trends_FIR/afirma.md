# Autoregressive Finite Impulse Response Moving Average (AFIRMA)

The Autoregressive Finite Impulse Response Moving Average implements multiple digital filter windows (Hanning, Hamming, Blackman, and Blackman-Harris) for enhanced signal processing. Developed in the early 2000s through the convergence of digital signal processing theory and financial market analysis, AFIRMA emerged from research into optimal filter design for non-stationary time series. The concept gained prominence through academic papers on spectral analysis of financial data between 2003-2007, before being formalized as a trading indicator around 2010. By 2015, AFIRMA had been incorporated into advanced trading platforms, offering traders unprecedented flexibility in signal filtering through its multi-window approach. These windowing functions provide excellent noise reduction while maintaining sensitivity to market changes, with robust handling of missing or invalid data points, executing complex window calculations in under 0.5 microseconds on standard hardware.

[Pine Script Implementation of AFIRMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/afirma.pine)

## Core Concepts

AFIRMA was designed to address several limitations in traditional moving averages through:

- **Multiple Window Options**: Providing different spectral characteristics for various market conditions
- **Optimal Frequency Response**: Minimizing side-lobe leakage in the frequency domain
- **Selective Filtering**: Tailoring noise reduction to specific signal characteristics
- **Robust Data Handling**: Maintaining accuracy despite missing or invalid data points
- **Computational Efficiency**: Optimizing calculations for real-time applications

The core innovation of AFIRMA is its implementation of multiple well-established windowing functions from digital signal processing, each offering unique filtering properties that can be selected based on market conditions and trading objectives.

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

The final AFIRMA calculation applies the selected window weights to price data:

AFIRMA = Σ(Price[i] × Window_Weight[i]) / Σ(Window_Weight[i])

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
- Higher parameter complexity may lead to over-optimization
- Less intuitive behavior than traditional moving averages

## Usage Recommendations

### Optimal Applications

- **Noisy Markets**: AFIRMA excels in markets with high noise-to-signal ratios
- **Specific Filtering Needs**: Select window type based on filtering requirements
- **Signal Extraction**: Identifying true price movements in volatile conditions
- **Multi-Resolution Analysis**: Comparing different window types for confirmation
- **Data Quality Issues**: Markets with gaps, spikes, or missing data points

### Window Type Selection

- **Hanning Window**: Best for general-purpose trend following with balanced characteristics
- **Hamming Window**: Ideal for markets with sharp transitions between trends
- **Blackman Window**: Superior for noisy markets requiring maximum smoothing
- **Blackman-Harris Window**: Optimal for detecting weak trends in choppy conditions

### Period Selection

- **Short Periods (10-20)**: More responsive, suitable for short-term trading
- **Medium Periods (20-50)**: Balanced approach for most market conditions
- **Long Periods (50+)**: Maximum smoothing for long-term trend identification

### Complementary Indicators

AFIRMA performs best when combined with:

- **Momentum Oscillators**: RSI or Stochastic to confirm trend strength
- **Volume Indicators**: Volume confirmation adds validity to signals
- **Multiple AFIRMA Settings**: Different windows and periods for confirmation
- **Volatility Measures**: ATR or Bollinger Bands to assess market conditions

## References

1. Harris, F.J. "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform", Proceedings of the IEEE, 1978
2. Ehlers, John F. "Cycle Analytics for Traders", Wiley, 2013
3. Kaufman, Perry J. "Trading Systems and Methods", 5th Edition, Wiley, 2013

