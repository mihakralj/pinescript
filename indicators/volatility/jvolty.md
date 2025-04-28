# JVOLTY: Jurik Volatility

[Pine Script Implementation of JVOLTY](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/jvolty.pine)

## Overview and Purpose

Jurik Volatility (JVOLTY) adapts Mark Jurik’s proprietary smoothing techniques to generate a fast yet low‑noise volatility gauge. By expanding and contracting adaptive envelopes around price, it extracts instantaneous volatility while filtering market micro‑structure noise. JVOLTY is favored for scalping systems, dynamic band construction, and volatility‑conditioned position sizing across all markets.

## Core Concepts

* **Adaptive envelope spread** — measures max deviation of price from rolling bands to capture bar‑level volatility  
* **Jurik smoothing** — non‑linear filter provides lag‑minimized noise suppression  
* **Relative scaling** — current spread divided by smoothed average reveals volatility spikes

Market application:  

* **Band trading:** drive adaptive Keltner/Jurik bands  
* **Vol filter:** disable signals when JVOLTY < threshold  
* **Risk model:** expand stop distance as JVOLTY rises

Timeframe suitability:  

* **Intraday (1 m – H1)** for high‑frequency context; works on daily charts for swing as well.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 10 | Look‑back for adaptive envelope & smoothing | Shorten for faster spikes, lengthen for stability |
| Source | Close | Price series for calculation | Use HL2 for range‑sensitive assets |
| Offset Divisor | 10 (implicit) | Determines decay of historical vol sum | Rarely changed; lower for more reactivity |

**Pro Tip:** Pair JVOLTY with a 50‑bar SMA of itself; trade breakouts only when JVOLTY exceeds 1.2 × its average to avoid low‑energy moves.

## Calculation and Mathematical Foundation

**Simplified explanation:**  
Compute the widest gap between price and adaptive upper/lower bands, smooth this volatility trace with Jurik’s filter, then express current spread as a ratio of its average.

**Technical formula (abridged):**

1. Kv = (LEN₂ / (LEN₂ + 1))^{√(rv^{POW₁})} with rv = vol / avgVol  
2. UpperBand = src − Kv·Δ₊ ; LowerBand = src − Kv·Δ₋  
3. JVOLTY = vol / avgVol , clipped to [1 , LEN₁^{1/POW₁}]

where LEN₁, LEN₂, POW₁ derive from `period` (see code); vol = max(|src−UB|, |src−LB|).

> 🔍 **Technical Note:** Jurik smoothing is similar to an EMA with dynamic α driven by volatility itself, yielding lower phase lag than standard filters of equal noise reduction.

## Interpretation Details

* **JVOLTY = 1** — volatility equals recent average; neutral backdrop  
* **JVOLTY > 1.5** — volatility surge; favor momentum tactics and wider stops  
* **JVOLTY falling toward 1** — compression phase; anticipate breakout after squeeze  
* **Persistent low JVOLTY (< 1.1)** — range trading conditions dominate

## Limitations and Considerations

* **Opacity of Jurik math:** proprietary filter parameters hinder strict replication  
* **Parameter sensitivity:** very small periods (< 5) can over‑fit noise  
* **High‑tick spreads:** illiquid symbols may distort adaptive bands

Complementary tools: Jurik Moving Average (JMA), ADX for trend strength, Bollinger Band Width.

## References

1. Jurik, M. “JMA and JMA‑Based Indicators.” Jurik Research, 1998.  
2. Harris, L. *Trading and Exchanges*, Oxford UP, 2003.
