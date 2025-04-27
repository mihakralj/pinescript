# DIRTY: Dirty Data Injection

[Pine Script Implementation of DIRTY](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/dirty.pine)

## Overview and Purpose

The Dirty Data Injection utility is a specialized testing tool designed to evaluate the robustness of trading indicators and systems when faced with incomplete or missing data. In real-world trading scenarios, data gaps frequently occur due to various factors including feed disruptions, exchange outages, or thin trading periods. By deliberately injecting NA (Not Available) values into a data series at regular intervals, this utility allows developers to stress-test their indicators and systems to ensure they degrade gracefully when faced with imperfect data conditions.

## Core Concepts

* **Robustness testing:** Simulates real-world data imperfections to verify indicator behavior under suboptimal conditions
* **Systematic injection:** Creates predictable patterns of missing data to ensure reproducible testing
* **Market application:** Particularly valuable during indicator development to ensure reliability in live trading environments

The core purpose of Dirty Data Injection is validation rather than analysis. By introducing controlled imperfections into otherwise clean data, developers can identify potential failure points in their indicators and trading systems before deploying them in live environments where unexpected data issues could lead to significant problems.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Interval | 10 | Controls frequency of NA value injections | Decrease for more aggressive testing, increase for more subtle testing |
| Source | close | Data series to inject NAs into | Typically left at default; can be changed to test different data series |

**Pro Tip:** After designing a new indicator, test it with increasingly aggressive dirty data injection (shorter intervals) to determine its breaking point. Then implement appropriate error handling to gracefully manage at least twice that level of data corruption.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The utility uses a simple modulo operation to identify which bars should be replaced with NA values. The first bar and every nth bar thereafter (based on the interval setting) will be converted to NA, creating a systematic pattern of missing data.

**Technical implementation:**
1. Sets the first bar to NA
2. Uses the modulo operator to identify bars at the specified interval
3. Replaces values at these positions with NA
4. Plots the resulting series with visual indicators to highlight missing data points

> 🔍 **Technical Note:** While random data corruption might seem more realistic, systematic interval-based corruption provides reproducible test conditions that make debugging and validation more reliable.

## Interpretation Details

This utility is not meant for market analysis but rather for indicator testing:

* **Indicator validation:** Verify that indicators handle missing data appropriately without generating erroneous signals
* **System testing:** Ensure trading systems degrade gracefully rather than catastrophically when data is incomplete
* **Error handling assessment:** Evaluate the effectiveness of NA-handling code in custom indicators
* **Visualization testing:** Confirm that charts and plots properly represent missing data points
* **Stability verification:** Check that calculations involving moving windows properly account for missing values

## Limitations and Considerations

* **Testing purpose only:** This is a development utility, not an analytical tool for trading decisions
* **Synthetic pattern:** Creates a regular pattern of missing data rather than the more random patterns that occur in real markets
* **Single-dimension testing:** Only tests for complete data absence (NA), not for other data quality issues like spikes or errors
* **Visual impact:** When used on charts, creates discontinuous visualization that may be difficult to interpret
* **System requirements:** Should be disabled before deploying indicators to production environments

## References

* Pardo, R. "The Evaluation and Optimization of Trading Strategies," Wiley, 2008
* Davey, K.J. "Building Algorithmic Trading Systems: A Trader's Journey From Data Mining to Monte Carlo Simulation," Wiley, 2014
