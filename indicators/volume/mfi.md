# MFI: Money Flow Index

[Pine Script Implementation of MFI](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/mfi.pine)

## Overview and Purpose

The Money Flow Index (MFI) is a momentum oscillator that uses both price and volume data to measure buying and selling pressure. Often referred to as a "volume-weighted RSI," MFI incorporates volume into the traditional RSI calculation, making it more sensitive to market changes and providing a more comprehensive view of market sentiment. Developed by Gene Quong and Avrum Soudack, MFI ranges from 0 to 100 and is particularly effective at identifying overbought and oversold conditions, as well as potential reversal points.

Unlike the traditional RSI which only considers price changes, MFI multiplies price movement by volume, giving more weight to periods of high trading activity. This makes MFI particularly valuable for confirming price movements and identifying when significant volume is supporting or contradicting price trends.

## Core Concepts

* **Volume-weighted momentum:** Combines price movement with volume data for enhanced signal quality
* **Typical price calculation:** Uses average of high, low, and close prices for more stable price representation
* **Money flow direction:** Determines buying vs. selling pressure based on typical price changes
* **Bounded oscillator:** Values range from 0 to 100, making interpretation straightforward
* **Divergence detection:** Excellent for identifying when volume patterns diverge from price action

The fundamental principle is that significant price movements should be accompanied by substantial volume. When volume supports price direction, trends tend to continue; when volume contradicts price movement, reversals often follow.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| MFI Period | 14 | Number of periods for calculation | Shorter for more sensitive signals, longer for smoother trends |
| Overbought Level | 80 | Upper threshold for overbought conditions | Lower for more sensitive overbought signals (70-85 range) |
| Oversold Level | 20 | Lower threshold for oversold conditions | Higher for more sensitive oversold signals (15-30 range) |

**Pro Tip:** MFI is most effective when used in conjunction with price action analysis. Look for divergences between MFI and price - when price makes new highs but MFI fails to confirm, or vice versa. The 14-period default works well for most timeframes, but consider 10 periods for more responsive signals or 21 periods for smoother, less noisy readings.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MFI calculates a typical price for each period, determines if money flow is positive or negative based on price direction, multiplies this by volume, then applies RSI-style mathematics to create a bounded oscillator.

**Technical formula:**
```
Typical Price = (High + Low + Close) / 3
Raw Money Flow = Typical Price × Volume
Positive Money Flow = Raw Money Flow (when Typical Price > Previous Typical Price)
Negative Money Flow = Raw Money Flow (when Typical Price < Previous Typical Price)
Money Flow Ratio = Sum(Positive Money Flow, n) / Sum(Negative Money Flow, n)
MFI = 100 - (100 / (1 + Money Flow Ratio))
```

**Step-by-step calculation:**
```
1. Calculate typical price: (High + Low + Close) / 3
2. Calculate raw money flow: Typical Price × Volume
3. Determine direction: Compare current vs. previous typical price
4. Classify money flow: Positive if up, negative if down, zero if unchanged
5. Sum positive and negative money flows over period
6. Calculate money flow ratio: Positive sum / Negative sum
7. Apply RSI formula: 100 - (100 / (1 + Ratio))
```

> 🔍 **Technical Note:** The MFI formula is identical to RSI except it uses volume-weighted price changes instead of simple price changes. This makes MFI more sensitive to periods of high volume activity and provides better confirmation of price movements.

## Implementation Features

The Pine Script implementation includes several enhancements:

* **Robust calculation:** Handles missing volume data and prevents division by zero errors
* **Customizable levels:** Adjustable overbought and oversold thresholds
* **Visual signals:** Alert arrows when crossing extreme levels
* **Background coloring:** Color-coded zones for easy interpretation
* **Reference lines:** Clear midline (50) and threshold levels

## Visual Elements

The indicator displays:

* **Purple MFI Line:** Main oscillator line (width 2)
* **Red Overbought Line:** Dashed line at overbought level (default 80)
* **Green Oversold Line:** Dashed line at oversold level (default 20)
* **Gray Midline:** Dotted line at 50 for trend bias reference
* **Background Coloring:** Red in overbought zone, green in oversold zone, gray elsewhere
* **Alert Arrows:** ▼ when entering overbought, ▲ when entering oversold

