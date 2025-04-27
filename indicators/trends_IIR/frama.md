# FRAMA: Fractal Adaptive Moving Average

[Pine Script Implementation of FRAMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/frama.pine)

## Overview and Purpose

The Fractal Adaptive Moving Average (FRAMA) is an advanced technical indicator that automatically adjusts its smoothing factor based on the fractal dimension of price action. Developed by John Ehlers and introduced in 2005, FRAMA utilizes concepts from fractal geometry to identify market states and adapt accordingly.

Unlike traditional moving averages with fixed parameters, FRAMA becomes more responsive during trending markets and more stable during sideways or choppy conditions. This is achieved by measuring the "fractal dimension" of the price series - a mathematical concept that quantifies how "jagged" or "smooth" the market is behaving. This approach creates a moving average that effectively filters market noise while maintaining responsiveness to genuine trend changes.

## Core Concepts

* **Fractal dimension analysis:** Measures the complexity of price movement to determine market state (trending vs. choppy)
* **Dynamic alpha adjustment:** Automatically modifies the smoothing factor based on the calculated fractal dimension
* **Self-adapting behavior:** Becomes faster in trending markets and slower in consolidating markets without manual intervention
* **Market structure recognition:** Identifies and adapts to different market conditions through mathematical principles

FRAMA achieves its adaptive nature by analyzing how price occupies space across different timeframes - a fundamental concept in fractal geometry. By calculating normalized price ranges at different scales, it determines a fractal dimension that ranges from 1 (smooth, trending markets) to 2 (noisy, choppy markets). This dimension then controls how quickly the moving average responds to price changes.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 16 | Base calculation period (should be divisible by 4) | Increase for longer-term analysis, decrease for shorter-term signals |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** Many professional traders find that setting the period to a multiple of 4 between 16-32 provides the optimal balance of responsiveness and stability across most market conditions. The 16-period setting is often ideal for swing trading timeframes.

## Calculation and Mathematical Foundation

**Simplified explanation:**
FRAMA works by measuring how "fractal" (complex or jagged) the recent price action has been. When prices are moving in a clean trend, FRAMA responds quickly to price changes. When prices are choppy and directionless, FRAMA slows down dramatically to filter out the noise.

**Technical formula:**
1. Divide the observation period into segments and calculate normalized price ranges:
   - N₁ = [H(n/4) - L(n/4)] × 4/n (smallest segment)
   - N₂ = [H(n/2) - L(n/2)] × 2/n (medium segment)
   - N₃ = [H(n) - L(n)] × 1/n (full period segment)
   Where H and L are highest and lowest prices in the segment

2. Calculate the fractal dimension:
   - D = [ln(N₁ + N₂) - ln(N₂ + N₃)] / ln(2)

3. Determine the adaptive alpha:
   - α = e^(-4.6(D-1)), constrained to [0.01, 1]

4. Apply to standard EMA formula:
   - FRAMA = α × Price + (1-α) × Previous FRAMA

> 🔍 **Technical Note:** The fractal dimension calculation is based on concepts from the Hurst exponent, which measures the self-similarity of time series data. When D approaches 1, the market is trending smoothly; when D approaches 2, the market is random and choppy. The exponential function applied to D creates a non-linear response that emphasizes the difference between trending and non-trending states.

## Interpretation Details

FRAMA provides several key insights for traders:

- When price crosses above FRAMA, it often signals the beginning of an uptrend
- When price crosses below FRAMA, it often signals the beginning of a downtrend
- The slope of FRAMA provides insight into trend strength and momentum
- FRAMA's smoothness/jaggedness itself indicates market conditions - smooth FRAMA suggests a clean trend
- Multiple FRAMA lines with different periods can identify potential reversal zones

FRAMA is particularly valuable in markets that alternate between trending and consolidation phases. Its ability to automatically slow down during choppy conditions helps filter out false signals, while its increased responsiveness during trends helps capture more of the significant price moves.

## Limitations and Considerations

* **Period requirements:** Works best with periods divisible by 4 due to the segmentation in its calculation
* **Data requirements:** Needs sufficient historical data for accurate fractal dimension calculation
* **Calculation complexity:** More computationally intensive than simple moving averages
* **Transition delay:** May experience a slight delay when transitioning between different market states
* **Complementary tools:** Works best when combined with volume analysis or momentum indicators for confirmation

## References

1. Ehlers, J. (2005). "FRAMA – Fractal Adaptive Moving Average," *Technical Analysis of Stocks & Commodities*.
2. Ehlers, J. (2004). *Cybernetic Analysis for Stocks and Futures*. John Wiley & Sons.
3. Mandelbrot, B. (1982). *The Fractal Geometry of Nature*. W.H. Freeman and Company.
