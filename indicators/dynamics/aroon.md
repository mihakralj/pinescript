# AROON: Aroon Indicator

[Pine Script Implementation of AROON](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/aroon.pine)

## Overview and Purpose

The Aroon indicator is a technical analysis tool designed to identify trend changes and determine the strength of a trend by measuring the time between highs and lows. Developed by Tushar Chande in 1995, the name "Aroon" comes from the Sanskrit word meaning "dawn's early light," reflecting its purpose of detecting the early light of new trends. Unlike momentum oscillators that focus on price, Aroon measures time, providing a unique perspective on market dynamics. The indicator consists of two lines - Aroon Up and Aroon Down - which help traders identify when new trends are emerging, when trends are strengthening, and when markets are consolidating.

## Core Concepts

* **Time-based analysis:** Measures the elapsed time since the last high and low rather than price movements, providing insight into the timing of market extremes
* **Trend detection:** Identifies emerging trends earlier than many price-based indicators by focusing on when highs and lows occur within a period
* **Timeframe flexibility:** Functions effectively across multiple timeframes, with 25-period being traditional but adjustable based on trading horizons

The distinctive feature of Aroon is its focus on when price extremes occur rather than their magnitude. This time-based approach provides a different analytical perspective from most indicators. When recent highs occur, Aroon Up approaches 100; when recent lows occur, Aroon Down approaches 100. By analyzing the relationship between these two lines, traders can identify trend beginnings, trend strength, and consolidation periods more effectively than with many traditional indicators.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 25 | Controls the lookback period | Increase for longer-term analysis and fewer signals, decrease for shorter-term sensitivity |
| Source | Close | Price data used for high/low detection | Typically left at default; high/low sources are used internally |

**Pro Tip:** Watch for parallel movement of both Aroon lines in the middle range (30-70) - this often indicates a consolidation phase before a significant breakout, providing potential early entry points when one line finally begins to move toward 100.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Aroon measures how long it's been since a high or low was recorded within a specific time period. If the highest price of the last 25 days occurred today, Aroon Up would be 100. If it occurred 12.5 days ago, Aroon Up would be 50. This approach spotlights when trend-defining moves occur, not just how big they are.

**Technical formula:**
Aroon Up = ((Period - Bars since Highest High) ÷ Period) × 100
Aroon Down = ((Period - Bars since Lowest Low) ÷ Period) × 100

Where:
- Period is the lookback window (typically 25)
- "Bars since" refers to how many periods have passed since the event

> 🔍 **Technical Note:** Aroon's value diminishes linearly over time if no new extremes are recorded. This creates a natural decay that helps identify aging trends and consolidation periods better than many oscillators that can remain at extreme values indefinitely.

## Interpretation Details

Aroon can be used in various trading strategies:

* **Trend identification:** When Aroon Up crosses above Aroon Down, an uptrend may be emerging; when Aroon Down crosses above Aroon Up, a downtrend may be forming
* **Trend strength assessment:** When either line moves above 70, especially reaching toward 100, it indicates a strong trend in that direction
* **Consolidation detection:** When both lines move parallel to each other in the middle range (30-70), the market is likely consolidating
* **Early breakout signals:** When one line begins rising toward 100 after a period of consolidation, it often signals the beginning of a new trend
* **Trend exhaustion:** When a line that has been near 100 begins falling, it may indicate the trend is weakening

## Limitations and Considerations

* **Time focus limitations:** By focusing solely on time, Aroon may miss significant price movements that don't create new extremes
* **Period sensitivity:** Results vary significantly with different period settings
* **False signals:** Can generate misleading signals in choppy or ranging markets
* **Complementary analysis needed:** Best used alongside price action analysis and other indicators for confirmation
* **Lag factor:** Requires a complete period worth of data before generating reliable signals

## References

* Chande, Tushar. "The New Technical Trader," Wiley, 1994
* Pring, Martin J. "Technical Analysis Explained," McGraw-Hill, 2014
