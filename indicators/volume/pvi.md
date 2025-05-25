# PVI: Positive Volume Index

[Pine Script Implementation of PVI](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/pvi.pine)

## Overview and Purpose

The Positive Volume Index (PVI) is a cumulative indicator that tracks price changes occurring on days when trading volume increases from the previous day. Developed alongside the Negative Volume Index (NVI) by Paul Dysart in the 1930s and later popularized by Norman Fosback, PVI is based on the theory that "uninformed money" (retail investors) tends to be more active during periods of higher volume, while institutional investors prefer to trade during quieter periods.

The fundamental premise is that significant price movements accompanied by increasing volume often represent retail activity, as individual investors tend to trade more actively during periods of high market attention and excitement. PVI helps identify these periods and the underlying price trends that may be driven by crowd behavior and market sentiment.

## Core Concepts

* **Volume-selective tracking:** Only updates when current volume is greater than previous period's volume
* **Cumulative nature:** Builds upon previous values, creating a running total of price changes
* **Crowd behavior theory:** Assumes retail investors are more active during high-volume periods
* **Trend identification:** Helps distinguish between institution-driven and retail-driven price movements
* **Market sentiment:** Excellent for tracking when crowd psychology is driving market action

The key insight is that when volume increases and prices move significantly, it often indicates that the broader market (retail investors) is participating, which can signal either trend continuation or potential exhaustion.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Price Source | Close | Price series used for calculations | Open for gap analysis, High/Low for range analysis |
| Starting Value | 100 | Initial value for PVI calculation | 1000 for easier percentage interpretation |
| Show MA | True | Display moving average of PVI | Essential for signal generation |
| MA Length | 255 | Periods for PVI moving average | Standard 255 (1 year daily), adjust for timeframe |

**Pro Tip:** The 255-period moving average is traditional for daily charts (approximately one trading year). For weekly charts, use 52 periods; for monthly, use 12. The relationship between PVI and its moving average is crucial for generating reliable signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
PVI starts at a base value (typically 100) and only changes on days when volume increases from the previous day. When volume rises, PVI is adjusted by the percentage price change. On days when volume decreases or stays the same, PVI remains unchanged.

**Technical formula:**
```
If Volume[today] > Volume[yesterday]:
    PVI[today] = PVI[yesterday] × (1 + ((Price[today] - Price[yesterday]) / Price[yesterday]))
Else:
    PVI[today] = PVI[yesterday]

Starting Value: PVI[0] = 100 (or 1000)
```

**Step-by-step calculation:**
```
1. Initialize PVI with starting value (100)
2. Compare current volume with previous volume
3. If current volume > previous volume:
   a. Calculate price change percentage: (Price[today] - Price[yesterday]) / Price[yesterday]
   b. Update PVI: PVI[yesterday] × (1 + price change percentage)
4. If current volume <= previous volume:
   a. PVI remains unchanged: PVI[today] = PVI[yesterday]
5. Repeat for each period
```

> 🔍 **Technical Note:** PVI is a cumulative indicator, meaning each value depends on all previous values. This creates a continuous index that reflects the cumulative effect of price changes during high-volume periods. The percentage-based calculation ensures that PVI responds proportionally to price movements regardless of the absolute price level.

## Implementation Features

The Pine Script implementation includes several enhancements:

* **Focused PVI calculation:** Clean implementation tracking only positive volume days
* **Moving average overlay:** Traditional 255-period MA for signal generation
* **Signal detection:** Automatic identification of PVI/MA crossovers
* **Visual indicators:** Background coloring and alert arrows for trend changes
* **Information table:** Real-time display of current values
* **Flexible parameters:** Customizable starting values and moving average periods

## Visual Elements

The indicator displays:

* **Red PVI Line:** Main Positive Volume Index (width 2)
* **Orange MA Line:** Moving average of PVI for trend identification
* **Gray Reference Line:** Dotted line at starting value
* **Background Colors:** Green when PVI > MA (bullish), Red when PVI < MA (bearish)
* **Signal Arrows:** ▲ for bullish crossovers, ▼ for bearish crossovers
* **Information Table:** Current values display in top-right corner

## Interpretation Details

Positive Volume Index provides several types of market insights:

