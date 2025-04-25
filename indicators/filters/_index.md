# Signal Filters

| Indicator                                       | Name                      | Description                                                                                           |
|-------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------|
| [BILATERAL](/indicators/filters/bilateral.md)   | Bilateral Filter          | Non-linear filter combining time and value weighting—smooths noise while preserving sharp moves.      |
| [BESSEL](/indicators/filters/bessel.md)         | Bessel Filter             | Maximally flat group delay filter, preserving waveform shape.                                         |
| [BUTTER](/indicators/filters/butter.md)         | Butterworth Filter        | Maximally flat magnitude response filter in the passband.                                             |
| [CHEBY1](/indicators/filters/cheby1.md)         | Chebyshev Type I Filter   | Steeper roll-off than Butterworth, allows passband ripple.                                            |
| [CHEBY2](/indicators/filters/cheby2.md)         | Chebyshev Type II Filter  | Steeper roll-off, allows stopband ripple, flat passband.                                              |
| [ELLIPTIC](/indicators/filters/elliptic.md)     | Elliptic (Cauer) Filter   | Steepest roll-off, allows ripple in both passband and stopband.                                       |
| [EHBPF](/indicators/filters/ehbpf.md)           | Ehlers Bandpass Filter    | Cascaded highpass and lowpass filter combination to isolate frequency components within a specific range. |
| [EHHPF](/indicators/filters/ehhpf.md)           | Ehlers Highpass Filter    | Removes low-frequency components (trend) while preserving high-frequency signals, using optimized coefficients. |
| [EHLP](/indicators/filters/ehlp.md)             | Ehlers Lowpass Filter     | Removes high-frequency components (noise) while preserving low-frequency signals (trend).             |
| [EHSSF](/indicators/filters/ehssf.md)           | Ehlers Supersmooth Filter | Optimized lowpass filter providing superior noise reduction with minimal lag using cascaded pole pairs. |
| [EHUSF](/indicators/filters/ehusf.md)           | Ehlers Ultrasmooth Filter | Advanced smoothing algorithm providing exceptional noise reduction with minimal lag using optimized coefficients. |
| GAUSS                                 | Gaussian Filter           | Symmetric FIR filter using a Gaussian kernel—provides smooth, edge-preserving low-pass behavior with no ripples in the passband. |
| HP                                    | Hodrick-Prescott Filter   | Decomposes a time series into trend and cyclical components.                                          |
| KF                                    | Kalman Filter             | Optimal recursive algorithm for estimating system state from noisy measurements.                      |
| KFS                                   | Kalman Filter Slope       | Estimates the slope (rate of change) using a Kalman filter variant.                                   |
| LOESS                                 | LOESS/LOWESS Smoothing    | Locally weighted polynomial regression smoothing that adapts to short-term trends.                    |
| MAAF                                  | MA Adaptive Filter        | Moving average filter whose parameters adapt based on input signal characteristics.                   |
| MEDIAN                                | Median Filter             | Non-linear filter replacing each point with the median of its neighbors—excellent for removing spikes. |
| NOTCH                                 | Notch Filter              | Narrow band-stop filter to remove periodic market-microstructure noise without disturbing trend.      |
| SGF                                   | Savitzky-Golay Filter     | Smoothing filter based on local polynomial regression. Preserves higher moments.                     |
| WIENER                                | Wiener Filter             | Optimal MSE linear filter that adapts to local signal/noise levels for noise reduction.               |
