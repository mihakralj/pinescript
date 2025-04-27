# BILATERAL: Bilateral Filter

[Pine Script Implementation of BILATERAL](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/bilateral.pine)

## Overview and Purpose

The Bilateral Filter is an edge-preserving smoothing technique that combines spatial filtering with intensity filtering to achieve noise reduction while maintaining significant price structure. Originally developed in computer vision for image processing, this adaptive filter has been adapted for financial time series analysis to provide superior smoothing that preserves important market transitions. The filter intelligently reduces noise in stable price regions while preserving sharp transitions like breakouts, reversals, and other significant market structures that would be blurred by conventional filters.

## Core Concepts

* **Dual-domain filtering:** Combines traditional time-based (spatial) filtering with value-based (range) filtering for adaptive smoothing
* **Edge preservation:** Maintains important price transitions while aggressively smoothing areas of minor fluctuation
* **Adaptive processing:** Automatically adjusts filtering strength based on local price characteristics

The core innovation of the Bilateral Filter is its ability to distinguish between random noise and significant price movements. Unlike conventional filters that smooth everything equally, Bilateral filtering preserves major price transitions by reducing the influence of price points that differ significantly from the current price, effectively preserving market structure while still eliminating noise.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback window size | Increase for more context in filtering decisions, decrease for quicker response |
| Sigma_S_Ratio | 0.3 | Controls spatial (time) weighting | Lower values emphasize recent bars, higher values distribute influence more evenly |
| Sigma_R_Mult | 2.0 | Controls range (price) sensitivity | Lower values increase edge preservation, higher values increase smoothing |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For breakout trading strategies, try reducing Sigma_R_Mult to 1.0-1.5 to make the filter more sensitive to significant price moves, allowing it to preserve breakout signals while still filtering noise.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Bilateral Filter calculates a weighted average of nearby prices, where the weights depend on two factors: how far away in time the price point is (spatial weight) and how different the price value is (range weight). Points that are close in time AND similar in value get the highest weight. This means stable price regions get smoothed while significant changes are preserved.

**Technical formula:**
BF[p] = (1 / Wp) × Σ_{q ∈ S} G_s(||p - q||) × G_r(|I[p] - I[q]|) × I[q]

Where:
- G_s is the spatial Gaussian kernel: exp(-||p - q||² / (2 × σ_s²))
- G_r is the range Gaussian kernel: exp(-|I[p] - I[q]|² / (2 × σ_r²))
- Wp is the normalization factor (sum of all weights)

> 🔍 **Technical Note:** The sigma_r parameter is typically calculated dynamically based on local price volatility (standard deviation) to provide adaptive filtering - this automatically adjusts filtering strength based on market conditions.

## Interpretation Details

The Bilateral Filter can be applied in various trading contexts:

* **Trend identification:** Reveals cleaner underlying price direction by removing noise while preserving trend changes
* **Support/resistance identification:** Provides clearer price levels by preserving significant turning points
* **Pattern recognition:** Maintains critical chart patterns while eliminating distracting minor fluctuations
* **Breakout trading:** Preserves sharp price transitions for more reliable breakout signals
* **Pre-processing:** Can be used as an initial filter before applying other technical indicators to reduce false signals

## Limitations and Considerations

* **Computational complexity:** More intensive calculations than traditional linear filters
* **Parameter sensitivity:** Performance highly dependent on proper parameter selection
* **Non-linearity:** Non-linear behavior may produce unexpected results in certain market conditions
* **Interpretation adjustment:** Requires different interpretation than conventional moving averages
* **Complementary tools:** Best used alongside volume analysis and traditional indicators for confirmation

## References

* Tomasi, C. and Manduchi, R. "Bilateral Filtering for Gray and Color Images," Proceedings of IEEE ICCV, 1998
* Paris, S. et al. "A Gentle Introduction to Bilateral Filtering and its Applications," ACM SIGGRAPH, 2008
