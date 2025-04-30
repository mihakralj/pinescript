# CHANGE: Percentage Change

[Pine Script Implementation of CHANGE](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/change.pine)

## Overview and Purpose

The Percentage Change indicator measures the relative price movement between the current value and a historical value over a specified lookback period. Unlike absolute change metrics, percentage change normalizes the movement relative to the starting price, providing a proportional representation of price movements regardless of the security's nominal value. This makes it particularly valuable for comparing securities with different price ranges, evaluating historical volatility patterns, and identifying acceleration or deceleration in price movements.

The implementation provided uses a direct history referencing approach for maximum computational efficiency, avoiding unnecessary array manipulations while maintaining proper error handling for historical data gaps or zero values. The result is presented as a decimal value (e.g., 0.05 for a 5% change) that can be easily formatted as a percentage in the user interface.

## Core Concepts

* **Relative measurement:** Expresses price movement as a proportion of the starting price, normalizing comparisons across different price scales
* **Lookback flexibility:** Allows analysis of changes over any time period, from short-term fluctuations to long-term trends
* **Baseline normalization:** By using the historical value as the denominator, creates a consistent measurement framework
* **Trend magnitude assessment:** Helps quantify the strength of price movements beyond simple directional analysis

Percentage change calculations form the foundation for many other technical indicators and risk metrics, including momentum oscillators, volatility measures, and performance comparisons. By focusing on the relative rather than absolute magnitude of price movements, this indicator helps traders identify significant price changes regardless of the nominal price range of the security being analyzed.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | Close | Price data used for change calculation | Modify to analyze different aspects of price action (e.g., high for resistance tests) |
| Length | 1 | Lookback period for comparison | Increase for longer-term analysis; decrease for more responsive signals |

**Pro Tip:** Try comparing percentage change across multiple timeframes simultaneously. When short-term percentage changes exceed longer-term average changes, it often indicates an acceleration phase that may signal the early stage of a new trend.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Percentage Change calculates how much the current value has changed relative to a past value, expressed as a percentage of that past value. The formula divides the difference between current and past values by the past value.

**Technical formula:**

Percentage Change = (Current Value / Historical Value) - 1

Where:
- Current Value is the latest price data
- Historical Value is the price data from Length bars ago

> 🔍 **Technical Note:** The implementation uses direct historical access with the `source[length]` operator for efficiency, avoiding the overhead of array creation and manipulation. It also includes proper handling for cases where the historical value is either missing (NA) or zero, returning NA in these scenarios to prevent division-by-zero errors.

## Interpretation Details

Percentage Change provides several analytical insights:

* **Positive vs. negative values:** Positive readings indicate upward movement relative to the historical price, while negative values indicate downward movement
* **Magnitude assessment:** Larger absolute values indicate stronger price movements relative to the starting price
* **Acceleration/deceleration:** Increasing percentage change values suggest accelerating momentum, while decreasing values indicate decelerating momentum
* **Comparative analysis:** Comparing percentage changes across different securities helps identify relative strength or weakness
* **Volatility indication:** The magnitude of percentage changes over consistent time periods provides insight into price volatility

## Limitations and Considerations

* **Base effect:** Small denominators (low historical prices) can produce misleadingly large percentage changes
* **Asymmetric scale:** Negative percentage changes are bounded at -100%, while positive changes are unbounded, creating an inherent asymmetry
* **Compound effect:** Sequential percentage changes cannot be simply added; they must be compounded
* **Reference point sensitivity:** The choice of the reference period can significantly affect the results
* **Time window constraints:** Fixed lookback periods may miss important reference points that don't align with the chosen period
* **Zero handling:** Requires special handling when the reference value is zero (division by zero)
* **Volatility bias:** More volatile securities tend to show larger percentage changes over any given period

## References

* Edwards, R. D., & Magee, J. (2007). Technical Analysis of Stock Trends. AMACOM.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
* Kirkpatrick, C. D., & Dahlquist, J. R. (2010). Technical Analysis: The Complete Resource for Financial Market Technicians. FT Press.
