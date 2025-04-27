# ADL: Accumulation/Distribution Line

[Pine Script Implementation of ADL](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/adl.pine)

## Overview and Purpose

The Accumulation/Distribution Line (ADL) is a volume-based indicator that measures the cumulative flow of money into and out of a security. It identifies whether a security is being accumulated (bought) or distributed (sold) by analyzing price movements in relation to volume. Developed by Marc Chaikin in the 1970s, ADL expands on Joe Granville's earlier On-Balance Volume (OBV) concept by focusing not just on whether price closed higher or lower, but where the close occurred within the period's trading range.

## Core Concepts

* **Volume-price relationship:** ADL measures buying and selling pressure by considering both trading volume and where prices close within their daily range
* **Market application:** Particularly useful for identifying divergences between price action and underlying buying/selling pressure, which can signal potential reversals
* **Timeframe suitability:** Works on all timeframes, but most effective on daily and weekly charts for identifying long-term accumulation or distribution patterns

The ADL's core principle is that the close position within a period's range reflects the strength of buyers versus sellers. When prices close in the upper portion of the range, this suggests accumulation (buying pressure); conversely, closes in the lower portion suggest distribution (selling pressure). This concept is then weighted by the period's volume to determine money flow.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | close | Price point used in money flow calculation | Rarely needs adjustment; close price typically provides the most relevant information |
| Volume | volume | Trading volume used to weight price movements | Consider adjusting when analyzing markets with unusual volume characteristics |

**Pro Tip:** Focus more on divergences between ADL and price rather than absolute ADL values - these divergences often provide the most actionable signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ADL calculates where price closed relative to its high-low range, multiplies this by volume to get "money flow," and maintains a running total of these values. When price closes in the upper half of the range, it adds volume (weighted by how high in the range); when price closes in the lower half, it subtracts volume (weighted by how low in the range).

**Technical formula:**
1. Money Flow Multiplier = ((Close - Low) - (High - Close)) / (High - Low)
   * Simplified as: (2 × Close - High - Low) / (High - Low)
2. Money Flow Volume = Money Flow Multiplier × Volume
3. ADL = Previous ADL + Current Money Flow Volume

> 🔍 **Technical Note:** The Money Flow Multiplier will range from -1 to +1. A close at the high gives +1, a close at the low gives -1, and a close at the exact middle of the range gives 0.

## Interpretation Details

ADL is primarily used to confirm price trends and identify potential reversals through divergences:

* **Trend confirmation:** When both price and ADL move in the same direction, it confirms the current trend
* **Bullish divergence:** When price makes a lower low but ADL makes a higher low, it suggests underlying buying pressure despite price weakness
* **Bearish divergence:** When price makes a higher high but ADL makes a lower high, it suggests underlying selling pressure despite price strength
* **Support/resistance breakthrough:** Strong ADL movements can help confirm valid breakouts from support or resistance levels

## Limitations and Considerations

* **Market conditions:** Less effective in low-volume environments where price movements may not reflect significant buying or selling pressure
* **Lag factor:** As a cumulative indicator, ADL can be slow to signal reversals in strongly trending markets
* **False signals:** Single-day volume spikes (earnings reports, news events) can distort the indicator without representing actual accumulation or distribution
* **Complementary tools:** Best used alongside momentum indicators and price action analysis rather than in isolation

## References

* [Investopedia - Accumulation/Distribution Line](https://www.investopedia.com/terms/a/accumulationdistribution.asp)
* [StockCharts - Accumulation Distribution Line](https://school.stockcharts.com/doku.php?id=technical_indicators:accumulation_distribution_line)
