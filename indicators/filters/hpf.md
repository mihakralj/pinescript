# HPF: Highpass Filter

[Pine Script Implementation of HPF](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/hpf.pine)

## Overview and Purpose

The Highpass Filter (HPF) is a specialized signal processing tool designed to remove low-frequency components (trends) from price data while preserving higher-frequency market movements. Developed by John Ehlers, a pioneer in applying digital signal processing to financial markets, this filter uses optimized coefficients to achieve excellent trend removal with minimal distortion of shorter-term price movements. Unlike moving averages which act as lowpass filters, HPF specifically isolates shorter-term market movements by suppressing longer-term trends, making it particularly valuable for identifying short-term trading opportunities regardless of the underlying trend direction.

## Core Concepts

* **Trend removal:** Effectively eliminates longer-term trends and drift components from price data
* **High-frequency preservation:** Maintains shorter-term market movements for analysis of oscillations and cycles
* **Market application:** Particularly useful for range-bound trading, mean reversion strategies, and cycle analysis

The core innovation of HPF is its optimized coefficient design that achieves sharp cutoff characteristics while minimizing unwanted artifacts like ringing or phase distortion. This allows traders to clearly see shorter-term market movements that might otherwise be obscured by dominant trends, enabling more precise identification of overbought/oversold conditions and short-term reversal points.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the cutoff period | Increase to remove more market components, decrease to preserve more market components |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For mean-reversion strategies, set the length parameter to approximately 2-3× your typical trade duration to filter out trends that exceed your trading timeframe while preserving actionable price movements.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The highpass filter works by calculating the difference between the current price and its recent average, highlighting rapid changes while suppressing slow-moving components. It uses carefully optimized coefficients to ensure clean separation between preserved and removed frequency components.

**Technical formula:**
HP = c1(X - 2X₁ + X₂) + c2×HP₁ + c3×HP₂

Where coefficients are calculated as:
- a1 = exp(-1.414π/length)
- b1 = 2a1 × cos(1.414 × 180/length)
- c1 = (1 + c2 - c3)/4
- c2 = b1
- c3 = -a1²

> 🔍 **Technical Note:** The filter uses a second-difference derivative term (X - 2X₁ + X₂) that inherently acts as a highpass filter, combined with feedback terms (HP₁, HP₂) that shape the frequency response for optimal performance.

## Interpretation Details

The Highpass Filter can be used in various trading contexts:

* **Mean reversion trading:** Identify overbought/oversold conditions when the filter output reaches extreme values
* **Cycle analysis:** Isolate market cycles by removing longer-term trends
* **Short-term reversal detection:** Zero-line crossings often indicate short-term direction changes
* **Divergence identification:** Compare filter output with price to spot potential reversal points
* **Volatility analysis:** Amplitude of filter output indicates short-term market volatility

## Limitations and Considerations

* **Center line oscillation:** Output oscillates around zero rather than tracking price levels
* **Initialization period:** Requires several bars to stabilize after the start of data
* **Not trend-following:** By design removes trend information, should not be used for trend following
* **Parameter sensitivity:** Performance depends on appropriate length selection for the market being analyzed
* **Complementary tools:** Best used alongside trend-identifying tools for complete market perspective

## References

* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
* Ehlers, J.F. "Rocket Science for Traders," Wiley, 2001
