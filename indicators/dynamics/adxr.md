# ADXR: Average Directional Movement Index Rating

[Pine Script Implementation of ADXR](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/adxr.pine)

## Overview and Purpose

The Average Directional Movement Index Rating (ADXR) is an extension of the ADX indicator that measures both the current trend strength and how it has changed over time. Developed by J. Welles Wilder Jr., ADXR compares the current ADX value with a historical ADX value to provide insight into whether trend strength is increasing or decreasing. This comparison helps traders identify not just the presence of a trend, but also whether that trend is gaining or losing momentum.

The implementation provided builds upon the efficient ADX calculations using Wilder's smoothing method, adding the historical comparison component while maintaining optimal performance. By averaging current and historical ADX values, ADXR provides a more complete picture of trend development and potential changes in trend strength.

## Core Concepts

* **Trend strength comparison:** Measures how current trend strength compares to historical trend strength
* **Momentum of trend strength:** Shows whether trending conditions are improving or deteriorating
* **Dual-period analysis:** Combines current and historical ADX readings for broader perspective
* **Trend development tracking:** Helps identify early stages of trend formation and potential exhaustion

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| ADX Period | 14 | Period for ADX calculation | Lower for more sensitivity, higher for more stability |
| Rating Period | 14 | Lookback period for historical ADX | Adjust based on typical trend duration in the market |

**Pro Tip:** Watch for divergences between ADXR and ADX - when ADXR starts declining while ADX is still rising, it often signals that trend momentum is weakening even though the trend appears strong.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ADXR calculates the average of the current ADX value and the ADX value from n periods ago. This shows whether trend strength is generally increasing (rising ADXR) or decreasing (falling ADXR) over time.

**Technical formula:**
ADXR = (Current ADX + Historical ADX) / 2

Where:
- Current ADX = Present ADX value
- Historical ADX = ADX value from n periods ago
- n = Rating Period

> 🔍 **Technical Note:** The implementation maintains the efficient ADX calculation using Wilder's smoothing and proper warmup handling, while adding the historical comparison component. This ensures accurate trend strength measurement while properly managing the additional complexity of historical value comparison.

## Interpretation Details

ADXR provides several analytical perspectives:

* **Trend strength evolution:** Rising ADXR indicates strengthening trend conditions
* **Trend exhaustion:** Falling ADXR suggests weakening trend conditions
* **Early trend detection:** ADXR rising from low levels can signal early trend development
* **Trend continuation:** Strong trends typically show rising or stable ADXR values
* **Divergence analysis:** ADXR diverging from ADX can signal potential trend changes
* **Market condition assessment:** ADXR levels help distinguish between trending and ranging markets

## Limitations and Considerations

* **Additional lag:** Historical comparison introduces more lag than standard ADX
* **False signals:** Can generate false signals during volatile market conditions
* **Parameter sensitivity:** Performance depends heavily on both ADX and rating periods
* **Market conditions:** Most effective in trending markets, less reliable in choppy conditions
* **Complementary tool:** Should be used alongside price action and other indicators
* **Historical requirement:** Needs sufficient historical data for meaningful signals

## References

* Wilder, J. Welles. "New Concepts in Technical Trading Systems," Trend Research, 1978
* Murphy, John J. "Technical Analysis of the Financial Markets," New York Institute of Finance, 1999
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
