# VWMA: Volume Weighted Moving Average

[Pine Script Implementation of VWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/vwma.pine)

## Overview and Purpose

The Volume Weighted Moving Average (VWMA) is a technical indicator that incorporates trading volume as a weighting factor in its calculation. Developed in the 1970s during the early days of computerized technical analysis, VWMA gained popularity as traders recognized the importance of volume confirmation in price movements. By integrating volume data into the moving average formula, VWMA creates a more comprehensive view of market activity that emphasizes price movements occurring during periods of higher trading volume, which often have greater significance in determining trend direction and strength.

## Core Concepts

* **Volume-price integration:** VWMA incorporates volume as a weighting factor, giving more importance to price movements that occur on higher volume
* **Market significance filtering:** Emphasizes price changes backed by significant volume while de-emphasizing those occurring on low volume
* **Timeframe flexibility:** Effective across multiple timeframes, with particular value in daily and weekly charts where volume analysis is most reliable

The core innovation of VWMA is its recognition that not all price movements are equal - those occurring with higher volume typically represent stronger market conviction and are more likely to indicate genuine trend direction. By weighting each price by its corresponding volume before averaging, VWMA creates an indicator that responds more strongly to high-volume price movements while reducing the influence of price changes that occur on minimal volume.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |
| Volume | volume | Volume data used for weighting | Typically left at default; can be substituted with custom volume metrics in specialized analyses |

**Pro Tip:** VWMA tends to perform best in markets with consistent and reliable volume data - stock markets and major futures contracts typically provide the most meaningful volume information compared to forex or thinly traded instruments.

## Calculation and Mathematical Foundation

**Simplified explanation:**
VWMA calculates a weighted average of prices where the weights are determined by trading volume. Prices from periods with higher trading volume have more influence on the average than those with lower volume. This creates a moving average that emphasizes price movements backed by significant trading activity.

**Technical formula:**
VWMA = Σ(Price[i] × Volume[i]) / Σ(Volume[i])

Where:
- Price[i] represents the price at position i in the lookback window
- Volume[i] represents the volume at position i in the lookback window
- The formula simply divides the sum of price×volume products by the sum of all volumes in the period

> 🔍 **Technical Note:** Unlike weighted moving averages that use arbitrary weighting schemes, VWMA uses actual trading volume as the weight, making it responsive to real market activity rather than mathematical constructs.

## Interpretation Details

VWMA can be used in various trading strategies:

* **Trend identification:** The direction of VWMA indicates the prevailing trend with volume confirmation
* **Signal generation:** Crossovers between price and VWMA generate potentially more reliable signals than standard moving averages due to volume validation
* **Support/resistance levels:** VWMA can act as stronger dynamic support/resistance levels than simple moving averages, especially on high-volume tests
* **Divergence analysis:** Comparing VWMA behavior to other moving averages can highlight the impact of volume on price movement
* **Volume-confirmed breakouts:** VWMA crossing above/below key levels with expanding volume provides stronger confirmation than price action alone

## Limitations and Considerations

* **Market conditions:** Requires reliable volume data to be effective; less useful in markets with inconsistent volume reporting
* **Lag factor:** Still introduces some lag in signal generation, though typically less than simple moving averages
* **Volume spikes:** Can be temporarily distorted by abnormal volume events (earnings releases, news events)
* **Weekend gaps:** In markets that close (stocks, futures), weekend gaps with no volume can create discontinuities
* **Complementary tools:** Best used alongside price pattern analysis and other confirmation indicators

## References

* Achelis, Steven B. "Technical Analysis from A to Z." McGraw-Hill, 2000
* Kirkpatrick, Charles D. and Dahlquist, Julie R. "Technical Analysis: The Complete Resource for Financial Market Technicians." FT Press, 2010
