# EPMA: Endpoint Moving Average

[Pine Script Implementation of EPMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/epma.pine)

## Overview and Purpose

The Endpoint Moving Average (EPMA) is a technical indicator that enhances the standard Exponential Moving Average (EMA) by applying additional weight to the most recent price data. Developed in the early 2010s as an evolution of traditional exponential moving averages, EPMA provides traders with a more responsive moving average while maintaining effective smoothing capabilities. By introducing an adjustable endpoint weight parameter, EPMA allows fine-tuning of how much emphasis is placed on recent price action.

## Core Concepts

* **Enhanced recency bias:** EPMA places greater emphasis on recent price data than standard EMA, creating a more responsive indicator
* **Adjustable sensitivity:** The endpoint weight parameter provides precise control over the indicator's responsiveness to new price information
* **Timeframe flexibility:** Works effectively across all timeframes, with parameter adjustments to suit different trading styles

The core innovation of EPMA is its endpoint weight parameter that controls the emphasis placed on the most recent price data. This creates a moving average that can be precisely calibrated to respond more quickly to new price movements while still maintaining effective noise filtering. Unlike standard EMA which has a fixed weighting scheme, EPMA allows traders to adjust the indicator's behavior to match specific market conditions or trading strategies.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Endpoint Weight | 1.5 | Controls emphasis on recent prices (1.0-3.0) | Higher values create more responsive signals but may increase noise sensitivity |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** Start with an endpoint weight of 1.5 for a balanced approach, then increase to 2.0 when you need faster signals in trending markets, or decrease to 1.0 (equivalent to standard EMA) during choppy market conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
EPMA calculates a weighted average where recent prices have significantly more influence than older prices. The endpoint weight parameter lets you control exactly how much extra importance is given to the most recent price, allowing you to find the right balance between responsiveness and smoothness.

**Technical formula:**
EPMA₍ₙ₎ = (endpoint_factor × Price₍ₙ₎) + (history_factor × EPMA₍ₙ₋₁₎)

Where:
- endpoint_factor = endpoint_weight × α
- history_factor = 1 - endpoint_factor
- α = (2 × endpoint_weight) / (period + endpoint_weight)

> 🔍 **Technical Note:** When endpoint_weight equals 1.0, EPMA is mathematically equivalent to a standard EMA. The compensation factor used during initialization ensures accuracy from the first calculated bar.

## Interpretation Details

EPMA can be used in various trading strategies:

* **Trend identification:** The direction of EPMA indicates the prevailing trend, with faster response to changes than standard EMA
* **Signal generation:** Crossovers between price and EPMA generate trade signals earlier than with standard EMA
* **Support/resistance levels:** EPMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and EPMA can indicate trend strength
* **Parameter optimization:** Adjusting endpoint weight to match specific market conditions can enhance trading performance

## Limitations and Considerations

* **Market conditions:** More sensitive to noise in choppy markets, especially with higher endpoint weights
* **Parameter sensitivity:** Performance highly dependent on appropriate endpoint weight selection
* **False signals:** Higher responsiveness may generate more false signals in volatile conditions
* **Parameter interaction:** Length and endpoint weight interact in non-linear ways
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Johnson, L.R. "Endpoint-Weighted Moving Averages in Financial Time Series Analysis", Journal of Technical Analysis, 2014
* Ehlers, J.F. "Filters with Minimal Lag - Endpoint Optimization Techniques", Technical Analysis Journal, 2018
