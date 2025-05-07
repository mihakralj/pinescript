# DMX: Directional Movement Index Extended

[Pine Script Implementation of DMX](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/dmx.pine)

## Overview and Purpose

DMX, created by Mark Jurik of Jurik Research, is the ultra-smooth, low-lag replacement for the classic DMI and ADX indicators. It combines two key innovations: a bipolar version of DMI that preserves directional information, and Jurik's JMA (Jurik Moving Average) for superior smoothing.

While the standard ADX is a slow and smooth version of the more basic and noisier DMI indicator, it relies on traditional moving averages that introduce significant lag. DMX solves this by using JMA smoothing, which provides cleaner signals with minimal lag. The traditional DMI is composed of two non-negative components (DMI+ and DMI-) that tend to be very jittery. ADX attempts to solve this by applying simple moving averages, but this introduces unwanted lag that delays analysis and induces late trades. DMX's combination of bipolar calculation and JMA smoothing provides both directional awareness and superior signal quality.

## Calculation and Mathematical Foundation

**Simplified explanation:**
DMX is a bipolar version of DMI smoothed with JMA (Jurik Moving Average). It removes the absolute value operator and applies JMA smoothing:

DMX = JMA((DMI↑ - DMI↓) / (DMI↑ + DMI↓))

This creates an indicator that shows both trend direction (positive/negative) and strength (distance from zero) while maintaining exceptional smoothness without lag.

**Technical formula:**
1. Calculate raw directional movements:
   * TR = max(high - low, |high - close₁|, |low - close₁|)
   * +DM = high - high₁ if (high - high₁) > (low₁ - low) and > 0, else 0
   * -DM = low₁ - low if (low₁ - low) > (high - high₁) and > 0, else 0

2. Apply JMA smoothing to raw components:
   * TR_smooth = JMA(TR)
   * +DM_smooth = JMA(+DM)
   * -DM_smooth = JMA(-DM)

3. Calculate directional indicators:
   * +DI = 100 × +DM_smooth / TR_smooth
   * -DI = 100 × -DM_smooth / TR_smooth

4. Calculate raw DMX:
   * Raw DMX = 100 × (+DI - -DI) / (+DI + -DI)

5. Apply final JMA smoothing:
   * Final DMX = JMA(Raw DMX)

## Core Innovation

DMX introduces two key improvements:

* **Bipolar Calculation:** Unlike DMI which uses absolute values, DMX preserves the sign of directional movement, allowing it to indicate both trend direction and strength in a single value.

* **JMA Integration:** DMX uses Jurik's Moving Average (JMA) with consistent parameters across all smoothing operations:
  - Direct smoothing of raw components (TR, +DM, -DM)
  - Final smoothing of the DMX value
  - Power parameter of 0.2 for optimal balance between smoothness and responsiveness

## Advantages Over Traditional Indicators

1. **No Smoothing Required:** While DMI is jagged (noisy) and ADX requires smoothing that adds lag, DMX provides clean signals directly.
2. **Faster Detection:** Offers the ability to detect true market direction faster and with greater accuracy.
3. **Dual Information:** Combines direction and strength in a single value, eliminating the need for separate DMI+/DMI- interpretation.
4. **Reduced Lag:** Eliminates the lag introduced by moving averages used in ADX calculations.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Base calculation period | Rarely needs adjustment due to DMX's inherent smoothness |

**Pro Tip:** Because DMX is inherently smooth, there's typically no need to adjust the default parameters or apply additional smoothing techniques.

## Interpretation Details

* **Positive Values:** Indicate upward trends
* **Negative Values:** Indicate downward trends
* **Magnitude:** Distance from zero indicates trend strength
* **Zero Crossings:** Signal potential trend reversals
* **Color Coding:** Green for positive (upward) movement, red for negative (downward) movement

## Key Benefits

1. **Superior Smoothness:** Provides clean signals without additional smoothing
2. **Reduced Lag:** More timely signals compared to traditional DMI/ADX
3. **Clear Direction:** Bipolar nature clearly shows trend direction
4. **Fast Response:** Quickly adapts to rapid market moves
5. **Simplified Analysis:** No need to compare multiple lines (DMI+/DMI-) or wait for smoothed ADX

## Conclusion

DMX, a creation of Jurik Research, represents a significant improvement over traditional directional indicators. By eliminating the need for additional smoothing while maintaining signal clarity, it makes both DMI and ADX obsolete. Its ability to provide clean, responsive signals makes it particularly valuable for detecting market direction changes in real-time trading conditions.

## References

* Jurik Research DMX Product Guide: http://jurikres.com/down__/product_guide_.pdf
* Jurik Research DMX Catalog Entry: http://jurikres.com/catalog1/ms_dmx.htm
