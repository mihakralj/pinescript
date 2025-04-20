# Finite Impulse Response (FIR) Trends and Predictors

Finite Impulse Response (FIR) indicators use a fixed window of price data points and have a finite memory of past inputs. They compute outputs based solely on inputs within that window, making them mathematically predictable with deterministic frequency-domain characteristics.

| Indicator  | Name                                    | Status | Description                                                  |
|------------|----------------------------------------|--------|---------------------------------------------------------------|
| AFIRMA     | Adaptive Finite Impulse Response MA     | ❌     | Uses finite impulse response filtering                       |
| [ALMA](/indicators/trends_FIR/alma.md)       | Arnaud Legoux MA                       | ✔️     | Uses Gaussian distribution for weights                       |
| [DWMA](/indicators/trends_FIR/dwma.md)       | Double Weighted MA                     | ✔️     | Double-weighted method for improved smoothing                |
| [EPMA](/indicators/trends_FIR/epma.md)       | Endpoint MA                            | ✔️     | Basic average emphasizing recent endpoints                   |
| [HMA](/indicators/trends_FIR/hma.md)        | Hull MA                                | ✔️     | Reduced lag WMA with trend emphasis                          |
| [HWMA](/indicators/trends_FIR/hwma.md)       | Holt Weighted MA                       | ✔️     | Uses finite window with Holt's method                        |
| [PWMA](/indicators/trends_FIR/pwma.md)       | Pascal Weighted MA                     | ✔️     | A MA that uses Pascal's triangle coefficients                |
| [SMA](/indicators/trends_FIR/sma.md)        | Simple MA                              | ✔️     | Basic arithmetic mean of signal over N periods               |
| [SINEMA](/indicators/trends_FIR/sinema.md)     | Sine-weighted MA                       | ✔️     | Uses sine function for weight distribution                   |
| SWMA       | Symmetric Weighted MA                  | ❌     | Balanced weight distribution MA                              |
| [TRIMA](/indicators/trends_FIR/trima.md)      | Triangular MA                          | ✔️     | Double-smoothed SMA with triangular weight distribution      |
| [WMA](/indicators/trends_FIR/wma.md)        | Weighted MA                            | ✔️     | Linear-weighted average giving more weight to recent signals |
