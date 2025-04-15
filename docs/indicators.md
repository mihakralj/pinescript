# Moving Average Indicators

| Indicator | Name | Status | Description |
|-----------|------|--------|-------------|
| **Simple Complexity** |||
| SMA | Simple Moving Average | ✅ | Basic arithmetic mean of signal over N periods |
| EMA | Exponential Moving Average | ✅ | Weighted average with exponential decay |
| WMA | Weighted Moving Average | ✅ | Linear-weighted average giving more weight to recent signals |
| RMA | wildeR Moving Average | ✅ | Variation of EMA with different smoothing factor |
| TRIMA | Triangular Moving Average | ✅ | Double-smoothed SMA with triangular weight distribution |
| QEMA | Quadruple Exponential Moving Average | ✅ | Simplified EMA calculation |
| EPMA | Endpoint Moving Average | ✅ | Basic average emphasizing recent endpoints |
| SINEMA | Sine-weighted Moving Average | ✅ | Uses sine function for weight distribution |
| HWMA |Holt-Winters Moving Average | ✅ | Uses Hann window function for weighting |
| FWMA | Fibonacci Weighted Moving Average | ❌ | Forward-looking weighted calculation |
| PWMA | Pascal Weighted Moving Average | ✅ | A moving average that uses Pascal's triangle coefficients as weights |
| MMA | Modified Moving Average | ❌ | Modified version of EMA with different weighting |
| **Medium Complexity** |||
| DEMA | Double Exponential Moving Average | ✅ | Reduced lag double EMA |
| TEMA | Triple Exponential Moving Average | ✅ | Further reduced lag triple EMA |
| HMA | Hull Moving Average | ✅ | Reduced lag WMA with trend emphasis |
| DWMA | Dynamic Weighted Moving Average | ✅ | Adapts to market volatility |
| HEMA | Hull Exponential Moving Average | ✅ | Hull-based smoothing using EMA instead of WMA |
| ZLEMA | Zero-Lag Exponential Moving Average | ✅ | EMA with minimal lag |
| DSMA | Dynamic Simple Moving Average | ❌ | Adapts period based on volatility |
| REMA | Regularized Exponential Moving Average | ✅ | Optimized EMA using regularization |
| LTMA | Linear Time Moving Average | ❌ | Uses linear regression over time |
| GMA | Gaussian Moving Average | ❌ | Based on normal distribution |
| MGDI | McGinley Dynamic Indicator | ❌ | Price momentum based dynamic average |
| T3 | Triple Exponential Moving Average (T3) | ❌ | Tim Tillson's improved triple EMA |
| VIDYA | Variable Index Dynamic Average | ❌ | Volatility-based dynamic average |
| **Complex Implementation** |||
| ZLDEMA | Zero-Lag Double Exponential Moving Average | ✅ | Advanced DEMA with lag reduction |
| ZLTEMA | Zero-Lag Triple Exponential Moving Average | ✅ | Advanced TEMA with lag reduction |
| KAMA | Kaufman Adaptive Moving Average | ❌ | Adapts to market noise using efficiency ratio |
| ALMA | Arnaud Legoux Moving Average | ❌ | Uses Gaussian distribution for weights |
| FRAMA | Fractal Adaptive Moving Average | ❌ | Uses fractal dimension for adaptation |
| JMA | Jurik Moving Average | ✅ | Complex smoothing with minimal lag |
| AFIRMA | Adaptive FIR Moving Average | ❌ | Uses finite impulse response filtering |
| MAAF | Moving Average Adaptive Filter | ❌ | Advanced adaptive filtering technique |
| MAMA | MESA Adaptive Moving Average | ❌ | Complex cycle analysis using MESA |
| HTIT | Hilbert Transform Instantaneous Trendline | ❌ | Based on Hilbert Transform |
