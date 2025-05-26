# III: Intraday Intensity Index

[Pine Script Implementation of III](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/iii.pine)

## Overview and Purpose

The Intraday Intensity Index (III) is a volume-weighted indicator that measures buying and selling pressure within each trading session by analyzing where the closing price falls within the day's trading range. Unlike simple volume indicators, III considers both the volume traded and the relative position of the close within the high-low range, providing insights into whether volume was associated with buying pressure (close near high) or selling pressure (close near low).

Developed by David Bostian, the III helps traders understand the quality of volume by weighting it according to the close's position in the daily range. When the close is near the high, the index is positive, indicating buying pressure. When the close is near the low, the index is negative, indicating selling pressure. This makes III particularly valuable for confirming price movements and identifying potential reversals.

## Core Concepts

* **Volume-weighted analysis**: Combines volume with price position for quality assessment
* **Intraday pressure measurement**: Evaluates buying vs. selling pressure within each session
* **Range-relative positioning**: Uses close position within high-low range as pressure indicator
* **Cumulative analysis**: Often smoothed or accumulated for trend identification
* **Confirmation tool**: Validates price movements with volume-based pressure analysis

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Smoothing period for the intensity index | Shorter (7-10) for more sensitive signals, longer (21-30) for smoother trends |
| Volume Source | volume | Volume data to weight the intensity | Use different volume sources (real volume, tick volume) based on data availability |
| Cumulative Mode | false | Whether to accumulate intensity values | Enable for long-term trend analysis, disable for oscillator behavior |

**Pro Tip:** Use III in conjunction with price action analysis. Strong price moves confirmed by high positive III values (buying pressure) or high negative III values (selling pressure) tend to be more sustainable than moves with neutral intensity.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Intraday Intensity Index calculates a multiplier based on where the close falls within the day's range, then multiplies this by volume. If the close is exactly at the high, the multiplier is +1. If at the low, it's -1. If at the midpoint, it's 0.

**Technical formula:**
```
Range = High - Low
Close_Position = ((Close - Low) - (High - Close)) / Range
Close_Position = (2 * Close - High - Low) / Range

Raw_III = Close_Position * Volume

Smoothed_III = SMA(Raw_III, period)
```

**Alternative calculation (equivalent):**
```
if High != Low:
    III = ((Close - Low) - (High - Close)) / (High - Low) * Volume
else:
    III = 0

Smoothed_III = SMA(III, period)
```

**Implementation considerations:**
- Handle zero range (High = Low) to avoid division by zero
- Raw values can be very large due to volume multiplication
- Smoothing helps identify trends in buying/selling pressure
- Positive values indicate net buying pressure, negative indicate selling pressure

> 🔍 **Technical Note:** The position multiplier ranges from -1 to +1, where +1 means close equals high (maximum buying pressure) and -1 means close equals low (maximum selling pressure). Multiplying by volume weights the pressure by participation level.

## Interpretation Details

The Intraday Intensity Index provides multiple analytical perspectives:

* **Positive Values (Above Zero):**
  - Close above the midpoint of the day's range
  - Net buying pressure during the session
  - Volume associated with upward price movement
  - Suggests accumulation or bullish sentiment

* **Negative Values (Below Zero):**
  - Close below the midpoint of the day's range
  - Net selling pressure during the session
  - Volume associated with downward price movement
  - Suggests distribution or bearish sentiment

* **Magnitude Analysis:**
  - **High positive values**: Strong buying pressure with high volume
  - **High negative values**: Strong selling pressure with high volume
  - **Values near zero**: Neutral pressure or close near midpoint
  - **Extreme values**: Indicate strong conviction in price direction

* **Trend Analysis:**
  - **Rising III**: Increasing buying pressure over time
  - **Falling III**: Increasing selling pressure over time
  - **III divergence**: Pressure direction differs from price direction
  - **III confirmation**: Pressure direction aligns with price movement

## Trading Applications

