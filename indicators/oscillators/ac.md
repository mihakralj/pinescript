# AC: Accelerator Oscillator

[Pine Script Implementation of AC](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/ac.pine)

## Overview and Purpose

The Accelerator Oscillator (AC) is a momentum indicator developed by Bill Williams as part of his trading methodology. It measures the acceleration or deceleration of market momentum by comparing the momentum of a fast moving average to a slow moving average, then measuring the rate of change of that difference. The AC builds upon the Awesome Oscillator (AO) concept by showing the acceleration of momentum rather than momentum itself, helping traders identify early stages of new moves and potential reversals before they become apparent in price action.

The implementation provided uses efficient circular buffers for all moving average calculations, ensuring optimal performance while properly handling data gaps. This approach maintains O(1) computational complexity for all operations, making it particularly suitable for real-time analysis while preserving accuracy in the momentum acceleration measurements.

## Core Concepts

* **Momentum acceleration:** Measures the rate of change of momentum rather than momentum itself
* **Early signal generation:** Often provides earlier signals than traditional momentum indicators
* **Zero-line significance:** Crossovers indicate potential trend changes or acceleration points
* **Color-based signals:** Green bars indicate increasing acceleration, red bars indicate deceleration

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Fast Length | 5 | Period for fast MA calculation | Rarely needs adjustment as it's part of Williams' original formula |
| Slow Length | 34 | Period for slow MA calculation | Rarely needs adjustment as it's part of Williams' original formula |

**Pro Tip:** Focus on the relationship between consecutive bars rather than absolute values. Three or more bars of the same color often indicate a sustained acceleration/deceleration phase that may precede a significant move.

## Calculation and Mathematical Foundation

**Simplified explanation:**
AC first calculates the Awesome Oscillator (AO) using two simple moving averages of median price, then subtracts a 5-period simple moving average of the AO from the current AO value to show acceleration.

**Technical formula:**
1. MP = (High + Low) / 2
2. AO = SMA(MP, Fast Length) - SMA(MP, Slow Length)
3. AC = AO - SMA(AO, 5)

Where:
- MP = Median Price
- SMA = Simple Moving Average
- Fast Length = 5 periods (default)
- Slow Length = 34 periods (default)

> 🔍 **Technical Note:** The implementation uses three separate circular buffers to efficiently calculate the required moving averages without storing the entire price history. This approach ensures constant memory usage and O(1) computational complexity per bar while properly handling NA values and maintaining accurate calculations.

## Interpretation Details

AC provides several analytical perspectives:

* **Zero-line crossovers:** Indicate potential trend changes or acceleration points
* **Color changes:** Green bars suggest increasing upward momentum, red bars suggest increasing downward momentum
* **Consecutive signals:** Three or more bars of the same color indicate sustained acceleration/deceleration
* **Divergence analysis:** AC diverging from price can signal potential reversals
* **Acceleration phases:** Higher highs in AC suggest strengthening momentum
* **Deceleration phases:** Lower highs suggest weakening momentum even if still in same direction

## Limitations and Considerations

* **Lagging component:** Contains some lag due to multiple moving average calculations
* **False signals:** Can generate noise in choppy or ranging markets
* **Parameter sensitivity:** While default parameters are standard, their effectiveness varies across timeframes
* **Complementary tool:** Should be used alongside price action and other indicators
* **Timeframe dependency:** More reliable on higher timeframes where noise is reduced
* **Signal confirmation:** Best used with other Williams' indicators like AO for confirmation

## References

* Williams, B. (1995). New Trading Dimensions. Wiley Trading.
* Williams, B. (1999). Trading Chaos (2nd ed.). Wiley Trading.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
