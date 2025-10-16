# ATAN2: Two-Argument Arctangent

[Pine Script Implementation of ATAN2](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/atan2.pine)

## Overview and Purpose

The two-argument arctangent function (atan2) is a fundamental mathematical function that computes the angle in radians between the positive x-axis and the point (x, y) in the Cartesian plane. Unlike the standard arctangent function (atan), which only considers the ratio y/x and returns values in the limited range (-π/2, π/2), atan2 considers both the numerator and denominator separately, allowing it to correctly determine angles across all four quadrants. This makes it particularly useful for:

*   **Phase Angle Calculation:** Computing the phase of complex signals in signal processing, including Hilbert Transform indicators and other cycle analysis tools.
*   **Directional Analysis:** Determining the direction or angle of movement in price action, momentum, or volatility measures.
*   **Quadrant-Aware Calculations:** Any computation requiring full 360-degree angle awareness, avoiding the ambiguity inherent in simple atan(y/x).

The atan2 function is the missing piece in PineScript that enables robust implementation of advanced technical indicators, particularly those based on John Ehlers' cycle analysis algorithms.

## Core Concepts

*   **Two-Argument Input:** Unlike atan(y/x), atan2(y, x) takes both numerator (y) and denominator (x) as separate arguments, preserving sign information needed for quadrant determination.
*   **Full Angle Range:** Returns angles in the range (-π, π], covering all four quadrants of the Cartesian plane.
*   **Quadrant Handling:** Correctly determines the quadrant based on the signs of both x and y:
    *   Quadrant I (x > 0, y > 0): angle ∈ (0, π/2)
    *   Quadrant II (x < 0, y > 0): angle ∈ (π/2, π)
    *   Quadrant III (x < 0, y < 0): angle ∈ (-π, -π/2)
    *   Quadrant IV (x > 0, y < 0): angle ∈ (-π/2, 0)
*   **Numerical Stability:** The implementation avoids division by very small numbers by using the identity atan(1/z) = π/2 - atan(z), ensuring stable results even when x or y approach zero.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|:----------|:--------|:---------|:---------------|
| Y (Numerator) | high - low | The y-coordinate or numerator for the angle calculation | Change to any series representing vertical displacement, range, or imaginary component in complex analysis |
| X (Denominator) | (high + low) / 2 | The x-coordinate or denominator for the angle calculation | Change to any series representing horizontal displacement, position, or real component in complex analysis |

**Pro Tip:** When using atan2 for Hilbert Transform calculations, Y typically represents the quadrature (Q) component and X represents the in-phase (I) component. For directional analysis, Y might represent price change while X represents time or another reference measure. The default inputs provide a simple demonstration using price range as Y and midpoint as X.

## Calculation and Mathematical Foundation

The atan2 function returns the angle θ such that:

x = r × cos(θ)
y = r × sin(θ)

Where r = √(x² + y²) is the magnitude (radius).

**Standard atan2 definition:**
```
θ = atan2(y, x)
```

**Numerically stable implementation:**

The algorithm uses different approaches based on the relative magnitudes of |x| and |y| to avoid numerical instability:

1. **If |x| > |y|:** Calculate directly using atan(|y| / |x|)
2. **If |y| ≥ |x|:** Use the identity atan(|x| / |y|) = π/2 - atan(|y| / |x|) to avoid division by small numbers

**Quadrant correction:**

After computing the base angle, adjust for the correct quadrant:
1. If x < 0, angle = π - angle (reflect across y-axis)
2. If y < 0, angle = -angle (reflect across x-axis)

**Mathematical properties:**
*   atan2(0, x) = 0 for x > 0
*   atan2(0, x) = π for x < 0  
*   atan2(y, 0) = π/2 for y > 0
*   atan2(y, 0) = -π/2 for y < 0
*   atan2(0, 0) is undefined (raises runtime error)

> 🔍 **Technical Note:** The Pine Script implementation uses math.atan() which returns values in (-π/2, π/2). By cleverly choosing which ratio to pass to atan and then applying quadrant corrections, we achieve full (-π, π] coverage. This approach is both numerically stable and computationally efficient, matching the behavior of atan2 in C standard library and other languages.

## Interpretation Details

*   **Output Range:** The atan2 function returns angles in radians in the range (-π, π], where:
    *   π radians = 180 degrees
    *   π/2 radians = 90 degrees
    *   Values wrap around: approaching π from below equals approaching -π from above
    
*   **Angle Meaning:**
    *   **Positive angles:** Counter-clockwise rotation from positive x-axis
    *   **Negative angles:** Clockwise rotation from positive x-axis
    *   **Zero angle:** Point lies on positive x-axis (y = 0, x > 0)
    *   **±π angle:** Point lies on negative x-axis (y = 0, x < 0)

*   **Practical Applications:**
    *   **Hilbert Transform:** Use atan2(Q, I) to get instantaneous phase
    *   **Momentum Direction:** Use atan2(price_change, time) for directional indicators
    *   **Complex Signal Phase:** Essential for any phasor-based analysis

*   **Discontinuity:** The function has a discontinuity at the negative x-axis where it jumps from π to -π. This is by design and represents the same physical angle.

## Limitations and Considerations

*   **Undefined at Origin:** atan2(0, 0) is mathematically undefined and will raise a runtime error. Ensure your inputs don't both become zero simultaneously.
*   **Discontinuity at -π/π:** When tracking continuous phase evolution, be aware of the wrap-around at ±π. Phase unwrapping algorithms may be needed for certain applications.
*   **Radian Output:** The function returns angles in radians, not degrees. To convert to degrees, multiply by 180/π (approximately 57.2958).
*   **Input Sensitivity:** For very small x and y values (near machine precision), numerical rounding errors may affect the output angle, though the implementation is designed to minimize such effects.
*   **Performance:** While optimized, atan2 involves transcendental function evaluation (atan) which is more computationally expensive than basic arithmetic operations.

## References

*   Wikipedia contributors. (2023). *atan2*. Wikipedia, The Free Encyclopedia.
*   ISO/IEC 9899:2018 (C18 standard). *The C Standard Library*, atan2 function specification.
*   Ehlers, J. F. (2001). *Rocket Science for Traders: Digital Signal Processing Applications*. John Wiley & Sons. (Chapter on Hilbert Transform)
*   Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007). *Numerical Recipes: The Art of Scientific Computing* (3rd ed.). Cambridge University Press.
