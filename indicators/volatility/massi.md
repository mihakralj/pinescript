# MASSI: Mass Index

[Pine Script Implementation of MASSI](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/massi.pine)

## Overview and Purpose

The Mass Index was developed by Donald Dorsey and introduced in the early 1990s as a method to identify potential trend reversals by analyzing the narrowing and widening of the trading range between high and low prices. Unlike most volatility indicators that measure the magnitude of price movement, the Mass Index focuses on the *compression* and *expansion* of the range itself. The indicator is based on the premise that significant trend reversals are often preceded by a "reversal bulge" — a period where the range narrows (indicated by the EMA ratio approaching 1.0) followed by a widening.

The Mass Index operates independently of price direction, making it equally effective for identifying both bullish and bearish reversals. By using a double exponential smoothing technique and summing the ratio of these smoothed values, the indicator effectively highlights periods when the market's trading range undergoes significant structural changes. This range-compression pattern often signals exhaustion in the current trend and potential reversal setup.

## Core Concepts

* **Range analysis focus** — examines the high-low range rather than closing prices or returns
* **Double EMA ratio** — compares single-smoothed to double-smoothed ranges to detect compression
* **Summation period** — aggregates the ratio over 25 periods to identify reversal bulges
* **Direction-neutral** — signals potential reversals regardless of trend direction
* **Reversal bulge pattern** — looks for values exceeding 27 followed by a drop below 26.5

Market application:

* **Reversal prediction** — identifies potential trend exhaustion and reversal setups
* **Risk management** — warns of increased reversal probability in trending positions
* **Entry timing** — provides advance notice of potential turning points
* **Confirmation tool** — validates other reversal signals from price action or oscillators

Timeframe suitability:

* **Daily to weekly** — most effective on higher timeframes where reversals are more significant
* **Intraday (≥ 1 hour)** — can be used on lower timeframes with adjusted parameters

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| EMA Length | 9 | Smoothing period for high-low range | Shorten for more sensitivity; lengthen for fewer but more reliable signals |
| Sum Length | 25 | Period for summing the EMA ratio | Rarely adjusted; 25 periods captures the reversal bulge effectively |
| Reversal Signal | 27.0 | Upper threshold for potential reversal setup | Can be adjusted based on market characteristics |
| Setup Line | 26.5 | Lower threshold confirming reversal signal | Typically kept 0.5 below reversal signal |

**Pro Tip:** The classic reversal signal occurs when the Mass Index rises above 27.0 and then falls back below 26.5. This "bulge" pattern indicates range compression followed by expansion, often preceding significant reversals. Wait for the drop below 26.5 rather than trading on the initial spike above 27.

## Calculation and Mathematical Foundation

**Simplified explanation:**  
Calculate the EMA of the high-low range, then calculate another EMA of that result. Divide the first EMA by the second EMA to get a ratio, and sum this ratio over 25 periods. When the range compresses, the ratio approaches 1.0, and the Mass Index rises above 27, signaling a potential reversal setup.

**Technical formula:**

1. Calculate high-low range:
   Range = High − Low

2. Calculate first EMA (single-smoothed):
   EMA₁ = EMA(Range, 9)

3. Calculate second EMA (double-smoothed):
   EMA₂ = EMA(EMA₁, 9)

4. Calculate the ratio:
   Ratio = EMA₁ / EMA₂

5. Sum the ratio over 25 periods:
   MASSI = Σ(Ratio, 25)

where the EMA uses the standard exponential smoothing formula with α = 2/(n+1).

> 🔍 **Technical Note:** The implementation uses an efficient circular buffer to maintain the 25-period sum, avoiding repeated summation calculations. The ratio EMA₁/EMA₂ approaches 1.0 when the range is compressing (indicating narrowing volatility), causing the Mass Index to rise as these near-unity values accumulate.

## Interpretation Details

* **Rising above 27.0** → potential reversal setup initiated; range compression occurring
* **Falling below 26.5 (after crossing 27.0)** → reversal signal confirmed; range expansion beginning
* **Values between 26.5-27.0** → neutral zone; no actionable signal
* **Prolonged elevation above 27** → extended range compression; strong reversal potential building
* **Multiple bulges** → indicates choppy, range-bound conditions; use with caution
* **Divergence with price** → when MASSI signals reversal but price continues trending, exercise caution

**Trading Rules:**
1. Wait for Mass Index to rise above 27.0 (setup)
2. Watch for subsequent drop below 26.5 (trigger)
3. Look for confirming price action (support/resistance breaks, candlestick patterns)
4. Direction of reversal determined by other indicators or price structure
5. Exit when Mass Index returns to normal levels or price confirms trend continuation

## Limitations and Considerations

* **No directional bias** — does not indicate whether reversal will be bullish or bearish
* **False signals** — can generate signals during ranging markets without meaningful reversals
* **Requires confirmation** — should be used with trend indicators, support/resistance, or price patterns
* **Lag component** — double EMA smoothing introduces delay in signal generation
* **Fixed thresholds** — 27/26.5 levels may not be optimal for all markets or timeframes
* **Infrequent signals** — relatively rare occurrence of true reversal bulges
* **Market-dependent** — works better in trending markets than in sustained range-bound conditions
* **Parameter sensitivity** — EMA length significantly affects signal frequency and reliability

Complementary tools: RSI or Stochastic (for overbought/oversold confirmation), trend lines or moving averages (for reversal direction), volume indicators (for reversal validation).

## References

1. Dorsey, D. (1992). "The Mass Index." *Technical Analysis of Stocks & Commodities*, Volume 10.
2. Achelis, S. B. (2001). *Technical Analysis from A to Z* (2nd ed.). McGraw-Hill.
3. Pring, M. J. (2002). *Technical Analysis Explained* (4th ed.). McGraw-Hill.
4. Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
