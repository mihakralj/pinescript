# VA: Volume Accumulation

[Pine Script Implementation of VA](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/va.pine)

## Overview and Purpose

Volume Accumulation (VA), created by Mark Chaikin, is a technical indicator that shows the cumulative volume adjusted by the relationship between the closing price and the midpoint of the day's range. Unlike the On Balance Volume (OBV) indicator which assigns all of a period's volume to either buyers or sellers based solely on whether the close is higher or lower, Volume Accumulation provides a more nuanced approach by proportionally distributing volume based on where the close falls within the day's range.

This proportional allocation makes VA particularly effective at identifying the quality of volume behind price movements, as it recognizes that closes near the high of the range indicate stronger buying pressure than closes in the middle or lower portion of the range, even when both result in positive price movement.

## Core Concepts

* **Proportional volume allocation**: Distributes volume based on close position relative to midpoint
* **Cumulative measurement**: Running total showing net volume accumulation over time
* **Range-weighted analysis**: Uses the relationship between close and range midpoint
* **Trend confirmation**: Validates price movements through volume quality assessment
* **Divergence detection**: Identifies potential reversals through VA-price disconnects

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| No inputs required | N/A | VA uses standard OHLC and volume data | No adjustments needed - uses raw market data |

**Pro Tip:** VA works best on instruments with consistent volume reporting and clear daily ranges. It's most effective on stocks, futures, and other instruments where high, low, close, and volume data are reliable and meaningful.

## Calculation and Mathematical Foundation

**Simplified explanation:**
VA calculates the difference between the closing price and the midpoint of the day's range (high+low)/2, then multiplies this difference by the volume. This value is added to a cumulative total, creating a running sum that reflects volume-weighted price positioning.

**Technical formula:**
```
Midpoint = (High + Low) / 2
VA_Period = Volume × (Close - Midpoint)
VA_Cumulative = Sum of all VA_Period values

Where:
- High = Period's highest price
- Low = Period's lowest price  
- Close = Period's closing price
- Volume = Period's trading volume
```

**Interpretation of calculation:**
- When Close > Midpoint: Positive VA (volume attributed to buyers)
- When Close < Midpoint: Negative VA (volume attributed to sellers)
- When Close = Midpoint: Zero VA (neutral volume)
- Magnitude depends on both volume size and distance from midpoint

> 🔍 **Technical Note:** The midpoint calculation (High+Low)/2 represents the theoretical balance point of the trading range, making it a more sophisticated reference than just the previous close used in OBV.

## Interpretation Details

VA provides multiple analytical perspectives:

* **Rising VA Line:**
  - Indicates net volume accumulation with buying bias
  - Closes consistently above range midpoints
  - Suggests underlying strength and buyer control
  - Confirms upward price trends when aligned

* **Falling VA Line:**
  - Shows net volume distribution with selling bias
  - Closes consistently below range midpoints
  - Indicates underlying weakness and seller control
  - Confirms downward price trends when aligned

* **VA-Price Relationships:**
  - **Confirmation:** VA and price moving in same direction
  - **Bullish divergence:** Price declining while VA rising (accumulation during weakness)
  - **Bearish divergence:** Price rising while VA falling (distribution during strength)
  - **Neutral phase:** VA flat while price moves (lack of conviction)

* **VA Acceleration/Deceleration:**
  - **Accelerating VA:** Increasing slope indicates strengthening trend
  - **Decelerating VA:** Decreasing slope suggests weakening momentum
  - **VA reversal:** Sharp direction change often precedes price reversal

## Trading Applications

**Primary Uses:**
- **Trend confirmation:** Validate price trends through volume quality
- **Divergence analysis:** Identify potential reversal points before they occur
- **Accumulation/distribution phases:** Recognize smart money activity
- **Breakout validation:** Confirm genuine breakouts vs. false signals

**Advanced Strategies:**
- **Volume quality assessment:** Strong trends show accelerating VA in trend direction
- **Support/resistance confirmation:** VA behavior at key levels validates importance
- **Sector rotation analysis:** Compare VA across related securities
- **Long-term positioning:** Use VA for identifying major accumulation/distribution phases

## Signal Combinations

**Strong Bullish Signals:**
- Rising price + accelerating positive VA
- Price at resistance + VA making new highs
- Bullish chart pattern + positive VA divergence

**Strong Bearish Signals:**
- Falling price + accelerating negative VA
- Price at support + VA making new lows
- Bearish pattern + negative VA divergence

**Warning Signals:**
- Price breakout + flat or declining VA
- New price highs/lows + VA divergence
- Sideways price + extremely active VA

## Comparison with OBV

| Aspect | Volume Accumulation (VA) | On Balance Volume (OBV) |
|--------|--------------------------|-------------------------|
| **Volume Assignment** | Proportional based on close position in range | All-or-nothing based on close direction |
| **Sensitivity** | More nuanced, recognizes partial accumulation | Binary, only recognizes full accumulation/distribution |
| **Noise Filtering** | Better at filtering insignificant movements | More susceptible to noise from small price changes |
| **Range Analysis** | Incorporates intraday high/low information | Only uses close-to-close comparison |
| **Best Use** | Quality assessment of volume behind moves | Simple trend confirmation and divergence |

## Limitations and Considerations

* **Range dependency:** Less effective on instruments with limited intraday ranges
* **Volume quality:** Requires accurate and consistent volume reporting
* **Market hours:** May be distorted by overnight gaps or extended trading sessions
* **Cumulative nature:** Historical bias can affect current readings
* **False signals:** Strong volume spikes can temporarily distort readings
* **Timeframe sensitivity:** Different timeframes may give conflicting signals

## References

* Chaikin, Marc (1986). Chaikin Oscillator and Money Flow. Stock & Commodities Magazine.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Schwager, J. D. (1996). Technical Analysis. John Wiley & Sons.
* Elder, Alexander (1993). Trading for a Living. John Wiley & Sons.
* Achelis, Steven B. (2000). Technical Analysis from A to Z. McGraw-Hill.
