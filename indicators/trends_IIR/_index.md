# Infinite Impulse Response (IIR) Trends and Predictors

| Indicator | Name | Description |
| ------------ | ---------------------------------------- | ---------------------------------------- |
| [DEMA](/indicators/trends_IIR/dema.md) | Double Exponential MA | Reduces lag by applying double exponential smoothing, enhancing responsiveness while maintaining signal quality. |
| [DSMA](/indicators/trends_IIR/dsma.md) | Deviation-Scaled MA | Adaptive IIR filter that adjusts its smoothing factor based on market volatility, increasing responsiveness during high-deviation periods. |
| [EMA](/indicators/trends_IIR/ema.md) | Exponential MA | Applies exponentially decreasing weights to price data, balancing responsiveness and stability. |
| [FRAMA](/indicators/trends_IIR/frama.md) | Fractal Adaptive MA | Adapts smoothing based on fractal dimension analysis, minimizing lag in trends and maximizing smoothing in consolidation. |
| [HEMA](/indicators/trends_IIR/hema.md) | Hull Exponential MA | Hybrid of Hull and exponential moving averages using logarithmic coefficient distribution and cubic acceleration for reduced lag and noise suppression. |
| [HTIT](/indicators/trends_IIR/htit.md) | Hilbert Transform Instantaneous Trend | Utilizes Hilbert Transform to isolate the instantaneous trend component, providing a zero-lag trendline with hybrid FIR-in-IIR design. |
| [JMA](/indicators/trends_IIR/jma.md) | Jurik MA | Adaptive filter achieving high noise reduction and low phase delay through multi-stage volatility normalization and dynamic parameter optimization. |
| [KAMA](/indicators/trends_IIR/kama.md) | Kaufman Adaptive MA | Automatically adjusts sensitivity based on market volatility using an Efficiency Ratio, balancing responsiveness and stability. |
| [LTMA](/indicators/trends_IIR/ltma.md) | Linear Trend MA | Projects the linear trend of price data using linear regression, focusing on the endpoint of the trendline. |
| [MAMA](/indicators/trends_IIR/mama.md) | MESA Adaptive MA | Applies Hilbert Transform for phase-based adaptation, using a dual-line system (MAMA/FAMA) for cycle-sensitive smoothing. |
| [MGDI](/indicators/trends_IIR/mgdi.md) | McGinley Dynamic Indicator | Adjusts speed based on market volatility using a dynamic factor, aiming to hug prices closely. |
| [MMA](/indicators/trends_IIR/mma.md) | Modified MA | Combines simple and weighted components, emphasizing central values for balanced smoothing. |
| [QEMA](/indicators/trends_IIR/qema.md) | Quadruple Exponential MA | Four-stage cascade architecture for superior lag reduction and noise suppression through progressive smoothing optimization. |
| [REMA](/indicators/trends_IIR/rema.md) | Regularized Exponential MA | Applies regularization to EMA using a lambda parameter, balancing smoothing and momentum-based prediction. |
| [RGMA](/indicators/trends_IIR/rgma.md) | Recursive Gaussian MA | Approximates Gaussian smoothing by recursively applying EMA filters multiple times (passes), controlled by an adjusted period. |
| [RMA](/indicators/trends_IIR/rma.md) | wildeR MA (SMMA, MMA)| Wilder's smoothing average using a specific alpha (1/period), designed for indicators like RSI and ATR. |
| [T3](/indicators/trends_IIR/t3.md) | Tillson T3 MA | Six-stage EMA cascade with optimized coefficients based on a volume factor for reduced lag and superior noise reduction. |
| [TEMA](/indicators/trends_IIR/tema.md) | Triple Exponential MA | Triple-cascade EMA architecture with optimized coefficients (3, -3, 1) for further lag reduction compared to DEMA. |
| [VIDYA](/indicators/trends_IIR/vidya.md) | Variable Index Dynamic Average | Adjusts smoothing factor based on market volatility using a Volatility Index (ratio of short-term to long-term standard deviation). |
| [ZLDEMA](/indicators/trends_IIR/zldema.md) | Zero-Lag Double Exponential MA | Hybrid dual-stage predictive architecture combining two ZLEMAs with optimized 1.5/0.5 coefficients for reduced lag and noise suppression. |
| [ZLEMA](/indicators/trends_IIR/zlema.md) | Zero-Lag Exponential MA | Reduces lag by estimating future price based on current momentum, using a dynamically calculated lag period. |
| [ZLTEMA](/indicators/trends_IIR/zltema.md) | Zero-Lag Triple Exponential MA | Advanced triple-cascade predictive architecture combining three ZLEMAs with optimized 2/2/1 coefficients for maximum lag reduction. |