**Primary Uses:**
- **Trend confirmation**: Verify price trends with volume-weighted pressure analysis
- **Divergence detection**: Identify potential reversals when III and price diverge
- **Breakout validation**: Confirm breakouts with supporting pressure intensity
- **Entry timing**: Use pressure shifts to time position entries and exits

**Advanced Strategies:**
- **Pressure divergence trading**: Trade when III trends opposite to price
- **Volume quality assessment**: Focus on moves with high absolute III values
- **Accumulation/Distribution analysis**: Identify phases of buying or selling pressure
- **Support/Resistance confirmation**: Validate key levels with pressure analysis

## Signal Combinations

**Strong Bullish Signals:**
- Rising prices + increasing positive III (confirmed buying pressure)
- Bullish divergence (price makes lower low, III makes higher low)
- Breakout above resistance + high positive III values

**Strong Bearish Signals:**
- Falling prices + increasing negative III (confirmed selling pressure)
- Bearish divergence (price makes higher high, III makes lower high)
- Breakdown below support + high negative III values

**Warning Signals:**
- Price advance with declining or negative III (weak buying pressure)
- Price decline with rising or positive III (weak selling pressure)
- Extreme III values may indicate exhaustion or climax conditions

## Comparison with Related Volume Indicators

| Indicator | Focus | Calculation | Best Use |
|-----------|-------|-------------|----------|
| **Intraday Intensity** | Intraday pressure | Close position × Volume | Session-based pressure analysis |
| **On Balance Volume** | Cumulative flow | Direction-based accumulation | Long-term trend confirmation |
| **Accumulation/Distribution** | Money flow | Close position + volume | Continuous pressure measurement |
| **Chaikin Money Flow** | Money flow pressure | Multi-period close position average | Smoothed pressure analysis |

## Limitations and Considerations

* **Range dependency**: Requires meaningful high-low ranges for accurate calculation
* **Volume quality**: Effectiveness depends on reliable volume data
* **Intraday focus**: Primarily designed for daily or intraday analysis
* **Smoothing lag**: Moving average smoothing creates inherent delay in signals
* **Market context**: Different markets may have different normal intensity patterns
* **Gap situations**: Opening gaps can affect range-based calculations

## Advanced Configurations

**Short-term Analysis:**
- Period: 7, Raw values for immediate pressure assessment

**Standard Setup:**
- Period: 14, Smoothed for trend identification

**Long-term Analysis:**
- Period: 21, Heavily smoothed for major trend confirmation

**Oscillator Mode:**
- Cumulative: false, Period: 10-14 for swing analysis

**Trend Mode:**
- Cumulative: true, Period: 5-7 for direction bias

## Intraday Intensity Patterns

**Classic Patterns:**
- **Positive divergence**: Price falls while III rises (buying pressure building)
- **Negative divergence**: Price rises while III falls (selling pressure building)
- **Pressure exhaustion**: Extreme III values followed by reversal
- **Pressure confirmation**: III direction matches price trend

**Signal Quality:**
- **Strong signals**: High absolute III values with clear direction
- **Weak signals**: III values near zero or conflicting with price
- **Best signals**: III extremes at support/resistance levels with volume confirmation

## Market Applications

**Daily Trading:**
- Assess intraday buying/selling pressure for position management
- Confirm daily breakouts or breakdowns with intensity analysis
- Identify potential reversal points through pressure divergence

**Swing Trading:**
- Use smoothed III for intermediate-term pressure trends
- Combine with price action for high-probability setups
- Monitor pressure shifts for trend continuation or reversal signals

**Position Trading:**
- Apply longer smoothing periods for major trend confirmation
- Focus on persistent pressure direction for strategic positioning
- Use III divergence for early trend change warnings

## References

* Bostian, David. Technical Analysis for the Trading Professional. McGraw-Hill.
* Achelis, Steven B. (2000). Technical Analysis from A to Z. McGraw-Hill.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, Martin J. (2002). Technical Analysis Explained. McGraw-Hill.
* Elder, Alexander (1993). Trading for a Living. John Wiley & Sons.
