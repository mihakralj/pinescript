# Infinite Impulse Response (IIR) Trends and Predictors

Infinite Impulse Response (IIR) indicators use recursive implementations that technically depend on all past inputs through feedback loops, making them computationally efficient but with more complex frequency responses. IIR indicators typically have lower computational requirements than their FIR counterparts of similar performance.

| Indicator  | Name                                    | Status | Description                                                  |
|------------|----------------------------------------|--------|---------------------------------------------------------------|
| [DEMA](/indicators/trends_IIR/dema.md)       | Double Exponential MA                  | ✅     | Reduced lag double EMA                                      |
| [DSMA](/indicators/trends_IIR/dsma.md)       | Deviation-Scaled MA                    | ✅     | Adaptive filter that scales based on volatility              |
| [EMA](/indicators/trends_IIR/ema.md)        | Exponential MA                         | ✅     | Weighted average with exponential decay                      |
| [FRAMA](/indicators/trends_IIR/frama.md)      | Fractal Adaptive MA                    | ✅     | Uses fractal dimension for adaptation                        |
| [HEMA](/indicators/trends_IIR/hema.md)       | Hull Exponential MA                    | ✅     | Hull-based smoothing using EMA instead of WMA                |
| HTIT       | Hilbert Transform Instantaneous Trend   | ❌     | Based on Hilbert Transform                                   |
| [JMA](/indicators/trends_IIR/jma.md)        | Jurik MA                               | ✅     | Complex smoothing with minimal lag                           |
| [KAMA](/indicators/trends_IIR/kama.md)       | Kaufman Adaptive MA                    | ✅     | Adapts to market noise using efficiency ratio                |
| MAMA       | MESA Adaptive MA                       | ❌     | Complex cycle analysis using MESA                            |
| GMA        | Gaussian MA                            | ❌     | Based on normal distribution                                 |
| LTMA       | Linear Time MA                         | ❌     | Uses linear regression over time                             |
| MGDI       | McGinley Dynamic Indicator             | ❌     | Price momentum based dynamic average                         |
| [MMA](/indicators/trends_IIR/mma.md)        | Modified MA                            | ✅     | Modified version of EMA with different weighting             |
| [QEMA](/indicators/trends_IIR/qema.md)       | Quadruple Exponential MA               | ✅     | Simplified EMA calculation                                   |
| [REMA](/indicators/trends_IIR/rema.md)       | Regularized Exponential MA             | ✅     | Optimized EMA using regularization                           |
| [RMA](/indicators/trends_IIR/rma.md)        | wildeR MA                              | ✅     | Variation of EMA with different smoothing factor             |
| SMMA       | Smoothed MA                            | ❌     | Smoothed version of simple MA                                |
| [T3](/indicators/trends_IIR/t3.md)         | Tillson T3 MA                          | ✅     | Tim Tillson's improved triple EMA                            |
| [TEMA](/indicators/trends_IIR/tema.md)       | Triple Exponential MA                  | ✅     | Further reduced lag triple EMA                               |
| VIDYA      | Variable Index Dynamic Average         | ❌     | Volatility-based dynamic average                             |
| VWAP       | Volume Weighted Average Price          | ❌     | Price average weighted by volume                             |
| VWMA       | Volume Weighted MA                     | ❌     | MA weighted by volume                                        |
| WCP        | Weighted Closing Price                 | ❌     | Price calculation with emphasis on closing price             |
| [ZLDEMA](/indicators/trends_IIR/zldema.md)     | Zero-Lag Double Exponential MA         | ✅     | Advanced DEMA with lag reduction                             |
| [ZLEMA](/indicators/trends_IIR/zlema.md)      | Zero-Lag Exponential MA                | ✅     | EMA with minimal lag                                         |
| [ZLTEMA](/indicators/trends_IIR/zltema.md)     | Zero-Lag Triple Exponential MA         | ✅     | Advanced TEMA with lag reduction                             |
