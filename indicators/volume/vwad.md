# VWAD: Volume Weighted Accumulation/Distribution

[Pine Script Implementation of VWAD](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/vwad.pine)

## Overview and Purpose

The Volume Weighted Accumulation/Distribution (VWAD) is an enhanced version of the traditional Accumulation/Distribution Line (ADL) that incorporates volume weighting to provide more accurate signals of buying and selling pressure. While the standard ADL multiplies the Money Flow Multiplier by volume, VWAD adds an additional layer by weighting the money flow volume based on relative volume activity over a specified period. This creates a more sensitive indicator that emphasizes periods of unusually high or low volume activity, making it particularly valuable for identifying accumulation and distribution phases that occur with significant volume backing.

## Core Concepts

* **Volume weighting enhancement:** Builds upon ADL by adding volume-relative weighting to emphasize periods of high volume activity
* **Money flow sensitivity:** More responsive to accumulation/distribution occurring on above-average volume
* **Institutional activity detection:** Better at identifying large-scale buying and selling that typically occurs with elevated volume

VWAD addresses a key limitation of traditional ADL by recognizing that money flow occurring on high volume periods should carry more significance than the same money flow occurring on low volume periods. This makes VWAD particularly effective for spotting institutional accumulation or distribution phases.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Volume Weight Period | 20 | Lookback period for calculating volume weighting | Increase for longer-term volume context, decrease for more responsive weighting |

**Pro Tip:** The Volume Weight Period determines how the current bar's volume is weighted relative to recent volume history. A period of 20 provides good balance between responsiveness and stability, but shorter periods (10-15) can be more sensitive to volume spikes, while longer periods (30-50) provide smoother, more stable weighting.

## Calculation and Mathematical Foundation

**Simplified explanation:**
VWAD calculates the Money Flow Multiplier (same as ADL), multiplies it by volume, then applies an additional volume weight based on the current bar's volume relative to the average volume over the specified period. This double volume weighting makes the indicator more sensitive to accumulation/distribution occurring during high volume periods.

**Technical formula:**
```
Money Flow Multiplier (MFM) = ((Close - Low) - (High - Close)) / (High - Low)
Volume Weight = Current Volume / Average Volume (over period)
Weighted Money Flow Volume = Volume × MFM × Volume Weight
VWAD = Cumulative sum of Weighted Money Flow Volume
```

**Step-by-step calculation:**
```
1. Calculate Money Flow Multiplier: MFM = ((C-L) - (H-C)) / (H-L)
2. Calculate volume weight: VW = Current Volume / Rolling Average Volume
3. Calculate weighted money flow: WMFV = Volume × MFM × VW
4. Add to cumulative VWAD: VWAD += WMFV
```

> 🔍 **Technical Note:** This implementation uses a circular buffer to efficiently maintain the rolling volume average for weighting calculations. The volume weight amplifies or diminishes the money flow based on whether current volume is above or below the recent average, making the indicator more responsive to volume-confirmed price movements while reducing noise from low-volume periods.

## Interpretation Details

VWAD provides enhanced accumulation/distribution analysis:

* **Trend confirmation:** Rising VWAD confirms accumulation with volume backing; falling VWAD confirms distribution
* **Volume-confirmed breakouts:** VWAD movements that coincide with price breakouts on high volume provide stronger confirmation
* **Divergence analysis:** VWAD diverging from price often provides earlier warning signals than standard ADL
* **Institutional activity:** Large VWAD movements often indicate institutional accumulation or distribution phases
* **Support/resistance testing:** VWAD behavior during support/resistance tests can reveal the volume-weighted conviction behind price movements

## Limitations and Considerations

* **Volume dependency:** Requires consistent and reliable volume data; less effective in markets with irregular volume reporting
* **Sensitivity to volume spikes:** Can be temporarily distorted by unusual volume events (earnings, news, option expiration)
* **Parameter sensitivity:** Different Volume Weight Periods can significantly affect the indicator's responsiveness and interpretation
* **Market structure:** More effective in liquid markets where volume accurately represents trading interest
* **Cumulative nature:** Like ADL, VWAD is cumulative and may trend higher or lower over long periods regardless of current conditions
* **Complementary analysis:** Best used alongside price action, momentum indicators, and volume profile analysis

## References

* Williams, Larry R. "The Secret of Selecting Stocks for Immediate and Substantial Gains." Windsor Books, 1972.
* Granville, Joseph E. "Granville's New Key to Stock Market Profits." Prentice-Hall, 1963.
* Arms Jr., Richard W. "Volume Cycles in the Stock Market." Equis International, 1994.
