# Normalized Jurik Volatility (JVOLTYN)

The Normalized Jurik Volatility (JVOLTYN) indicator is a normalized volatility measure that uses adaptive techniques to adjust to market volatility. It employs Jurik's smoothing techniques to provide a less noisy and more responsive volatility estimate, normalized between 0 and 1.

[Pine Script Implementation of JVOLTYN](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/jvoltyn.pine)

## Mathematical Foundation

1. **Adaptive Volatility Calculation:** Calculates an initial volatility estimate based on the difference between the source series and upper/lower bands.
2. **Jurik Smoothing:** Applies Jurik smoothing to the volatility estimate to reduce noise and improve responsiveness.
3. **Normalization:** Normalizes the smoothed volatility to a value between 0 and 1 using a sigmoid function.

## Key Components

1. **Adaptive Smoothing:** Employs Jurik's smoothing algorithm to reduce noise and improve responsiveness.
2. **Volatility Bands:** Uses upper and lower bands to estimate volatility based on price deviations.
3. **Normalization:** Normalizes the volatility estimate to a value between 0 and 1.

## Advantages and Disadvantages

### Advantages

* **Reduced Noise:** Jurik smoothing helps to reduce noise and improve the accuracy of the volatility estimate.
* **Responsiveness:** Adaptive techniques allow the indicator to respond quickly to changes in market volatility.
* **Normalized Output:** The normalized output allows for easy comparison across different assets and time periods.

### Disadvantages

* **Complexity:** The JVOLTYN calculation is more complex than simple volatility measures.
* **Parameter Sensitivity:** The indicator's performance can be sensitive to the choice of parameters.
