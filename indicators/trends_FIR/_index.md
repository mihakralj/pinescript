# Finite Impulse Response (FIR) Trends and Predictors

| Indicator | Name | Description |
| ------------ | ---------------------------------------- | ---------------------------------------- |
| [AFIRMA](/indicators/trends_FIR/afirma.md) | Adaptive Finite Impulse Response MA | Adaptively adjusts filter response characteristics based on input data dynamics for optimal smoothing. |
| [ALMA](/indicators/trends_FIR/alma.md) | Arnaud Legoux MA | Applies Gaussian distribution weights to price data with configurable offset and sigma parameters to reduce lag while maintaining noise filtering. |
| [BLMA](/indicators/trends_FIR/blma.md) | Blackman Window MA | Implements Blackman window function for superior frequency response with minimized side-lobes in spectral domain. |
| [CONV](/indicators/trends_FIR/conv.md) | Convolution MA with any kernel | Provides generalized convolution framework supporting arbitrary kernel functions for customizable filtering characteristics. |
| [BWMA](/indicators/trends_FIR/bwma.md) | Bessel-Weighted MA | Uses Bessel function weighting to achieve maximally flat group delay with minimal phase distortion. |
| [DWMA](/indicators/trends_FIR/dwma.md) | Double Weighted MA | Applies squared weighting factors to emphasize recent price action while maintaining smooth transitions. |
| [EPMA](/indicators/trends_FIR/epma.md) | Endpoint MA | Shifts weighting toward most recent data points to minimize lag at trend endpoints. |
| [GWMA](/indicators/trends_FIR/gwma.md) | Gaussian-Weighted MA | Distributes weights according to normal distribution for balanced noise reduction and trend preservation. |
| [HAMMA](/indicators/trends_FIR/hamma.md) | Hamming Window MA | Employs Hamming window function to optimize main-lobe width and side-lobe attenuation for improved spectral characteristics. |
| [HANMA](/indicators/trends_FIR/hanma.md) | Hanning Window MA | Applies raised cosine weighting (Hanning window) for smooth frequency response with zero weight at window edges. |
| [HMA](/indicators/trends_FIR/hma.md) | Hull MA | Combines weighted averages at different periods with momentum-enhanced processing to reduce lag by 83% while maintaining 94% noise suppression. |
| [HWMA](/indicators/trends_FIR/hwma.md) | Holt Weighted MA | Integrates exponential weighting with trend-component analysis for improved prediction of time series data. |
| [LSMA](/indicators/trends_FIR/lsma.md) | Least Squares Moving Average | Fits a linear regression line to price data using the method of least squares, reducing lag while maintaining smoothness. |
| [PWMA](/indicators/trends_FIR/pwma.md) | Pascal Weighted MA | Utilizes Pascal's triangle coefficients for weight distribution, offering balanced statistical properties. |
| [SGMA](/indicators/trends_FIR/sgma.md) | Savitzky-Golay MA | Performs polynomial regression within sliding windows to preserve higher moments of the distribution while smoothing. |
| [SINEMA](/indicators/trends_FIR/sinema.md) | Sine-weighted MA | Distributes weights according to sine function for gradual influence transition and improved harmonic response. |
| [SMA](/indicators/trends_FIR/sma.md) | Simple MA | Implements foundational uniformly-weighted average with optimized recursive calculation, achieving 85% noise reduction with deterministic -13dB/octave frequency roll-off. |
| [TRIMA](/indicators/trends_FIR/trima.md) | Triangular MA | Applies triangular weighting scheme for enhanced smoothing with twice the noise reduction of simple moving averages. |
| [VWMA](/indicators/trends_FIR/vwma.md) | Volume Weighted MA | Incorporates trading volume as a weighting factor to emphasize price movements with higher volume confirmation. |
| [WMA](/indicators/trends_FIR/wma.md) | Weighted MA | Assigns linearly decreasing weights to older data points to reduce lag while maintaining effective noise filtering. |
