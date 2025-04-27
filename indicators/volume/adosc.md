# ADOSC: Chaikin Accumulation/Distribution Oscillator

[Pine Script Implementation of ADOSC](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/adosc.pine)

## Overview and Purpose

The Chaikin Accumulation/Distribution Oscillator (ADOSC) is a momentum indicator that measures the buying and selling pressure in a security by analyzing the relationship between price and volume. Developed by Marc Chaikin in the 1970s, this oscillator builds upon the Accumulation/Distribution Line (ADL) by applying a momentum formula to detect changes in the flow of money into or out of a security. By comparing the difference between two exponential moving averages (EMAs) of the ADL, ADOSC helps identify potential turning points in price action.

## Core Concepts

* **Volume flow momentum:** ADOSC measures the momentum of the volume flow by comparing fast and slow EMAs of the ADL, highlighting acceleration and deceleration in buying/selling pressure
* **Market application:** Particularly effective for identifying divergences between price and volume flow, signaling potential reversals before they appear in price action
* **Timeframe suitability:** Functions across all timeframes, but most valuable on daily charts for spotting significant shifts in institutional money flow

The ADOSC's core principle builds on the foundation that volume precedes price movement. When institutional investors begin accumulating or distributing positions, the indicator helps detect these activities before they fully manifest in price changes. The oscillator fluctuates above and below a zero line, with positive values indicating accumulation (buying pressure) and negative values indicating distribution (selling pressure).

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Short Period | 3 | Controls the sensitivity of the fast EMA | Lower for more responsive signals in volatile markets, higher for fewer false signals |
| Long Period | 10 | Controls the sensitivity of the slow EMA | Adjust based on trading timeframe - higher values for longer-term analysis |

**Pro Tip:** The 3-10 day setting combination tends to be effective for most traders, but try widening the gap between short and long periods (e.g., 3-16) to generate fewer but potentially more significant signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ADOSC first calculates the Accumulation/Distribution Line, which measures money flow by considering where prices close within their range and weighting by volume. It then calculates the difference between a fast EMA and a slow EMA of this line to determine momentum.

**Technical formula:**
1. Money Flow Multiplier = ((Close - Low) - (High - Close)) / (High - Low)
2. Money Flow Volume = Money Flow Multiplier × Volume
3. ADL = Previous ADL + Current Money Flow Volume
4. ADOSC = EMA(ADL, Short Period) - EMA(ADL, Long Period)

> 🔍 **Technical Note:** Unlike simple moving averages, the EMAs used in ADOSC give more weight to recent data, making the oscillator more responsive to changes in buying/selling pressure.

## Interpretation Details

The ADOSC generates several types of actionable signals:

* **Zero line crossovers:** When ADOSC crosses above zero, it indicates a shift toward accumulation (potential buy signal); crossing below zero indicates distribution (potential sell signal)
* **Divergences:** When price makes a new high but ADOSC fails to confirm with a new high, it signals potential weakness (bearish divergence); conversely, when price makes a new low but ADOSC makes a higher low, it indicates potential strength (bullish divergence)
* **Trend confirmation:** Strong readings in the direction of the price trend help confirm the trend's strength
* **Overbought/oversold conditions:** Extreme readings on the oscillator may indicate potential reversal points

## Limitations and Considerations

* **Market conditions:** Less reliable in thinly traded securities where volume may be inconsistent
* **Lag factor:** As a derivative of ADL which itself is cumulative, ADOSC can sometimes be slow to signal major shifts
* **False signals:** Like many oscillators, ADOSC can generate false signals during strong trends or when volume patterns are irregular
* **Complementary tools:** Most effective when used in conjunction with price analysis, trend indicators, and other volume indicators for confirmation

## References

* [Investopedia - Chaikin Oscillator](https://www.investopedia.com/terms/c/chaikinoscillator.asp)
* [StockCharts - Chaikin Oscillator](https://school.stockcharts.com/doku.php?id=technical_indicators:chaikin_oscillator)
