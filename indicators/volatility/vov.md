---
title: Volatility of Volatility (VOV)
description: The Volatility of Volatility (VOV) indicator measures the rate of change in volatility itself, providing insights into the stability or instability of market volatility.
author: Mihai Crăciunescu
date: 2025-05-13
tags: [volatility, market analysis, risk management]
---

## Volatility of Volatility (VOV)

### Overview

The Volatility of Volatility (VOV) indicator measures the rate of change in an asset's volatility. It essentially quantifies how stable or erratic the volatility itself is. A high VOV suggests that volatility levels are changing rapidly, indicating increasing market uncertainty or a transition phase. A low VOV suggests that volatility is relatively stable, even if the overall volatility level is high or low.

This indicator is often used by traders and analysts to gauge market sentiment, identify potential turning points, or assess risk. For example, a sharp increase in VOV might precede a significant market move as volatility conditions become unstable.

### How It's Calculated

The VOV is typically calculated in two main steps:

1.  **Calculate Initial Volatility:** First, a measure of volatility is calculated for the underlying asset. A common choice for this is the Standard Deviation of the asset's price (e.g., closing price) over a defined lookback period (`volatilityPeriod`).

    `InitialVolatility = StandardDeviation(Source, volatilityPeriod)`

2.  **Calculate Volatility of the Initial Volatility:** Once the initial volatility series is obtained, the VOV is calculated as the standard deviation of this initial volatility series over a second lookback period (`vovPeriod`).

    `VOV = StandardDeviation(InitialVolatility, vovPeriod)`

The standard deviation itself is a measure of the dispersion of a set of values. It is calculated as the square root of the variance, where variance is the average of the squared differences from the Mean. The Pine Script™ implementation below uses an efficient rolling algorithm for this.

### Parameters

*   **Source (`src`)**: The input data series for the initial volatility calculation. Default is `close`.
*   **Volatility Period (`volatilityPeriod`)**: The lookback period used to calculate the initial volatility. Default is `20`.
*   **VOV Period (`vovPeriod`)**: The lookback period used to calculate the standard deviation of the initial volatility series. Default is `10`.

### Interpretation

*   **High VOV**: Indicates that the level of volatility is changing rapidly. This can signal increasing market nervousness, uncertainty, or a potential shift in market regime. High VOV might be observed during periods leading up to major news events or during market panics where volatility spikes erratically.
*   **Low VOV**: Suggests that the current level of volatility (whether high or low) is relatively stable and not changing much. This might indicate a more predictable market environment in terms of its risk profile, or a period of consolidation in volatility.
*   **Rising VOV**: May suggest that an existing trend in volatility is accelerating or that a new period of high volatility is beginning.
*   **Falling VOV**: May suggest that volatility is stabilizing or that a period of high volatility is subsiding.

### Example Usage

Traders might use VOV in conjunction with other indicators:

*   **Breakout Confirmation**: A breakout accompanied by rising VOV might be considered more significant, as it suggests that the change in price is also causing volatility itself to become unstable.
*   **Risk Management**: Monitoring VOV can help in adjusting position sizes or stop-loss levels. Rapidly increasing VOV might warrant tighter risk controls.
*   **Option Pricing**: VOV can be an input or consideration for more sophisticated option pricing models, as it relates to the volatility of implied volatility (though this indicator typically uses historical volatility).

### Limitations

*   **Lagging Nature**: Since VOV uses two stages of standard deviation calculations, it is a lagging indicator. It describes recent changes in volatility rather than predicting future volatility.
*   **Parameter Sensitivity**: The behavior and responsiveness of the VOV indicator are sensitive to the chosen `volatilityPeriod` and `vovPeriod`. Shorter periods will make it more responsive but also noisier, while longer periods will make it smoother but slower to react.
*   **Interpretation Context**: A high or low VOV value should be interpreted within the broader market context and in relation to its own historical levels for the specific asset being analyzed.

### Pine Script™ Implementation

```pinescript
// The MIT License (MIT)
// © mihakralj
//@version=5
indicator("Volatility of Volatility (VOV)", shorttitle="VOV", format=format.price, precision=4, overlay=false)

//@function Calculates the Volatility of Volatility (VOV) with embedded rolling standard deviation algorithms.
//@param src The source series. Default is `close`.
//@param volatilityPeriod The lookback period for the initial volatility calculation. Default is 20.
//@param vovPeriod The lookback period for calculating the standard deviation of the volatility series. Default is 10.
//@returns float The VOV value.
vov(series float src, int volatilityPeriod, int vovPeriod) =>
    if volatilityPeriod <= 0 or vovPeriod <= 0
        runtime.error("Periods must be greater than 0")

    var int p1 = 0, head1 = 0, count1 = 0
    var array<float> buffer1 = array.new_float(0)
    var float sum1 = 0.0, sumSq1 = 0.0
    
    if p1 != volatilityPeriod // Handles initialization and period changes
        p1 := math.max(1, volatilityPeriod)
        buffer1 := array.new_float(p1, na)
        head1 := 0
        count1 := 0
        sum1 := 0.0
        sumSq1 := 0.0

    float oldest1 = array.get(buffer1, head1)
    if not na(oldest1)
        sum1 -= oldest1
        sumSq1 -= oldest1 * oldest1
        if count1 == p1 
            count1 -=1 
            
    float val1 = nz(src)
    sum1 += val1
    sumSq1 += val1 * val1
    
    count1 := count1 < p1 ? count1 + 1 : count1 // Use ternary for conditional increment
        
    array.set(buffer1, head1, val1)
    head1 := (head1 + 1) % p1
    float initialVolatility = count1 > 1 ? math.sqrt(math.max(0.0, (sumSq1 / count1) - math.pow(sum1 / count1, 2))) : 0.0

    var int p2 = 0, head2 = 0, count2 = 0
    var array<float> buffer2 = array.new_float(0)
    var float sum2 = 0.0, sumSq2 = 0.0

    if p2 != vovPeriod // Handles initialization and period changes
        p2 := math.max(1, vovPeriod)
        buffer2 := array.new_float(p2, na)
        head2 := 0
        count2 := 0
        sum2 := 0.0
        sumSq2 := 0.0
        
    float oldest2 = array.get(buffer2, head2)
    if not na(oldest2)
        sum2 -= oldest2
        sumSq2 -= oldest2 * oldest2
        if count2 == p2
            count2 -= 1
            
    float val2 = nz(initialVolatility)
    sum2 += val2
    sumSq2 += val2 * val2

    count2 := count2 < p2 ? count2 + 1 : count2 // Use ternary for conditional increment
        
    array.set(buffer2, head2, val2)
    head2 := (head2 + 1) % p2
    float vovValue = count2 > 1 ? math.sqrt(math.max(0.0, (sumSq2 / count2) - math.pow(sum2 / count2, 2))) : 0.0
    
    vovValue

// Inputs
i_src = input.source(close, "Source")
i_volatilityPeriod = input.int(20, "Volatility Period", minval=1, tooltip="Period for initial volatility calculation.")
i_vovPeriod = input.int(10, "VOV Period", minval=1, tooltip="Period for StDev of the volatility series.")

// Calculation
vovValue = vov(i_src, i_volatilityPeriod, i_vovPeriod)

// Plot
plot(vovValue, "VOV", color.new(color.yellow, 0), 2)
```

This implementation directly embeds an efficient rolling standard deviation algorithm for both stages of the VOV calculation. Invalid period inputs will result in a runtime error.