* **Trend direction:** PVI above its MA suggests retail participation in uptrend (bullish)
* **Trend reversal:** PVI below its MA indicates retail distribution or selling (bearish)
* **Signal generation:** Crossovers between PVI and its MA provide buy/sell signals
* **Market character:** Rising PVI suggests crowd is bullish; falling PVI suggests bearish sentiment
* **Volume analysis:** Periods when PVI doesn't change indicate low-volume (institutional) activity
* **Divergence opportunities:** PVI moving opposite to price can signal potential reversals

## Function Usage

```pine
pvi(src, vol, start_value)
```

**Parameters:**
* `src` (series float): Price series to use for calculation (typically close)
* `vol` (series float): Volume series
* `start_value` (simple float): Starting value for PVI (typically 100 or 1000)

**Returns:** `float` - The current PVI value

## Trading Applications

* **Trend following:** Buy when PVI crosses above MA, sell when it crosses below
* **Market timing:** Use PVI direction to gauge retail investor sentiment
* **Crowd behavior tracking:** Monitor PVI changes to follow retail sentiment
* **Divergence trading:** Look for PVI/price divergences for potential reversal signals
* **Volume analysis:** Combine with NVI to understand retail vs. institutional activity
* **Sentiment analysis:** PVI is particularly effective for identifying crowd-driven moves

## Comparison with Similar Indicators

* **vs. Negative Volume Index (NVI):** PVI tracks high-volume days while NVI tracks low-volume days
* **vs. On-Balance Volume:** OBV uses all volume data while PVI is selective based on volume changes
* **vs. Accumulation/Distribution:** A/D considers intraday price position while PVI uses closing prices
* **vs. Money Flow Index:** MFI is bounded 0-100 while PVI is cumulative and unbounded
* **vs. Volume Rate of Change:** VROC measures volume changes while PVI measures price changes on volume increases

## Advantages of PVI

* **Retail sentiment insight:** Provides visibility into crowd behavior and retail trading patterns
* **Trend confirmation:** Excellent for confirming trends driven by broad market participation
* **High signal clarity:** Filtering by volume increases reduces noise from institutional activity
* **Historical context:** Cumulative nature preserves long-term market sentiment memory
* **Complementary analysis:** Works perfectly with NVI for comprehensive volume analysis

## Limitations and Considerations

* **Lagging nature:** As a cumulative indicator, PVI can be slow to signal trend changes
* **Volume dependency:** Requires reliable volume data; less effective with poor volume reporting
* **Market regime sensitivity:** May behave differently in algorithm-dominated trading environments
* **Crowd focus:** Better suited for understanding retail behavior than institutional activity
* **Starting value impact:** Different starting values can affect visual interpretation
* **Moving average dependency:** Signal quality depends heavily on appropriate MA period selection

## Advanced Analysis Techniques

* **PVI/NVI spread analysis:** Monitor the difference between PVI and NVI for market regime changes
* **Multiple timeframe analysis:** Compare PVI signals across different timeframes for confirmation
* **Sector analysis:** Use PVI to identify when retail money is flowing into specific sectors
* **Market cycle analysis:** PVI trends often align with retail investor sentiment cycles
* **Divergence confirmation:** Use PVI divergences to confirm signals from other technical indicators

## Market Context Applications

* **Bull markets:** Rising PVI above MA confirms retail participation in uptrend
* **Bear markets:** Falling PVI below MA suggests retail capitulation or selling
* **Sideways markets:** PVI oscillations around MA indicate retail indecision
* **Market tops:** PVI making new highs while price stagnates can signal retail exhaustion
* **Market bottoms:** PVI making higher lows while price makes lower lows can signal retail accumulation

## Historical Significance

* **Paul Dysart (1930s):** Original developer alongside NVI
* **Norman Fosback (1970s):** Popularized PVI through extensive research on crowd behavior
* **"Smart Money" theory:** Academic foundation for volume-based market segmentation
* **Retail behavior:** Research validates crowd tendency to trade during high-volume periods
* **Market timing:** Historical studies show PVI effectiveness in tracking retail sentiment

## References

* Fosback, Norman G. "Stock Market Logic." The Institute for Econometric Research, 1976.
* Dysart, Paul. "Market Analysis." Financial Publishing, 1935.
* Murphy, John J. "Technical Analysis of the Financial Markets." New York Institute of Finance, 1999.
* Arms, Richard W. "Volume Cycles in the Stock Market." Equis International, 1994.
* Colby, Robert W. "The Encyclopedia of Technical Market Indicators." McGraw-Hill, 2003.
