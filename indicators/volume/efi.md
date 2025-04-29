# EFI: Elder's Force Index

[Pine Script Implementation of EFI](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/efi.pine)

## Overview and Purpose

The Elder's Force Index (EFI) is a volume-price oscillator developed by Dr. Alexander Elder that measures the force (or power) behind price movements. Combining price change with volume, EFI provides a comprehensive view of the strength behind market moves, helping traders assess the conviction of bulls or bears. Unlike simple volume studies, EFI reveals not just the presence of activity but its direction and intensity, making it particularly valuable for trend confirmation and divergence analysis.

The indicator oscillates above and below a zero line, with positive values indicating buying pressure and negative values indicating selling pressure. By measuring both the direction of price change and the volume behind it, EFI helps traders identify the "force" driving the market, which can be more revealing than price movements alone.

## Core Concepts

* **Force measurement:** Measures the power behind price movements by combining price change and volume
* **Trend strength assessment:** Evaluates whether current price movements are supported by sufficient volume
* **Multi-timeframe utility:** Functions effectively across all timeframes, with different settings providing short-term or long-term perspectives
* **Smoothing mechanism:** Uses exponential moving average (EMA) to reduce noise while preserving significant signals

The indicator's fundamental principle is that significant price moves should be accompanied by significant volume. When price increases with high volume, EFI rises sharply; when price falls with high volume, EFI falls sharply. The magnitude of EFI readings provides insight into the strength of market forces, while the direction indicates whether buying or selling pressure dominates.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 13 | Lookback period for EMA smoothing | Shorter for more sensitivity/signals, longer for stronger trend focus |
| Price Source | Close | Price data for calculating change | Rarely needs adjustment |
| Volume Source | Volume | Volume data for weighting price change | Consider adjusting when analyzing unusual volume characteristics |

**Pro Tip:** Elder recommended a 13-period EFI for identifying short-term trends and a 2-period EFI for very short-term signals. Consider using multiple timeframes simultaneously – a 13-period EFI crossing above zero confirms uptrends on the intermediate timeframe, while a 2-period EFI can pinpoint precise entry timing.

## Calculation and Mathematical Foundation

**Simplified explanation:**
EFI multiplies the change in price by volume to determine the "force" behind the move. This raw force value is then smoothed using an exponential moving average (EMA) to reduce noise and highlight significant trends.

**Technical formula:**

1. Raw Force = (Current Close - Previous Close) × Volume
2. EFI = EMA(Raw Force, Length)

> 🔍 **Technical Note:** The implementation handles initialization bias by using a specialized warmup procedure that corrects EMA values during the early calculation phase. This ensures accurate EFI values even with limited historical data, preventing the common EMA initialization bias.

## Interpretation Details

The Elder's Force Index provides several types of actionable signals:

* **Zero line crossovers:** When EFI crosses above zero, it indicates net buying pressure (potential buy signal); crossing below zero indicates net selling pressure (potential sell signal)
* **Divergences:** When price makes a new high but EFI fails to confirm with a new high, it signals potential weakness (bearish divergence); conversely, when price makes a new low but EFI makes a higher low, it indicates potential strength (bullish divergence)
* **Extreme readings:** Unusually high or low EFI values suggest overextended conditions that may lead to reversals
* **Trend confirmation:** Strong readings in the direction of the price trend help confirm the trend's validity
* **Multiple timeframe analysis:** Comparing EFI across different timeframes helps identify alignment or conflict between short-term and long-term forces

## Limitations and Considerations

* **Volume dependency:** Less reliable in markets with inconsistent or manipulated volume data
* **Lagging component:** Due to EMA smoothing, EFI can sometimes lag significant price moves
* **False signals:** Can generate misleading signals during choppy market conditions or low-volume periods
* **Normalization issues:** Different securities may have different typical EFI ranges, making direct comparisons challenging
* **Complementary analysis:** Works best when combined with price action analysis and other technical indicators
* **Warmup requirements:** Requires sufficient historical data to generate reliable signals, particularly with longer length settings

## References

* Elder, A. (1993). Trading for a Living: Psychology, Trading Tactics, Money Management. John Wiley & Sons.
* Elder, A. (2002). Come Into My Trading Room: A Complete Guide to Trading. John Wiley & Sons.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
