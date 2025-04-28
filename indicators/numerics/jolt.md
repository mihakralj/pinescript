# Jolt: Third Derivative of Price Trend

[Pine Script Implementation of Jolt](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/jolt.pine)

## Overview and Purpose

Jolt is a third-order derivative indicator that measures the rate of change of acceleration over time. While slope indicates trend direction and steepness, and acceleration shows whether that momentum is increasing or decreasing, jolt reveals how quickly the acceleration itself is changing. This provides extremely early insights into potential inflection points in market behavior before they become visible in price, slope, or even acceleration readings.

By quantifying the rate of change of acceleration, jolt can identify when trends are experiencing sudden changes in their momentum profile. This can be particularly valuable for detecting early signs of trend exhaustion, momentum shifts, or the beginning of new trend impulses.

## Core Concepts

* **Momentum Change Rate:** Measures how quickly acceleration is changing, indicating potential inflection points in trend dynamics
* **Early Reversal Detection:** Often changes direction before acceleration, slope, and price, potentially providing the earliest warning of trend changes
* **Impulse Recognition:** Helps identify the beginning and end of strong trend impulses by measuring rapid changes in momentum
* **Exhaustion Identification:** Can signal when a trend is approaching exhaustion by showing decreasing rate of change in acceleration

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
| :-------- | :------ | :------- | :------------ |
| Period | 14 | Controls the lookback window for calculation | Lower (8-10) for more sensitivity at the cost of noise, higher (20-30) for smoother readings with increased lag |
| Source | Close | Data point used for calculation | Adjust based on specific analysis focus - High/Low for range dynamics, HLC3 for overall price action |

**Pro Tip:** Use jolt in combination with price, slope, and acceleration to create a complete momentum profile - when all four align (same direction), it often indicates a strong, sustained move is likely to continue.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Jolt calculates the slope (first derivative) of price data, then calculates the slope of those slope values (second derivative/acceleration), and finally calculates the slope of the acceleration values (third derivative/jolt). This reveals how quickly the trend's acceleration itself is changing.

**Technical formula:**
First, calculate slope using linear regression:

Slope = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)

Next, apply the same formula to slope values to get acceleration:

Accel = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)

Finally, apply the formula again to acceleration values to get jolt:

Jolt = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)

Where:

* n is the number of data points (period)
* x represents the time index (sequential position)
* y represents the source values (price for slope, slope values for acceleration, acceleration values for jolt)
* Σ denotes summation

> 🔍 **Technical Note:** The Pine Script implementation uses three cascaded linear regression calculations with dynamic arrays to efficiently process the data. The algorithm carefully handles edge cases and warmup periods by tracking valid counts throughout the calculation chain. A minimum of 2 bars is required for each derivative level, resulting in a minimum of 4 bars before jolt produces meaningful values.

## Interpretation Details

Jolt provides insights that complement slope and acceleration readings:

* **Positive Jolt:** Indicates increasing acceleration - the trend is not just accelerating, but accelerating at an increasing rate
* **Negative Jolt:** Shows decreasing acceleration - the trend may still be accelerating, but at a decreasing rate
* **Zero Crossing:** When jolt crosses from positive to negative, it suggests acceleration is beginning to flatten, potentially preceding a change in trend direction
* **Magnitude:** Larger jolt values (positive or negative) indicate more rapid changes in market momentum
* **Divergences:** When price continues making new highs/lows but jolt readings decline, it may signal an approaching reversal

## Limitations and Considerations

* **Significant Lag:** As a third-order derivative, jolt contains more inherent lag than price, slope, or acceleration
* **Noise Susceptibility:** Extremely sensitive to market noise, requiring careful period selection and often additional filtering
* **Complex Interpretation:** The concept of "rate of change of acceleration" is mathematically intuitive but can be challenging to interpret practically
* **False Signals:** Can generate numerous false signals, especially in choppy or range-bound markets
* **Complete Analysis Framework:** Most effective when used as part of a complete derivative analysis alongside price, slope, and acceleration
* **Warmup Requirements:** Needs at least 4 bars of data before producing meaningful values, creating a substantial initial warmup period

## References

* Ehlers, J. F. (2004). Cybernetic Analysis for Stocks and Futures: Cutting-Edge DSP Technology to Improve Your Trading. Wiley Trading.
* Mulloy, P. B. (1994). Smoothing Data with Faster Moving Averages. Technical Analysis of Stocks & Commodities, 12(2).