## Interpretation Details

Money Flow Index provides several types of trading insights:

* **Overbought conditions:** MFI above 80 suggests potential selling pressure and possible reversal
* **Oversold conditions:** MFI below 20 indicates potential buying opportunity and possible bounce
* **Trend confirmation:** MFI moving in same direction as price confirms trend strength
* **Divergence signals:** MFI diverging from price often precedes trend reversals
* **Volume validation:** High MFI readings with rising prices confirm strong buying pressure
* **Midline significance:** MFI above 50 suggests bullish bias, below 50 indicates bearish bias

## Function Usage

```pine
mfi(len, src_high, src_low, src_close, src_vol)
```

**Parameters:**
* `len` (simple int): Period for MFI calculation (typically 14)
* `src_high` (series float): High price series
* `src_low` (series float): Low price series
* `src_close` (series float): Close price series
* `src_vol` (series float): Volume series

**Returns:** `float` - The MFI value (0-100)

## Trading Applications

* **Overbought/Oversold trading:** Buy near oversold levels (20), sell near overbought levels (80)
* **Divergence trading:** Look for MFI/price divergences for early reversal signals
* **Trend confirmation:** Use MFI to confirm breakouts and trend continuations
* **Volume analysis:** High MFI with strong price moves indicates institutional participation
* **Support/Resistance:** MFI extremes often coincide with key price levels
* **Multiple timeframe analysis:** Compare MFI across different timeframes for comprehensive view

## Comparison with Similar Indicators

* **vs. RSI:** MFI includes volume while RSI uses only price; MFI often provides earlier signals
* **vs. Chaikin Money Flow:** MFI is bounded 0-100 while CMF oscillates around zero
* **vs. On-Balance Volume:** MFI considers price magnitude while OBV uses only direction
* **vs. Volume Rate of Change:** MFI incorporates price changes while VROC focuses purely on volume
* **vs. Accumulation/Distribution:** MFI uses typical price while A/D uses intraday price position

## Advantages of MFI

* **Volume integration:** Provides more reliable signals by incorporating trading volume
* **Early warnings:** Often leads price movements, especially at extremes
* **Bounded nature:** Clear overbought/oversold levels make interpretation straightforward
* **Divergence detection:** Excellent at identifying when volume patterns conflict with price
* **Market sentiment:** Effectively measures the intensity of buying and selling pressure

## Limitations and Considerations

* **Volume dependency:** Requires reliable volume data; less effective with poor volume reporting
* **False signals:** Can generate premature signals in trending markets
* **Lag:** Like all oscillators, MFI lags price action and may miss rapid reversals
* **Market context:** More effective in ranging markets than strong trending environments
* **Time sensitivity:** Different periods can produce conflicting signals
* **Volume anomalies:** Unusual volume spikes can distort readings temporarily

## Advanced Analysis Techniques

* **Failure swings:** MFI failing to reach previous extremes while price does can signal reversals
* **50-line analysis:** Use midline crossovers for trend bias confirmation
* **Multiple divergences:** Look for divergence patterns across multiple timeframes
* **Volume profile integration:** Compare MFI with volume profile data for comprehensive analysis
* **Sector rotation:** Use MFI to identify when money flows between different market sectors

## Market Context Applications

* **Bull markets:** Focus on oversold bounces and trend confirmations
* **Bear markets:** Emphasize overbought failures and distribution signals
* **Sideways markets:** Most effective environment for traditional overbought/oversold trading
* **High volatility:** Adjust thresholds wider (15-85) to avoid excessive signals
* **Low volatility:** Tighten thresholds (25-75) for more responsive signals

## References

* Quong, Gene, and Avrum Soudack. "Technical Analysis of Stocks & Commodities." 1989.
* Murphy, John J. "Technical Analysis of the Financial Markets." New York Institute of Finance, 1999.
* Pring, Martin J. "Technical Analysis Explained." McGraw-Hill, 2002.
* Achelis, Steven B. "Technical Analysis from A to Z." McGraw-Hill, 2000.
* Colby, Robert W. "The Encyclopedia of Technical Market Indicators." McGraw-Hill, 2003.
