# Signal Filters

| Indicator  | Name                                    | Status | Description                                                  |
|------------|----------------------------------------|--------|---------------------------------------------------------------|
| BESSEL     | Bessel Filter              | ❌     | Linear phase filter with adjustable cutoff frequency          |
| BUTTER     | Butterworth Filter         | ❌     | Classic n-pole DSP filter with selectable cutoff              |
| CHEBY1     | Chebyshev Type I Filter    | ❌     | Equiripple passband, flat stopband, variable cutoff          |
| CHEBY2     | Chebyshev Type II Filter   | ❌     | Flat passband, equiripple stopband, variable cutoff          |
| ELLIP      | Elliptic (Cauer) Filter    | ❌     | Equiripple both bands with adjustable transition width       |
| FIR        | Finite Impulse Response    | ❌     | Linear phase filter with configurable frequency response      |
| IIR        | Infinite Impulse Response  | ❌     | Recursive filter with adjustable frequency characteristics    |
| CWT        | Continuous Wavelet Transform| ❌     | Time-frequency analysis with variable resolution             |
| DWT        | Discrete Wavelet Transform  | ❌     | Multi-resolution analysis using wavelet decomposition        |
| EACP       | Ehlers Autocorrelation Periodogram | ❌ | Advanced cycle detection using autocorrelation             |
| [EHBPF](./indicators/filters/ehbpf.md)      | Ehlers Bandpass Filter                 | ✔️     | Combines highpass and lowpass for frequency band isolation    |
| [EHHPF](./indicators/filters/ehhpf.md)      | Ehlers Highpass Filter                 | ✔️     | Isolates high-frequency components of price movement          |
| [EHLP](./indicators/filters/ehlp.md)       | Ehlers Lowpass Filter      | ✔️     | Smooths price data while preserving trend components          |
| [EHUSF](./indicators/filters/ehusf.md)    | Ehlers Ultrasmooth Filter  | ✔️     | Advanced smoothing with optimized coefficients                |
| HOMOD      | Homodyne Discriminator     | ❌     | Cycle detection using phase discrimination                    |
| HP         | Hodrick-Prescott Filter    | ❌     | Trend extraction filter popular in quantitative analysis      |
| HWC        | Holt-Winters Channel       | ❌     | Adaptive bands based on triple exponential smoothing          |
| KF         | Kalman Filter              | ❌     | Optimal estimation filter for noisy data                       |
| KFS        | Kalman Filter Slope        | ❌     | Measures the derivative of the Kalman Filter output           |
| LF         | Laguerre Filter            | ❌     | Low-pass filter with near-zero lag, Ehlers-approved           |
| MAAF       | MA Adaptive Filter         | ❌     | Advanced adaptive filtering technique                          |
| SGF        | Savitzky-Golay Filter     | ❌     | Polynomial FIR smoother for curve smoothing                   |
| SSF        | Super Smoother Filter      | ❌     | Ehlers' advanced noise reduction filter                       |
