---
title: Volatility Ratio (VR)
description: The Volatility Ratio (VR) compares the current true range to the average true range over a longer period, indicating short-term volatility relative to recent norms.
author: Mihai Crăciunescu
date: 2025-05-14
tags: [volatility, true range, atr, market analysis]
---

## Volatility Ratio (VR)

### Overview

The Volatility Ratio (VR) is an indicator that measures the current period's true range relative to the average true range over a specified longer period. It helps traders understand if the current bar's volatility is significantly higher or lower than the recent norm.

A VR greater than 1 suggests that the current bar's true range is larger than the recent average true range, indicating an expansion in short-term volatility. Conversely, a VR less than 1 suggests that the current bar's true range is smaller than the recent average, indicating a contraction in short-term volatility.

### How It's Calculated

The Pine Script™ implementation calculates the Volatility Ratio within a single main function `vr(atrPeriod)`. This function encapsulates all necessary logic:

1.  **Calculate Current True Range**: Inside the `vr()` function, the true range for the current bar (referred to as `tr` in the script) is explicitly calculated. True Range is the greatest of:
    *   Current High minus Current Low
    *   Absolute value of (Current High minus Previous Close)
    *   Absolute value of (Current Low minus Previous Close)
    This calculation is performed directly.

2.  **Calculate Average True Range (Bias-Corrected Wilder's RMA)**: Also within the `vr()` function, the Average True Range (referred to as `atrCurrent` in the script) of the True Range values is calculated over a specified lookback period (`atrPeriod`). This method is a variation of Wilder's RMA (Running Moving Average) that includes a bias correction mechanism for the initial values, aiming for a more responsive start compared to a standard SMA-initialized ATR. It involves:
    *   Calculating a "raw" ATR (`raw_atr`) using Wilder's smoothing:
        `raw_atr = (Previous_raw_atr * (Period - 1) + CurrentTrueRange) / Period`. The first `raw_atr` is typically initialized with the first `CurrentTrueRange` value.
    *   Maintaining a bias compensator factor (`e_compensator`) which is updated each bar:
        `e_compensator = (1 - alpha) * Previous_e_compensator`, where `alpha = 1 / Period`.
    *   The final, bias-corrected ATR (`atrCurrent`) is then derived:
        `atrCurrent = e_compensator > EPSILON ? raw_atr / (1 - e_compensator) : raw_atr`.
        (EPSILON is a very small constant to prevent division by zero or near-zero issues with the compensator).
    This provides the "true range over a longer period."

3.  **Calculate Volatility Ratio**:
    `VolatilityRatio = TrueRange / AverageTrueRange` (i.e. `tr / atrCurrent` in the script)

    If `AverageTrueRange` is zero (which can happen in periods of no price movement or very early in the data), the Volatility Ratio is typically considered `na` to avoid division by zero.

### Parameters

*   **ATR Period (`atrPeriod`)**: The lookback period used for calculating the Average True Range. Default is `14`.

### Interpretation

*   **VR > 1.0**: The current bar's true range is greater than the average true range over the `atrPeriod`. This signals an increase in short-term volatility compared to the recent norm. Very high values (e.g., > 2 or 3) can indicate significant breakout bars or panic selling/buying.
*   **VR < 1.0**: The current bar's true range is smaller than the average true range. This signals a decrease in short-term volatility. Very low values might indicate market consolidation or indecision.
*   **VR ≈ 1.0**: The current bar's true range is roughly in line with the recent average volatility.

Traders can use the VR to:
*   Identify potential breakout signals (a sharp increase in VR).
*   Gauge the strength of a move (moves accompanied by high VR might be more significant).
*   Filter trades (e.g., avoid trading when VR is extremely low, indicating a quiet market).

### Limitations

*   **Short-Term Focus**: The VR primarily reflects the volatility of the current bar against a recent average. It's a short-term gauge.
*   **Not Directional**: Like ATR, the VR measures the magnitude of volatility, not its direction.
*   **Parameter Sensitivity**: The `atrPeriod` will influence the baseline average true range. Shorter periods will make the ATR more reactive, and thus the VR might fluctuate more.
*   **Smoothing Method**: The ATR calculation uses a bias-corrected Wilder's RMA. Different smoothing methods or initialization techniques (e.g., standard SMA-initialized ATR) would yield different VR values, especially in the initial period of the calculation.

### Pine Script™ Implementation

```pinescript
// The MIT License (MIT)
// © mihakralj
//@version=5
indicator("Volatility Ratio (VR)", shorttitle="VR", format=format.price, precision=2, overlay=false)

//@function Calculates the Volatility Ratio (VR).
// All logic for True Range and ATR calculation is encapsulated within this function.
// ATR uses Wilder's RMA with bias correction for initialization.
//@param atrPeriod The lookback period for ATR. Must be > 0.
//@returns float The Volatility Ratio value for the current bar.
vr(int atrPeriod) =>
    if atrPeriod <= 0
        runtime.error("ATR Period must be greater than 0")
        float(na)
    float tr = na
    float h_l = high - low
    if not na(close[1])
        float h_pc = math.abs(high - close[1])
        float l_pc = math.abs(low - close[1])
        tr := math.max(h_l, h_pc, l_pc)
    else
        tr := h_l
    var float EPSILON_ATR = 1e-10
    var float raw_atr = 0.0
    var float e_compensator = 1.0
    float trForAtr = nz(tr)
    float atrCurrent = na
    if not na(trForAtr)
        float alpha = 1.0 / float(atrPeriod)
        if na(raw_atr[1]) and e_compensator == 1.0
            raw_atr := trForAtr
        else
            raw_atr := (nz(raw_atr[1]) * (atrPeriod - 1) + trForAtr) / atrPeriod
        e_compensator := (1.0 - alpha) * e_compensator
        atrCurrent := e_compensator > EPSILON_ATR ? raw_atr / (1.0 - e_compensator) : raw_atr
    float volatilityRatio = na
    if not na(atrCurrent) and atrCurrent != 0
        volatilityRatio := tr / atrCurrent
    volatilityRatio

// Inputs
i_atrPeriod = input.int(14, title="ATR Period", minval=1, tooltip="The lookback period for calculating the Average True Range (ATR).")

// Calculation
vrValue = vr(i_atrPeriod)

// Plot
plot(vrValue, title="VR", color=color.new(color.teal, 0), linewidth=2)

// Optional: Line at 1.0 for reference
hline(1.0, "Reference Line", color=color.gray, linestyle=hline.style_dashed)
