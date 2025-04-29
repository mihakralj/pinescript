# AOBV: Archer On-Balance Volume

[Pine Script Implementation of AOBV](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/aobv.pine)

## Overview and Purpose

The Archer On-Balance Volume (AOBV) is an enhanced variation of the classic On-Balance Volume (OBV) indicator, providing a smoother representation of volume flow with improved signal generation capabilities. It combines the volume-price relationship principles of OBV with exponential moving average (EMA) smoothing to reduce noise while preserving responsiveness to significant volume events.

AOBV calculates both Fast (4-period) and Slow (14-period) lines, allowing traders to identify potential entry and exit points through crossovers, similar to a moving average crossover system. This dual-line approach helps filter out false signals while highlighting significant shifts in buying or selling pressure that may precede price movements.

## Core Concepts

* **Volume Flow Analysis:** Measures cumulative buying and selling pressure by adding or subtracting volume based on price movement direction
* **Smoothing Mechanism:** Applies EMA calculations to the raw OBV values to reduce noise while maintaining sensitivity to significant volume events
* **Dual Timeframe Approach:** Provides both Fast and Slow AOBV lines for crossover signals and trend confirmation
* **Bias Correction:** Implements specialized warmup handling for more accurate EMA values from the beginning of the calculation

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | Close | Price point used for direction determination | Rarely needs adjustment; close price typically provides the most relevant direction information |
| Volume | Volume | Trading volume used in calculations | Consider adjusting when analyzing markets with unusual volume characteristics |

**Pro Tip:** Pay attention to divergences between the Fast and Slow AOBV lines during trend transitions - when they begin to narrow after a significant separation, it often indicates diminishing momentum and a potential trend change.

## Calculation and Mathematical Foundation

**Simplified explanation:**
AOBV first creates a standard OBV by adding volume when price closes higher than the previous close and subtracting volume when price closes lower. It then applies two separate EMAs (4-period and 14-period) to this OBV value, with special bias correction during the warmup period for more accurate early values.

**Technical formula:**
1. Calculate raw OBV:
   - If Close > Previous Close: OBV = Previous OBV + Volume
   - If Close < Previous Close: OBV = Previous OBV - Volume
   - If Close = Previous Close: OBV = Previous OBV

2. Calculate AOBV Fast and Slow using bias-corrected EMAs:
   - During warmup: EMA_corrected = EMA / (1 - (1-α)^n)
   - After warmup: EMA = EMA_previous + α × (OBV - EMA_previous)
   
   Where:
   - α is 2/(period+1)
   - Period is 4 for Fast and 14 for Slow

> 🔍 **Technical Note:** The Pine Script implementation uses specialized arrays to track EMA values and correction factors, handling NA values gracefully by preserving the last valid price. It also implements a proper warmup bias correction to minimize the initialization effect common to exponential moving averages.

## Interpretation Details

AOBV provides several analytical perspectives:

* **Trend Confirmation:** When both AOBV lines are rising, it confirms bullish pressure; when both are falling, it confirms bearish pressure
* **Crossovers:** When Fast AOBV crosses above Slow AOBV, it suggests increasing buying momentum; crosses below suggest increasing selling momentum
* **Divergences:** When price makes a new high/low but AOBV fails to confirm, it suggests potential weakness in the current trend
* **Volume Confirmation:** Strong price moves should be accompanied by corresponding AOBV movement in the same direction
* **Zero Line Analysis:** Extended periods above/below the zero line (if normalized) indicate sustained buying/selling pressure

## Limitations and Considerations

* **Market Conditions:** Less effective in low-volume environments where price movements may not reflect significant buying or selling pressure
* **Lag Component:** While reduced compared to simpler moving averages, the smoothing process still introduces some lag
* **False Signals:** Volume spikes from news events can create temporary distortions unrelated to genuine trend changes
* **NA Handling:** The implementation preserves previous values when encountering missing data, which maintains continuity but may not reflect actual market conditions
* **Parameter Sensitivity:** The default periods (4 and 14) may need adjustment in different market conditions or timeframes
* **Complementary Analysis:** Works best when combined with price action analysis and other technical indicators

## References

* Archer, T. (n.d.). Technical Analysis Using Multiple Timeframes. Marketplace Books.
* Dormeier, B. (2011). Investing with Volume Analysis. FT Press.
