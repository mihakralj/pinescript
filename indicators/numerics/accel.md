# Accel: Acceleration (Slope of Slope)

[Pine Script Implementation of Accel](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/accel.pine)

## Overview and Purpose

Acceleration is a second-order derivative indicator that measures the rate of change of slope over time. While slope indicates the direction and steepness of a trend, acceleration reveals whether that trend is gaining momentum, maintaining steady momentum, or losing strength. This provides early insights into potential trend exhaustion or reversal points before they become visible in price action or even in slope readings.

By quantifying the curvature of price movement rather than just its direction, acceleration helps traders anticipate inflection points in market behavior. Positive acceleration during an uptrend suggests increasing momentum, while negative acceleration may signal an impending slowdown even while prices continue rising.

## Core Concepts

* **Trend Acceleration/Deceleration:** Reveals whether a trend is gaining or losing momentum, even before changes appear in price direction
* **Inflection Point Detection:** Helps identify when a trend is transitioning from acceleration to deceleration (or vice versa)
* **Early Warning System:** Often changes direction before slope and price, potentially providing leading signals
* **Momentum Confirmation:** Validates the strength and sustainability of existing trends

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
| :-------- | :------ | :------- | :------------ |
| Period | 14 | Controls the lookback window for calculation | Lower for quicker signals with more noise (8-10), higher for smoother readings with increased lag (20-30) |
| Source | Close | Data point used for calculation | Adjust based on analysis focus - High/Low for range dynamics, Volume for momentum confirmation |

**Pro Tip:** Watch for divergences between acceleration and price - when price continues making higher highs but acceleration turns negative, the uptrend may be losing steam and approaching exhaustion.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Acceleration calculates the slope of the price data over the specified period, then calculates the slope of those slope values. This reveals how quickly the trend's angle (slope) itself is changing.

**Technical formula:**
First, calculate the slope using linear regression:

Slope = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)

Then, apply the same formula to the sequence of slope values to get acceleration:

Accel = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)

Where:
* n is the number of data points (period)
* x represents the time index (bar_index for slope, position index for acceleration)
* y represents the source values (price data for slope, slope values for acceleration)
* Σ denotes summation

> 🔍 **Technical Note:** The Pine Script implementation uses dynamic arrays to store both the original data points and the calculated slope values. The algorithm efficiently handles warmup periods by tracking valid counts and only performing calculations when sufficient data is available. A minimum of 2 bars is required for slope calculation, and thus a minimum of 3 bars for acceleration calculation.

## Interpretation Details

Acceleration provides unique insights into market dynamics:

* **Positive Acceleration:** Indicates increasing momentum - trend is strengthening (slopes are getting steeper)
* **Negative Acceleration:** Shows decreasing momentum - trend is weakening (slopes are getting flatter)
* **Zero Crossing:** When acceleration crosses from positive to negative, it suggests the trend is beginning to lose strength, even if prices continue in the same direction
* **Consistent Sign:** When acceleration and slope have the same sign (both positive or both negative), it confirms the trend's strength and sustainability
* **Opposing Signs:** When acceleration and slope have opposite signs, it suggests the trend may be approaching an inflection point

## Limitations and Considerations

* **Signal Lag:** As a second-order derivative, acceleration contains more lag than price or slope
* **Noise Sensitivity:** More susceptible to market noise than simpler indicators, potentially generating false signals
* **Parameter Dependency:** Results vary significantly based on the chosen period - too short creates noise, too long increases lag
* **Math Complexity:** The double derivative nature makes interpretation more complex than first-order indicators
* **Complete Analysis:** Should be used alongside price action, slope, and other confirming indicators rather than in isolation
* **Warmup Period:** Requires at least 3 bars of data before producing meaningful values

## References

* Ehlers, J. F. (2001). Rocket Science for Traders: Digital Signal Processing Applications. Wiley Trading.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
