# JVOLTYN: Normalized Jurik Volatility

[Pine Script Implementation of JVOLTYN](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/jvoltyn.pine)

## Overview and Purpose

Normalized Jurik Volatility (JVOLTYN) compresses the raw Jurik Volatility (JVOLTY) output onto a bounded 0–1 scale via a sigmoid transformation. The result offers a quick, dimension‑less reading of how “hot” or “cold” the market is relative to its own recent activity, eliminating units and simplifying comparative scans across symbols and timeframes. Traders employ JVOLTYN as a volatility oscillator for breakout timing, position‑sizing caps, and risk‑on/off dashboards.

## Core Concepts

* **Sigmoid normalization** — maps unbounded JVOLTY ratios to [0 , 1] for intuitive interpretation  
* **Adaptive responsiveness** — inherits Jurik smoothing, providing swift detection of regime shifts with low noise  
* **Volatility oscillator** — behaves like an RSI of volatility, enabling overbought/oversold‑style thresholds  

Market application:  
* **Breakout filter:** act only when JVOLTYN > 0.7 (high energy)  
* **Risk dial:** scale leverage linearly to JVOLTYN; cap risk when > 0.9  
* **Mean‑reversion:** seek fades when JVOLTYN < 0.3

Timeframe suitability:  
* **All frames**—intraday scalps to multi‑day swing; normalization keeps values consistent.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 10 | Underlying JVOLTY calculation window | Shorten for faster spikes, lengthen to smooth |
| Source | Close | Price input | HL2 for range emphasis |
| Sigmoid Strength | 2 | Steepness of 0–1 mapping | Increase for crisper extremes |

**Pro Tip:** Use dual thresholds: enter momentum trades when JVOLTYN crosses above 0.65 and exit when it falls back below 0.45—this avoids whipsaws during volatility collapses.

## Calculation and Mathematical Foundation

**Simplified explanation:**  
Calculate JVOLTY, then pass it through a logistic (sigmoid) function so values hug 0 in calm periods and approach 1 during volatility explosions.

**Technical formula:**

1. JVOLTYₜ from original algorithm  
2. JVOLTYNₜ = 1 ⁄ (1 + e^{−k·(JVOLTYₜ − 1)})    ; *k* = Sigmoid Strength

> 🔍 **Technical Note:** Centering the logistic at JVOLTY = 1 ensures a 0.5 neutral line; choosing *k* ≈ 2 maps JVOLTY ≈ 1.5 to JVOLTYN ≈ 0.73.

## Interpretation Details

* **> 0.8** — extreme volatility; trend followers thrive, tighten risk controls  
* **0.5 zone** — average energy; standard strategies  
* **< 0.2** — volatility drought; expect range‑bound price, favor options selling or stay flat

## Limitations and Considerations

* **Inherited opacity:** depends on JVOLTY internals  
* **Parameter over‑tuning:** extreme sigmoid strength can flatten mid‑range sensitivity  
* **Normalization illusion:** 0.9 on one asset may reflect different absolute ATR than another; still confirm with dollars‑at‑risk.

Complementary tools: ATRP for percent volatility, Bollinger Band %‑b, ADX.

## References

1. Jurik, M. “Normalized Volatility Techniques.” Jurik Research Notes, 1999.  
2. Sheldon, N. *Volatility Modeling in Intraday Trading*. Wiley, 2014.
