# DSP Filters

| Indicator  | Name                                    | Status | Description                                                  |
|------------|----------------------------------------|--------|---------------------------------------------------------------|
| AFIRMA     | Adaptive FIR MA                        | ❌     | Uses finite impulse response filtering                         |
| DSMA       | Deviation-Scaled MA                    | ✅     | Adaptive filter that scales based on volatility               |
| EHBP       | Ehlers Bandpass Filter                 | ✅     | Combines highpass and lowpass for frequency band isolation    |
| EHHP       | Ehlers Highpass Filter                 | ✅     | Isolates high-frequency components of price movement          |
| EHLP       | Ehlers Lowpass Filter                  | ✅     | Smooths price data while preserving trend components          |
| EHUS       | Ehlers Ultrasmooth Filter              | ✅     | Advanced smoothing with optimized coefficients                |
| HWMA       | Holt-Winters MA                        | ✅     | Uses Hann window function for weighting                       |
| MAAF       | MA Adaptive Filter                     | ❌     | Advanced adaptive filtering technique                         |
| SSF        | Ehler's Super Smoother Filter          | ❌     | Advanced noise reduction filter                               |
