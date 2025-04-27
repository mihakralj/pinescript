# HTIT: Hilbert Transform Instantaneous Trendline

[Pine Script Implementation of HTIT](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/htit.pine)

## Overview and Purpose

The Hilbert Transform Instantaneous Trendline (HTIT) is a technical indicator developed by John Ehlers that utilizes digital signal processing techniques to identify market cycles and trends. HTIT applies the Hilbert Transform to isolate the trend component of price data, creating a trendline that adapts to changing market conditions with reduced lag compared to traditional moving averages.

What makes HTIT notable is its combined filter structure, which integrates Finite Impulse Response (FIR) filter elements within an Infinite Impulse Response (IIR) framework. This design helps the indicator balance responsiveness with noise reduction while tracking the underlying trend.

## Core Concepts

HTIT applies several key signal processing principles to market data:

* **Hilbert Transform application:** Generates in-phase (I) and quadrature (Q) components from price data, enabling cycle analysis
* **Cycle-based adaptation:** Automatically adjusts to the dominant market cycle period detected in the data
* **Phase measurement:** Uses phase relationships between I/Q components to identify trend direction and strength
* **Combined filter design:** Implements both FIR components for linear phase response and IIR elements for efficient feedback processing

HTIT achieves its performance through a multi-stage calculation process that analyzes cyclical components in price data, measures their phase relationships, and produces a trend estimation that reflects the current market direction with reduced delay.

## Calculation and Mathematical Foundation

The HTIT calculation combines several distinct processing stages:

1. **Initial Smoothing (FIR-like):** 
   - Price and smoothed price calculations use weighted averaging:
   ```
   price = (4 × source + 3 × source[1] + 2 × source[2] + source[3]) / 10
   smooth = (4 × price + 3 × price[1] + 2 × price[2] + price[3]) / 10
   ```

2. **Hilbert Transform Components (FIR):** 
   - Detrender and quadrature calculations use fixed coefficients:
   ```
   detrender = (0.0962 × smooth + 0.5769 × smooth[2] - 0.5769 × smooth[4] - 0.0962 × smooth[6]) × padAdj
   Q1 = (0.0962 × detrender + 0.5769 × detrender[2] - 0.5769 × detrender[4] - 0.0962 × detrender[6]) × padAdj
   ```

3. **Adaptive Elements (IIR):** 
   - Smoothing operations use recursive feedback:
   ```
   I2 = 0.2 × (I1 - jQ) + 0.8 × I2[1]
   Q2 = 0.2 × (Q1 + jI) + 0.8 × Q2[1]
   ```

4. **Period Estimation and Final Output:** 
   - Dominant cycle detection and trend calculation:
   ```
   periodEst = max(6, min(50, 0.2 × newP + 0.8 × periodEst))
   currentITrend = 0.9 × newITrendComponent + 1.1 × currentITrend1 - 1.0 × currentITrend2
   ```

> 🔍 **Technical Note:** HTIT combines properties of both FIR and IIR filters. The Hilbert Transform components use linear-phase FIR structures, while adaptive period estimation and final smoothing employ feedback-based IIR designs. This creates a hybrid approach that leverages advantages from both filter types.

## Interpretation Details

HTIT provides several useful insights for traders:

- When price crosses above HTIT, it often indicates the beginning of an uptrend
- When price crosses below HTIT, it often indicates the beginning of a downtrend
- The slope of HTIT helps determine trend strength and momentum
- HTIT tends to remain flat during sideways or consolidation periods
- The indicator adapts automatically to different market cycle periods

HTIT is particularly useful for trend identification and can help determine when a market is trending versus when it's moving sideways. The indicator's reduced lag compared to standard moving averages allows for earlier identification of potential trend changes.

## Limitations and Considerations

* **Calculation complexity:** More mathematically involved than simple moving averages, requiring multiple calculation stages
* **Sensitivity to noise:** Can react to short-term price fluctuations in particularly volatile markets
* **Potential overshooting:** May occasionally overshoot price during sharp reversals
* **Learning curve:** Understanding how the indicator works requires some knowledge of signal processing concepts
* **Parameter interpretation:** While adaptive, proper interpretation requires familiarity with cycle analysis

## References

1. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons.
2. Ehlers, J. (2004). *Cybernetic Analysis for Stocks and Futures*. John Wiley & Sons.
3. Ehlers, J. Various articles in *Technical Analysis of Stocks & Commodities* magazine.
