# NVI: Negative Volume Index

[Pine Script Implementation of NVI](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/nvi.pine)

## Overview and Purpose

The Negative Volume Index (NVI) is a cumulative indicator that tracks price changes occurring on days when trading volume decreases from the previous day. Developed by Paul Dysart in the 1930s and later popularized by Norman Fosback, NVI is based on the theory that "smart money" (institutional investors) tends to trade during periods of lower volume, while "uninformed money" (retail investors) is more active during high-volume periods.

The fundamental premise is that significant price movements accompanied by declining volume often represent institutional activity, as large players prefer to trade quietly to avoid moving the market against their positions. NVI helps identify these periods and the underlying price trends that may be driven by informed trading decisions.

## Core Concepts

* **Volume-selective tracking:** Only updates when current volume is less than previous period's volume
* **Cumulative nature:** Builds upon previous values, creating a running total of price changes
* **Smart money theory:** Assumes institutional investors prefer to trade during quiet market periods
* **Trend identification:** Helps distinguish between retail-driven and institution-driven price movements
* **Divergence detection:** Excellent for spotting when price action contradicts volume patterns

The key insight is that when volume decreases but prices continue to move significantly, it often indicates that fewer but more informed participants are driving the price action.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Price Source | Close | Price series used for calculations | Open for gap analysis, High/Low for range analysis |
| Starting Value | 100 | Initial value for NVI calculation | 1000 for easier percentage interpretation |
| Show PVI | True | Display Positive Volume Index for comparison | Disable to focus solely on NVI |
| Show MA | True | Display moving average of NVI | Essential for signal generation |
| MA Length | 255 | Periods for NVI moving average | Standard 255 (1 year daily), adjust for timeframe |

**Pro Tip:** The 255-period moving average is traditional for daily charts (approximately one trading year). For weekly charts, use 52 periods; for monthly, use 12. The relationship between NVI and its moving average is crucial for generating reliable signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
NVI starts at a base value (typically 100) and only changes on days when volume decreases from the previous day. When volume drops, NVI is adjusted by the percentage price change. On days when volume increases or stays the same, NVI remains unchanged.

**Technical formula:**
```
If Volume[today] < Volume[yesterday]:
    NVI[today] = NVI[yesterday] × (1 + ((Price[today] - Price[yesterday]) / Price[yesterday]))
Else:
    NVI[today] = NVI[yesterday]

Starting Value: NVI[0] = 100 (or 1000)
```

**Step-by-step calculation:**
```
1. Initialize NVI with starting value (100)
2. Compare current volume with previous volume
3. If current volume < previous volume:
   a. Calculate price change percentage: (Price[today] - Price[yesterday]) / Price[yesterday]
   b. Update NVI: NVI[yesterday] × (1 + price change percentage)
4. If current volume >= previous volume:
   a. NVI remains unchanged: NVI[today] = NVI[yesterday]
5. Repeat for each period
```

> 🔍 **Technical Note:** NVI is a cumulative indicator, meaning each value depends on all previous values. This creates a continuous index that reflects the cumulative effect of price changes during low-volume periods. The percentage-based calculation ensures that NVI responds proportionally to price movements regardless of the absolute price level.

## Implementation Features

The Pine Script implementation includes several enhancements:

* **Dual index display:** Both NVI and PVI (Positive Volume Index) for comprehensive analysis
* **Moving average overlay:** Traditional 255-period MA for signal generation
* **Signal detection:** Automatic identification of NVI/MA crossovers
* **Visual indicators:** Background coloring and alert arrows for trend changes
* **Information table:** Real-time display of current values
* **Flexible parameters:** Customizable starting values and moving average periods

## Visual Elements

The indicator displays:

* **Blue NVI Line:** Main Negative Volume Index (width 2)
* **Red PVI Line:** Positive Volume Index for comparison (optional)
* **Orange MA Line:** Moving average of NVI for trend identification
* **Gray Reference Line:** Dotted line at starting value
* **Background Colors:** Green when NVI > MA (bullish), Red when NVI < MA (bearish)
* **Signal Arrows:** ▲ for bullish crossovers, ▼ for bearish crossovers
* **Information Table:** Current values display in top-right corner

## Interpretation Details

Negative Volume Index provides several types of market insights:

