# KVO: Klinger Volume Oscillator

[Pine Script Implementation of KVO](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/kvo.pine)

## Overview and Purpose

The Klinger Volume Oscillator (KVO) is a technical indicator developed by Stephen Klinger that combines price movement and volume to identify short-term and long-term money flow trends. The oscillator compares the relationship between price and volume over two different time periods to detect potential reversal points in the market. KVO is particularly effective at identifying divergences between price action and volume flow, making it valuable for spotting potential trend changes before they become apparent in price alone.

## Core Concepts

* **Volume flow analysis:** Measures the volume flow based on price movement direction and intraday price position
* **Dual timeframe comparison:** Uses fast and slow exponential moving averages to compare short-term vs long-term trends
* **Trend direction sensitivity:** Incorporates the overall price trend direction in volume calculations
* **Signal line confirmation:** Includes a signal line for trade timing and confirmation

KVO's unique approach to volume analysis makes it particularly useful for identifying accumulation and distribution phases, as well as potential trend reversals when the oscillator diverges from price action.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Fast EMA Period | 34 | Short-term volume trend smoothing | Decrease for more sensitivity, increase for smoother signals |
| Slow EMA Period | 55 | Long-term volume trend smoothing | Adjust based on timeframe and market volatility |
| Signal Line Period | 13 | Signal line smoothing | Shorter for faster signals, longer for more reliable signals |

**Pro Tip:** The default settings (34, 55, 13) were optimized by Klinger for daily charts. For intraday trading, consider reducing all periods proportionally. For longer-term analysis, increase the periods while maintaining their relative relationships.

## Calculation and Mathematical Foundation

**Simplified explanation:**
KVO calculates a "daily measurement" (DM) that combines volume with price trend direction and intraday price position. It then applies fast and slow EMAs to this measurement and takes the difference to create the oscillator.

**Technical formula:**
```
HLC3 = (High + Low + Close) / 3
Trend = 1 if HLC3 > HLC3[previous], -1 if HLC3 < HLC3[previous], else previous Trend

CM = ABS(2 * ((High - Low - (Close - Low)) / (High - Low)) - 1)
DM = Trend × Volume × CM

Fast EMA = EMA(DM, Fast Period)
Slow EMA = EMA(DM, Slow Period)

KVO = Fast EMA - Slow EMA
Signal Line = EMA(KVO, Signal Period)
```

**Step-by-step calculation:**
```
1. Calculate typical price: HLC3 = (High + Low + Close) / 3
2. Determine trend direction: Compare current HLC3 with previous using ternary operator
3. Calculate Close Money (CM): Measures intraday price position
4. Calculate Daily Measurement: DM = Trend × Volume × CM
5. Apply fast EMA to DM with warmup compensation: Fast EMA(DM)
6. Apply slow EMA to DM with warmup compensation: Slow EMA(DM)
7. Calculate KVO: Fast EMA - Slow EMA
8. Calculate Signal Line with warmup compensation: EMA(KVO, Signal Period)
```

> 🔍 **Technical Note:** The Close Money (CM) component measures where the close falls within the day's range, similar to Williams %R but applied to volume weighting. This gives more weight to volume when prices close near the high (bullish) or low (bearish) of the session, making KVO sensitive to intraday price action patterns.

## Implementation Features

The Pine Script implementation includes several optimizations:

* **Warmup compensation:** Individual EMA warmup systems ensure accurate values from the first bar
* **Ternary trend detection:** Efficient single-line trend determination logic
* **Dirty data protection:** Uses `nz()` functions to handle missing volume data
* **Optimized performance:** Compact code structure with minimal operations per cycle
* **Standard parameter order:** Period parameters (fast, slow, signal) come first for easy adjustment

## Visual Elements

The indicator displays:

* **Yellow KVO Line:** Main oscillator line (width 2)
* **Blue Signal Line:** Confirmation line for timing signals (width 1)
* **Zero Reference Line:** Dashed gray line for accumulation/distribution analysis
* **Green/Red Histogram:** Visual representation of KVO vs Signal difference (50% transparency)

## Interpretation Details

KVO provides several types of trading signals:

* **Zero line crossovers:** KVO crossing above zero suggests accumulation; below zero suggests distribution
* **Signal line crossovers:** KVO crossing above its signal line generates buy signals; crossing below generates sell signals
* **Divergence analysis:** KVO diverging from price action often precedes trend reversals
* **Trend confirmation:** KVO direction should align with price trend for strong moves
* **Overbought/oversold:** Extreme KVO values may indicate potential reversal points
* **Volume flow shifts:** Changes in KVO direction reveal shifts in volume flow patterns

## Function Usage

```pine
kvo(fast_len, slow_len, signal_len, src_open, src_high, src_low, src_close, src_vol)
```

**Parameters:**
* `fast_len` (int, default 34): Fast EMA period
* `slow_len` (int, default 55): Slow EMA period  
* `signal_len` (int, default 13): Signal line period
* `src_open` (series float): Open price series
* `src_high` (series float): High price series
* `src_low` (series float): Low price series
* `src_close` (series float): Close price series
* `src_vol` (series float): Volume series

**Returns:** `[KVO line, Signal line]`

## Limitations and Considerations

* **Lagging nature:** As an oscillator based on EMAs, KVO has inherent lag that may delay signals
* **False signals:** Can generate whipsaws in choppy or low-volume market conditions
* **Volume data dependency:** Requires reliable volume data; less effective with poor volume reporting
* **Parameter sensitivity:** Different market conditions may require parameter adjustments
* **Market structure:** More effective in liquid markets with consistent volume patterns
* **Divergence timing:** Divergences can persist longer than expected before price follows
* **Complementary analysis:** Best used with other technical indicators and price action analysis

## References

* Klinger, Stephen J. "The Klinger Oscillator." Stocks & Commodities Magazine, 1997.
