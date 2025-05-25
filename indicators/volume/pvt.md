# PVT: Price Volume Trend

[Pine Script Implementation of PVT](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/pvt.pine)

## Overview and Purpose

The Price Volume Trend (PVT) is a momentum-based technical indicator that combines price movement with volume to create a cumulative measure of buying and selling pressure. Developed as an improvement over On-Balance Volume (OBV), PVT considers not just the direction of price movement but also its magnitude, making it more sensitive to the degree of price changes. Unlike OBV which uses only the direction of price movement, PVT multiplies volume by the percentage price change, providing a more nuanced view of volume flow.

PVT operates on the principle that volume should confirm price movements. When prices rise significantly with high volume, PVT increases substantially. When prices fall with high volume, PVT decreases. This relationship helps traders identify the strength behind price movements and potential divergences that may signal trend changes.

## Core Concepts

* **Volume-weighted price momentum:** Combines volume with the magnitude of price changes rather than just direction
* **Cumulative measurement:** Maintains a running total that reflects long-term volume and price relationships
* **Percentage-based calculation:** Uses relative price changes rather than absolute changes for better scaling
* **Trend confirmation:** Helps confirm whether volume supports current price trends
* **Divergence detection:** Identifies when volume flow diverges from price action, potentially signaling reversals

The fundamental principle is that meaningful price movements should be accompanied by proportional volume. PVT's sensitivity to both price change magnitude and volume makes it particularly effective at identifying when institutional money is flowing into or out of a security.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Signal Line Period | 14 | Period for signal line smoothing (SMA of PVT) | Shorter for more sensitive signals, longer for smoother trend identification |

**Pro Tip:** PVT is most effective when used for divergence analysis. Look for situations where price makes new highs or lows but PVT fails to confirm these moves. The signal line helps smooth out noise and identify the overall trend direction of the PVT itself.

## Calculation and Mathematical Foundation

**Simplified explanation:**
PVT calculates the percentage change in price, multiplies it by volume, and adds this to a cumulative total. This creates a running indicator that rises when prices increase with volume and falls when prices decrease with volume.

**Technical formula:**
```
Price Change % = (Current Close - Previous Close) / Previous Close
Volume Adjustment = Volume × Price Change %
PVT = Previous PVT + Volume Adjustment
Signal Line = SMA(PVT, Signal Period)
```

**Step-by-step calculation:**
```
1. Calculate price change: Current Close - Previous Close
2. Calculate percentage change: Price Change / Previous Close
3. Calculate volume adjustment: Volume × Percentage Change
4. Add to cumulative PVT: Previous PVT + Volume Adjustment
5. Calculate signal line: Simple Moving Average of PVT
```

> 🔍 **Technical Note:** Unlike OBV which adds or subtracts entire volume based on price direction, PVT scales volume by the magnitude of price change. A 1% price increase with 1000 shares adds 10 to PVT, while a 5% increase adds 50, better reflecting the strength of the move.

## Implementation Features

The Pine Script implementation includes several enhancements:

* **Robust calculation:** Handles missing data and prevents division by zero errors
* **Signal line:** Optional smoothed version using Simple Moving Average for trend identification
* **Visual enhancements:** Background coloring and zero reference line for clear interpretation
* **Cumulative tracking:** Maintains proper running total across all historical data

## Visual Elements

The indicator displays:

* **Yellow PVT Line:** Main cumulative price volume trend (width 2)
* **Red Signal Line:** Smoothed version of PVT for trend identification (width 1)
* **Zero Reference Line:** Dashed gray line for positive/negative distinction
* **Background Coloring:** Green when PVT > Signal, Red when PVT < Signal (95% transparency)

## Interpretation Details

Price Volume Trend provides several types of trading insights:

* **Trend confirmation:** PVT moving in the same direction as price confirms the trend's strength
* **Divergence analysis:** PVT diverging from price action often precedes trend reversals
* **Volume flow assessment:** Rising PVT indicates accumulation, falling PVT suggests distribution
* **Signal line crossovers:** PVT crossing above signal line suggests bullish momentum; crossing below indicates bearish momentum
* **Zero line significance:** PVT above zero generally indicates net accumulation over the analysis period
* **Slope analysis:** The steepness of PVT changes indicates the intensity of buying or selling pressure

## Function Usage

```pine
pvt(src, src_vol)
```

**Parameters:**
* `src` (series float): Source price data (typically close)
* `src_vol` (series float): Volume data

**Returns:** `float` - The cumulative PVT value

## Trading Applications

* **Trend confirmation:** Use PVT to confirm price breakouts and trend continuations
* **Divergence trading:** Look for PVT divergences from price for early reversal signals
* **Accumulation/Distribution analysis:** Rising PVT indicates accumulation phases, falling suggests distribution
* **Signal line strategy:** Trade PVT crossovers above/below signal line for momentum shifts
* **Volume validation:** Confirm that significant price moves are supported by proportional volume flow
* **Long-term analysis:** PVT's cumulative nature makes it excellent for identifying long-term volume trends

## Comparison with Similar Indicators

* **vs. On-Balance Volume (OBV):** PVT considers price change magnitude while OBV uses only direction
* **vs. Accumulation/Distribution Line:** PVT uses percentage change while A/D uses intraday price position
* **vs. Chaikin Money Flow:** PVT is cumulative while CMF is a bounded oscillator
* **vs. Volume Weighted Average Price:** PVT tracks momentum while VWAP shows average price levels
* **vs. Money Flow Index:** PVT is unbounded and cumulative while MFI is a bounded oscillator

## Advantages of PVT

* **Magnitude sensitivity:** Responds appropriately to the size of price changes, not just direction
* **Volume integration:** Properly weights price movements by their accompanying volume
* **Divergence detection:** Excellent at identifying when volume flow conflicts with price action
* **Trend analysis:** Cumulative nature provides clear long-term trend perspective
* **Early signals:** Often leads price movements, providing early warning of trend changes

## Limitations and Considerations

* **Cumulative nature:** Values can become very large over time, making absolute levels less meaningful
* **No natural bounds:** Unlike oscillators, PVT doesn't have fixed upper/lower limits
* **Trend dependency:** More effective in trending markets than in sideways consolidations
* **Volume data quality:** Requires reliable volume data for accurate calculations
* **Context requirement:** Best used with other technical analysis tools for comprehensive market assessment
* **Starting point sensitivity:** Initial value affects the absolute level, though trends remain valid

## Advanced Analysis Techniques

* **Multiple timeframe analysis:** Compare PVT across different timeframes for comprehensive perspective
* **Rate of change:** Analyze the speed of PVT changes to gauge momentum intensity
* **Relative comparison:** Compare PVT patterns between different securities or market indices
* **Volume anomaly detection:** Identify unusual volume/price relationships through PVT spikes
* **Institutional activity tracking:** Large PVT movements may indicate institutional buying/selling

## References

* Granville, Joseph E. "Granville's New Key to Stock Market Profits." Prentice-Hall, 1963.
* Arms, Richard W. "Volume Cycles in the Stock Market." Dow Jones-Irwin, 1983.
* Murphy, John J. "Technical Analysis of the Financial Markets." New York Institute of Finance, 1999.
* Achelis, Steven B. "Technical Analysis from A to Z." McGraw-Hill, 2000.
