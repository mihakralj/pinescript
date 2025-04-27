# CHEBY2: Chebyshev Type II Filter

[Pine Script Implementation of CHEBY2](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/cheby2.pine)

## Overview and Purpose

The Chebyshev Type II Filter, also known as the Inverse Chebyshev filter, is an advanced signal processing tool that offers maximally flat response in the passband and controlled ripples in the stopband. Developed based on Pafnuty Chebyshev's mathematical work, this filter achieves steeper roll-off than Butterworth filters while maintaining smooth passband characteristics. This implementation provides a 2nd-order low-pass filter with 1dB passband ripple and 40dB stopband attenuation, designed to effectively remove high-frequency market noise while maintaining the integrity of trend signals, making it valuable for traders seeking clean signals without distorting the main price trends.

## Core Concepts

* **Flat passband:** Maintains signal integrity in the frequency range of interest with maximally flat passband response
* **Stopband ripple control:** Achieves steeper roll-off by allowing controlled ripples in frequencies outside the passband
* **Market application:** Particularly effective for trend following strategies where maintaining signal integrity is crucial while still requiring effective noise removal

The core innovation of the Chebyshev Type II filter is its inverse approach to the Type I design - by moving ripples from the passband to the stopband, it delivers superior performance for financial time series where preserving the exact shape of trend signals is critical while still needing effective noise reduction.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the cutoff period | Increase for smoother signals, decrease for more responsiveness |
| Attenuation | 40 | Controls stopband attenuation (dB) | Higher values provide more noise suppression but may increase ringing |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** When used for trend identification, a length setting approximately 1.5× your typical trade duration often provides optimal results - for example, use a 15-period filter for strategies with 10-bar average holding periods.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Chebyshev Type II filter calculates a smoothed output that preserves important trend information while effectively removing market noise. Unlike Type I filters, it keeps the passband (important frequencies) maximally flat while concentrating ripples in the stopband (noise frequencies), resulting in clean signals that maintain the integrity of significant price movements.

**Technical formula:**
Implemented as a 2nd-order IIR filter:

y[n] = B0 × x[n] + B1 × x[n-1] + B2 × x[n-2] - A1 × y[n-1] - A2 × y[n-2]

Where coefficients are derived through a complex process involving:
- ε = 1 / sqrt(10^(Rs/10) - 1) (inverse of Type I epsilon calculation)
- The placement of zeros on the imaginary axis: omega_z = Wc / cos(π/(2n))
- Calculation of poles similar to Type I but with the inverse epsilon

> 🔍 **Technical Note:** Unlike Chebyshev Type I which has all poles and no finite zeros, Type II has finite zeros that create the stopband notches. These zeros are placed on the imaginary axis to achieve the optimal attenuation characteristics.

## Interpretation Details

The Chebyshev Type II filter can be used in various trading strategies:

* **Trend identification:** Reveals underlying price direction with minimal distortion of the trend component
* **Signal generation:** Crossovers between price and filtered output generate cleaner trade signals
* **Support/resistance levels:** Creates more reliable dynamic support and resistance levels with less noise
* **Multiple timeframe analysis:** Apply filters with different cutoff periods to identify trends across various time horizons
* **Pattern recognition:** Improves the reliability of chart pattern identification by removing distracting noise

## Limitations and Considerations

* **Stopband ripple:** May not completely eliminate all frequency components in the stopband due to ripple structure
* **Moderate phase distortion:** Better than Type I but still exhibits some non-linear phase characteristics
* **Transient response:** May exhibit moderate ringing or overshoot when responding to sharp price changes
* **Computational complexity:** More involved calculations than simple moving averages or Butterworth filters
* **Complementary tools:** Best used alongside momentum indicators and volume analysis for confirmation

## References

* Parks, T.W. and Burrus, C.S. "Digital Filter Design," Wiley, 1987
* Daniels, R.W. "Approximation Methods for Electronic Filter Design," McGraw-Hill, 1974
