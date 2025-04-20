# Jurik Volatility (JVOLTY)

The Jurik Volatility (JVOLTY) indicator is a volatility measure that uses adaptive techniques to adjust to market volatility. It employs Jurik's smoothing techniques to provide a less noisy and more responsive volatility estimate.

[Pine Script Implementation of JVOLTY](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/jvolty.pine)

## Mathematical Foundation

The JVOLTY calculation involves several steps:

1. **Adaptive Volatility Calculation:** Calculates an initial volatility estimate based on the difference between the source series and upper/lower bands.
2. **Jurik Smoothing:** Applies Jurik smoothing to the volatility estimate to reduce noise and improve responsiveness.
3. **Normalization:** Normalizes the smoothed volatility to provide a relative measure of volatility.

## Key Components

1. **Adaptive Smoothing:** Employs Jurik's smoothing algorithm to reduce noise and improve responsiveness.
2. **Volatility Bands:** Uses upper and lower bands to estimate volatility based on price deviations.
3. **Normalization:** Normalizes the volatility estimate for comparison across different assets and time periods.

## Advantages and Disadvantages

### Advantages

* **Reduced Noise:** Jurik smoothing helps to reduce noise and improve the accuracy of the volatility estimate.
* **Responsiveness:** Adaptive techniques allow the indicator to respond quickly to changes in market volatility.
* **Relative Measure:** Normalization provides a relative measure of volatility that can be compared across different assets and time periods.

### Disadvantages

* **Complexity:** The JVOLTY calculation is more complex than simple volatility measures.
* **Parameter Sensitivity:** The indicator's performance can be sensitive to the choice of parameters.