* **Trend direction:** NVI above its MA suggests institutional accumulation (bullish)
* **Trend reversal:** NVI below its MA indicates institutional distribution (bearish)
* **Signal generation:** Crossovers between NVI and its MA provide buy/sell signals
* **Market character:** Rising NVI suggests smart money is bullish; falling NVI suggests bearish sentiment
* **Volume analysis:** Periods when NVI doesn't change indicate high-volume (retail-driven) activity
* **Divergence opportunities:** NVI moving opposite to price can signal potential reversals

## Function Usage

```pine
nvi(src, vol, start_value)
```

**Parameters:**
* `src` (series float): Price series to use for calculation (typically close)
* `vol` (series float): Volume series
* `start_value` (simple float): Starting value for NVI (typically 100 or 1000)

**Returns:** `float` - The current NVI value

## Trading Applications

* **Trend following:** Buy when NVI crosses above MA, sell when it crosses below
* **Market timing:** Use NVI direction to confirm broader market trends
* **Smart money tracking:** Monitor NVI changes to follow institutional sentiment
* **Divergence trading:** Look for NVI/price divergences for early reversal signals
* **Volume analysis:** Combine with PVI to understand retail vs. institutional activity
* **Long-term positioning:** NVI is particularly effective for identifying major trend changes

## Comparison with Similar Indicators

* **vs. Positive Volume Index (PVI):** NVI tracks low-volume days while PVI tracks high-volume days
* **vs. On-Balance Volume:** OBV uses all volume data while NVI is selective based on volume changes
* **vs. Accumulation/Distribution:** A/D considers intraday price position while NVI uses closing prices
* **vs. Money Flow Index:** MFI is bounded 0-100 while NVI is cumulative and unbounded
* **vs. Volume Rate of Change:** VROC measures volume changes while NVI measures price changes on volume decreases

## Advantages of NVI

* **Smart money insight:** Provides visibility into institutional trading patterns
* **Trend persistence:** Excellent for identifying and confirming long-term trends
* **Low noise:** Filtering by volume reduces false signals from retail-driven volatility
* **Historical context:** Cumulative nature preserves long-term market memory
* **Complementary analysis:** Works well with PVI for comprehensive volume analysis

## Limitations and Considerations

* **Lagging nature:** As a cumulative indicator, NVI can be slow to signal trend changes
* **Volume dependency:** Requires reliable volume data; less effective with poor volume reporting
* **Market regime sensitivity:** May behave differently in high-frequency trading environments
* **Long-term focus:** Better suited for position trading than short-term scalping
* **Starting value impact:** Different starting values can affect visual interpretation
* **Moving average dependency:** Signal quality depends heavily on appropriate MA period selection

## Advanced Analysis Techniques

* **NVI/PVI spread analysis:** Monitor the difference between NVI and PVI for market regime changes
* **Multiple timeframe analysis:** Compare NVI signals across different timeframes for confirmation
* **Sector rotation:** Use NVI to identify when smart money is rotating between sectors
* **Economic cycle analysis:** NVI trends often align with economic cycles and institutional allocation changes
* **Divergence confirmation:** Use NVI divergences to confirm signals from other technical indicators

## Market Context Applications

* **Bull markets:** Rising NVI above MA confirms institutional participation in uptrend
* **Bear markets:** Falling NVI below MA suggests institutional distribution
* **Sideways markets:** NVI oscillations around MA indicate institutional indecision
* **Market tops:** NVI failing to confirm new price highs can signal distribution
* **Market bottoms:** NVI making higher lows while price makes lower lows can signal accumulation

## Historical Significance

* **Paul Dysart (1930s):** Original developer of the concept
* **Norman Fosback (1970s):** Popularized NVI through extensive research
* **"Dumb Money" theory:** Academic foundation for volume-based market segmentation
* **Market timing:** Historical studies show NVI effectiveness in major trend identification
* **Institutional behavior:** Research validates the premise of smart money operating in low-volume periods

## References

* Fosback, Norman G. "Stock Market Logic." The Institute for Econometric Research, 1976.
* Dysart, Paul. "Market Analysis." Financial Publishing, 1935.
* Murphy, John J. "Technical Analysis of the Financial Markets." New York Institute of Finance, 1999.
* Arms, Richard W. "Volume Cycles in the Stock Market." Equis International, 1994.
* Colby, Robert W. "The Encyclopedia of Technical Market Indicators." McGraw-Hill, 2003.
