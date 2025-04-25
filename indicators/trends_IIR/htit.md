# Hilbert Transform Instantaneous Trendline (HTIT)

## Introduction

The Hilbert Transform Instantaneous Trendline (HTIT) is an advanced moving average developed by John Ehlers. It utilizes the Hilbert Transform to isolate the instantaneous trend component of price data, aiming to provide a zero-lag trendline that adapts quickly to changing market conditions. HTIT is notable for its unique hybrid design, embedding Finite Impulse Response (FIR) filter stages within an overall Infinite Impulse Response (IIR) framework.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/htit.pine)

## Core Concepts

HTIT leverages signal processing techniques to analyze price cycles and extract the underlying trend:

- **Hilbert Transform**: Used to generate in-phase (I) and quadrature (Q) components of the price data, allowing for cycle analysis.
- **Instantaneous Trend**: Calculates the trend component based on the phase and amplitude derived from the I/Q components.
- **Adaptive Period Estimation**: Dynamically adjusts its internal period estimate based on the dominant cycle detected in the data.
- **Zero-Lag Filtering**: Employs specific filter structures to minimize lag compared to traditional moving averages.
- **Hybrid FIR-in-IIR Design**: Combines FIR filtering for core signal processing with IIR feedback loops for smoothing and adaptation.

## Mathematical Foundation & Hybrid Structure

HTIT's calculation involves several stages, blending FIR and IIR filtering techniques:

1. **Initial Smoothing (FIR-like)**: Price and smoothed price calculations use weighted averages, resembling short FIR filters.
    *price* = (4 × *source* + 3 × *source*\[1] + 2 × *source*\[2] + *source*\[3]) / 10
    *smooth* = (4 × *price* + 3 × *price*\[1] + 2 × *price*\[2] + *price*\[3]) / 10

2. **Hilbert Transform Components (FIR)**: The core detrending and I/Q calculations employ fixed-coefficient, linear-phase FIR filters using specific kernels (0.0962, 0.5769) over lookbacks. These are classic FIR stages with no feedback.
    *detrender* = (0.0962 × *smooth* + 0.5769 × *smooth*\[2] - 0.5769 × *smooth*\[4] - 0.0962 × *smooth*\[6]) × *padAdj*
    *Q1* = (0.0962 × *detrender* + 0.5769 × *detrender*\[2] - 0.5769 × *detrender*\[4] - 0.0962 × *detrender*\[6]) × *padAdj*
    (Similar calculations for *I1*, *jI*, *jQ*)

3. **Adaptive Smoothing & Homodyne Discriminator (IIR)**: The smoothing of *I2*/*Q2* and the calculation of *Re*/*Im* use recursive formulas (e.g., 0.2 × new + 0.8 × prev), which are first-order IIR filters (exponential smoothing).
    *I2* = 0.2 × (*I1* - *jQ*) + 0.8 × *I2*\[1]
    *Q2* = 0.2 × (*Q1* + *jI*) + 0.8 × *Q2*\[1]
    *Re* = 0.2 × (*I2* × *I2*\[1] + *Q2* × *Q2*\[1]) + 0.8 × *Re*\[1]
    *Im* = 0.2 × (*I2* × *Q2*\[1] - *Q2* × *I2*\[1]) + 0.8 × *Im*\[1]

4. **Period Estimation (IIR)**: The dominant cycle period (*periodEst*) is adaptively updated using an IIR smoothing approach.
    *periodEst* = max(6, min(50, 0.2 × *newP* + 0.8 × *periodEst*))

5. **Final Trend Filter (IIR)**: The final trendline (*iTrend*) calculation uses a 2-pole IIR filter structure involving the current component and the two previous trend values.
    *currentITrend* = 0.9 × *newITrendComponent* + 1.1 × *currentITrend1* - 1.0 × *currentITrend2*

**Conclusion**: The Hilbert Transform "engine" relies on FIR filters, but the adaptive period estimation and final trend smoothing wrap this engine in IIR feedback loops. Therefore, HTIT is neither pure FIR nor pure IIR but a sophisticated FIR-in-IIR hybrid design.

## Calculation Process Summary

1. Apply initial smoothing to the source price.
2. Calculate the detrended price using an FIR filter.
3. Compute the In-Phase (I1) and Quadrature (Q1) components using FIR filters.
4. Calculate adjusted I/Q components (jI, jQ) using FIR filters.
5. Smooth I1/Q1 into I2/Q2 using first-order IIR filters.
6. Calculate Real (Re) and Imaginary (Im) parts for the homodyne discriminator using IIR filters.
7. Estimate the dominant cycle period adaptively using IIR smoothing.
8. Calculate the phase angle and trend power.
9. Compute the raw new trend component.
10. Apply the final 2-pole IIR filter to generate the HTIT value.

## Advantages and Limitations

### Advantages

- **Reduced Lag**: Designed to follow price trends with minimal delay compared to conventional MAs.
- **Adaptability**: Automatically adjusts to the dominant cycle period in the market.
- **Trend Clarity**: Aims to provide a clear representation of the instantaneous trend.
- **Smoothness**: Incorporates smoothing stages to reduce noise.

### Limitations

- **Complexity**: The calculation is significantly more complex than standard moving averages.
- **Sensitivity**: Can be sensitive to sharp, non-cyclical price movements or noise.
- **Potential for Overshoot**: Like other adaptive or zero-lag filters, it might overshoot during abrupt reversals.
- **Parameter Interpretation**: While adaptive, understanding the internal mechanics requires signal processing knowledge.

## Sources

1. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons. (General Hilbert Transform concepts)
2. Ehlers, J. (2004). *Cybernetic Analysis for Stocks and Futures*. John Wiley & Sons. (Further discussion of cycle analysis and filters)
3. Ehlers, J. Various articles in *Technical Analysis of Stocks & Commodities* magazine. (Specific indicator details often appear here first).
