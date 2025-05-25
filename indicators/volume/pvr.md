# PVR: Price Volume Rank

[Pine Script Implementation of PVR](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/pvr.pine)

## Overview and Purpose

The Price Volume Rank (PVR) is a simple technical indicator developed by Anthony J. Macek that categorizes market conditions using only two data sets: price and volume. Published in the June 1994 issue of "Technical Analysis of Stocks & Commodities" magazine, PVR provides a straightforward classification system that ranks the relationship between price movement and volume activity into four distinct categories plus a neutral state.

Unlike complex volume indicators that use moving averages or oscillators, PVR offers a binary comparison approach that immediately identifies the current market condition by comparing today's price and volume to yesterday's values. This simplicity makes it particularly useful for quick market assessment and systematic trading decisions.

## Core Concepts

* **Binary comparison system:** Compares current price and volume to previous period's values
* **Categorical classification:** Assigns integer values (0-4) based on price-volume relationships
* **Real-time assessment:** Provides immediate market condition identification
* **Volume confirmation:** Validates price movements with corresponding volume activity
* **Trend quality measurement:** Distinguishes between strong and weak price movements

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Price Source | Close | Price series used for comparison | Use High/Low for range analysis, Open for gap analysis |
| Buy/Sell Threshold | 2.5 | Level separating buy and sell signals | Standard threshold recommended by Macek |

**Pro Tip:** PVR works best as a confirmation tool rather than a standalone signal generator. Combine with trend analysis and support/resistance levels for optimal results.

## Calculation and Mathematical Foundation

**Simplified explanation:**
PVR compares today's price and volume to yesterday's price and volume, assigning a rank from 0 to 4 based on the four possible combinations of higher/lower relationships.

**Technical formula:**
```
If Price > PrevPrice AND Volume > PrevVolume then PVR = 1
If Price > PrevPrice AND Volume < PrevVolume then PVR = 2  
If Price < PrevPrice AND Volume < PrevVolume then PVR = 3
If Price < PrevPrice AND Volume > PrevVolume then PVR = 4
Else PVR = 0 (when Price = PrevPrice)
```

Where:
- PrevPrice = Previous period's price
- PrevVolume = Previous period's volume

> 🔍 **Technical Note:** The indicator uses simple period-to-period comparisons without any smoothing or averaging. The neutral state (PVR = 0) occurs when price remains unchanged from the previous period, regardless of volume activity.

## Interpretation Details

PVR provides clear categorical signals:

* **PVR = 1 (Strong Bullish):**
  - Price up with increased volume
  - Indicates strong buying pressure with institutional participation
  - Most bullish condition with volume confirmation

* **PVR = 2 (Weak Bullish):**
  - Price up with decreased volume
  - Suggests limited buying interest or profit-taking
  - Potential reversal warning as volume doesn't support price advance

* **PVR = 3 (Weak Bearish):**
  - Price down with decreased volume
  - Indicates selling without strong conviction
  - May represent temporary pullback rather than trend reversal

* **PVR = 4 (Strong Bearish):**
  - Price down with increased volume
  - Shows strong selling pressure with volume confirmation
  - Most bearish condition indicating potential continued decline

* **PVR = 0 (Neutral):**
  - Price unchanged from previous period
  - Market indecision or consolidation
  - Wait for clearer directional signals

## Trading Signals

**Basic Macek Strategy:**
- **Buy Signal:** PVR ≤ 2.5 (Categories 1 and 2)
- **Sell Signal:** PVR > 2.5 (Categories 3 and 4)

**Advanced Interpretations:**
- **Strongest Buy:** PVR = 1 (price up, volume up)
- **Caution Zone:** PVR = 2 (price up, volume down - potential top)
- **Weak Selling:** PVR = 3 (price down, volume down - potential bottom)
- **Strong Sell:** PVR = 4 (price down, volume up)

## Limitations and Considerations

* **Single-period focus:** Only considers immediate previous period, may miss longer trends
* **Equal weighting:** Treats small and large price/volume changes equally
* **No magnitude consideration:** Doesn't account for the size of price or volume changes
* **Gap sensitivity:** May give misleading signals during price gaps
* **Low volume periods:** Less reliable during holiday or low-activity sessions
* **Whipsaw potential:** Can generate frequent signals in choppy markets

## References

* Macek, Anthony J. (1994). "Price Volume Rank." Technical Analysis of Stocks & Commodities, June 1994.
