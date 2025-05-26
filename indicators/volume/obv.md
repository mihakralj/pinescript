# OBV: On Balance Volume

[Pine Script Implementation of OBV](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/obv.pine)

## Overview and Purpose

On Balance Volume (OBV), developed by Joseph Granville in the 1960s, is one of the most fundamental and widely-used volume indicators in technical analysis. OBV operates on the simple but powerful premise that volume precedes price movement, making it an essential tool for confirming trends and identifying potential reversals before they become apparent in price action.

The indicator works by adding the entire day's volume to a cumulative total when the closing price is higher than the previous close, and subtracting the entire day's volume when the closing price is lower. This binary approach creates a momentum oscillator that tracks the flow of volume in relation to price direction, providing insights into the underlying buying and selling pressure.

## Core Concepts

* **Volume precedes price**: Volume changes often signal future price movements
* **Binary volume allocation**: All volume assigned to either buyers or sellers based on close direction
* **Cumulative momentum**: Running total showing net volume accumulation over time
* **Trend confirmation**: Validates price movements through volume backing
* **Divergence detection**: Identifies potential reversals through OBV-price disconnects

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| No inputs required | N/A | OBV uses standard close and volume data | No adjustments needed - uses raw market data |

**Pro Tip:** OBV's power lies in its simplicity. The indicator requires no parameters, making it universally applicable across all timeframes and instruments. Focus on OBV direction, trend confirmation, and divergences rather than absolute values.

## Calculation and Mathematical Foundation

**Simplified explanation:**
OBV compares today's closing price to yesterday's closing price. If today's close is higher, add today's volume to the OBV total. If today's close is lower, subtract today's volume from the OBV total. If prices are unchanged, OBV remains the same.

**Technical formula:**
```
If Close > Previous_Close:
    OBV = Previous_OBV + Volume

If Close < Previous_Close:
    OBV = Previous_OBV - Volume

If Close = Previous_Close:
    OBV = Previous_OBV

Where:
- Close = Current period's closing price
- Previous_Close = Previous period's closing price
- Volume = Current period's trading volume
- Previous_OBV = Previous OBV value
```

**Implementation considerations:**
- First period OBV typically starts at 0 or first period's volume
- Equal closes leave OBV unchanged (neutral volume)
- Binary nature makes it simple but sometimes less nuanced than proportional methods

> 🔍 **Technical Note:** OBV's binary approach treats a 1-cent price increase the same as a $10 increase, focusing purely on direction rather than magnitude. This makes it excellent for trend confirmation but less sensitive to the degree of price movement.

## Interpretation Details

OBV provides multiple analytical perspectives:

* **Rising OBV:**
  - Indicates net volume accumulation (buying pressure)
  - More closes above previous closes than below
  - Suggests underlying strength and potential continuation
  - Confirms upward price trends when aligned

* **Falling OBV:**
  - Shows net volume distribution (selling pressure)
  - More closes below previous closes than above
  - Indicates underlying weakness and potential decline
  - Confirms downward price trends when aligned

* **OBV-Price Relationships:**
  - **Confirmation:** OBV and price moving in same direction (strong signal)
  - **Bullish divergence:** Price declining while OBV rising (potential reversal up)
  - **Bearish divergence:** Price rising while OBV falling (potential reversal down)
  - **Flat OBV:** Roughly equal buying/selling pressure (consolidation)

* **OBV Patterns:**
  - **Breakouts:** OBV breaking resistance/support often precedes price breakouts
  - **Double tops/bottoms:** OBV patterns can confirm or negate price patterns
  - **Trend lines:** OBV trend lines provide additional confirmation signals

## Trading Applications

**Primary Uses:**
- **Trend confirmation:** Validate price trends through volume backing
- **Divergence analysis:** Identify potential reversals before price signals
- **Breakout validation:** Confirm genuine breakouts vs. false signals
- **Support/resistance confirmation:** Volume-backed levels carry more significance

**Advanced Strategies:**
- **OBV breakouts:** Trade when OBV breaks significant levels ahead of price
- **Divergence trading:** Enter positions when OBV diverges from price direction
- **Trend strength assessment:** Rising OBV confirms strong trends, flat OBV warns of weakness
- **Volume dry-up identification:** Flat OBV during price moves indicates lack of conviction

## Signal Combinations

**Strong Bullish Signals:**
- Price breakout above resistance + OBV at new highs
- Bullish price pattern + OBV making higher highs and higher lows
- Price holding support + OBV showing accumulation (rising trend)

**Strong Bearish Signals:**
- Price breakdown below support + OBV at new lows
- Bearish price pattern + OBV making lower highs and lower lows
- Price hitting resistance + OBV showing distribution (falling trend)

**Warning Signals:**
- Price making new highs but OBV failing to confirm (bearish divergence)
- Price making new lows but OBV showing strength (bullish divergence)
- Strong price moves with flat or declining OBV (lack of volume confirmation)

## Comparison with Related Indicators

| Indicator | Volume Method | Best Use |
|-----------|---------------|----------|
| **OBV** | Binary (all-or-nothing) | Trend confirmation, basic divergence analysis |
| **PVT** | Proportional to price change | More sensitive to price movement magnitude |
| **ADL** | Based on close position in range | Intraday buying/selling pressure |
| **CMF** | Money flow over period | Short-term volume flow analysis |
| **VA** | Range-weighted allocation | Quality assessment of volume positioning |

## Limitations and Considerations

* **Binary nature:** Doesn't account for magnitude of price changes
* **Gap sensitivity:** Large gaps can distort OBV interpretation
* **Volume quality:** Requires accurate and consistent volume reporting
* **No normalization:** Different securities have different OBV scales
* **False signals:** Volume spikes don't always lead to sustained moves
* **Timeframe dependency:** Different timeframes may give conflicting signals

## Historical Context and Development

Joseph Granville introduced OBV in his 1963 book "Granville's New Key to Stock Market Profits." The indicator was revolutionary for its time, being one of the first to systematically combine price and volume data. Granville's work laid the foundation for modern volume analysis and established the principle that "volume precedes price."

## References

* Granville, Joseph (1963). Granville's New Key to Stock Market Profits. Prentice-Hall.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Schwager, J. D. (1996). Technical Analysis. John Wiley & Sons.
* Elder, Alexander (1993). Trading for a Living. John Wiley & Sons.
* Achelis, Steven B. (2000). Technical Analysis from A to Z. McGraw-Hill.
