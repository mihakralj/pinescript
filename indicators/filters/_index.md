# Signal Filters

This collection provides advanced signal filtering techniques adapted for financial market analysis. These filters offer superior noise reduction and signal extraction capabilities compared to traditional moving averages, with various specialized characteristics for different analytical needs.

## Ehlers Filters

| Indicator | Name | Key Characteristics |
|-----------|------|---------------------|
| [EHSSF](/indicators/filters/ehssf.md) | Ehlers Super Smooth Filter | Exceptional noise reduction with minimal lag using optimized pole placement |
| [EHUSF](/indicators/filters/ehusf.md) | Ehlers Ultra Smooth Filter | Maximum noise suppression for major trend identification in volatile markets |
| [EHBPF](/indicators/filters/ehbpf.md) | Ehlers Bandpass Filter | Isolates specific frequency ranges to detect cycles and rhythmic patterns |
| [EHHPF](/indicators/filters/ehhpf.md) | Ehlers Highpass Filter | Removes trends while preserving shorter-term movements for mean reversion strategies |

## Classic Digital Filters

| Indicator | Name | Key Characteristics |
|-----------|------|---------------------|
| [BESSEL](/indicators/filters/bessel.md) | Bessel Filter | Preserves signal shape with maximally flat group delay and minimal waveform distortion |
| [BUTTER](/indicators/filters/butter.md) | Butterworth Filter | Maximally flat magnitude response in passband with good roll-off characteristics |
| [CHEBY1](/indicators/filters/cheby1.md) | Chebyshev Type I Filter | Steeper roll-off than Butterworth with controlled passband ripple |
| [CHEBY2](/indicators/filters/cheby2.md) | Chebyshev Type II Filter | Maximally flat passband with ripples in stopband for efficient noise reduction |
| [ELLIPTIC](/indicators/filters/elliptic.md) | Elliptic (Cauer) Filter | Steepest possible roll-off with controlled ripples in both bands |

## Adaptive and Non-Linear Filters

| Indicator | Name | Key Characteristics |
|-----------|------|---------------------|
| [BILATERAL](/indicators/filters/bilateral.md) | Bilateral Filter | Edge-preserving non-linear filter that maintains significant price transitions |
| MEDIAN | Median Filter | Non-linear filter that removes spikes and outliers while preserving edges |
| KF | Kalman Filter | Optimal recursive estimator that adapts to changing market dynamics |
| WIENER | Wiener Filter | Optimizes signal-to-noise ratio based on statistical characteristics |

## Specialized Analysis Filters  

| Indicator | Name | Key Characteristics |
|-----------|------|---------------------|
| HP | Hodrick-Prescott Filter | Decomposes price into trend and cyclical components |
| LOESS | LOESS/LOWESS Smoothing | Locally weighted regression that adapts to non-linear patterns |
| SGF | Savitzky-Golay Filter | Polynomial regression-based filter that preserves higher moments |
| GAUSS | Gaussian Filter | Provides smooth, edge-preserving low-pass filtering with bell-shaped weights |
| NOTCH | Notch Filter | Removes specific frequency components while leaving others intact |
