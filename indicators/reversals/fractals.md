# FRACTALS: Williams Fractals

[Pine Script Implementation of FRACTALS](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/fractals.pine)

## Overview and Purpose

Williams Fractals are a reversal pattern identification tool developed by Bill Williams as part of his trading system. A fractal is a recurring pattern in price action that signals potential reversal points. The pattern identifies local peaks and troughs in price movement, helping traders spot potential support and resistance levels.

Introduced in Williams' book "Trading Chaos" (1995), fractals are based on the concept that markets are fractal in nature - patterns repeat at different scales. The fractal pattern is simple yet powerful: it requires a specific configuration of five consecutive bars where the middle bar represents a local extreme (high or low).

Williams Fractals are fundamental components of the Alligator trading system and are widely used in conjunction with other Williams indicators to identify high-probability trade setups. They provide clear, objective markers for potential market turning points.

## Core Concepts

* **Up Fractal (Bearish):** Five-bar pattern where the middle bar's high is greater than the two bars before and two bars after it
* **Down Fractal (Bullish):** Five-bar pattern where the middle bar's low is less than the two bars before and two bars after it
* **Confirmation Lag:** Fractals are confirmed two bars after they occur (need to see two bars ahead to validate the pattern)
* **Support/Resistance:** Fractals often mark key support (down fractals) and resistance (up fractals) levels
* **Trend Structure:** Series of higher fractals indicate uptrend; series of lower fractals indicate downtrend

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Show Up Fractals | true | Display bearish fractals (resistance) | Toggle based on trading strategy focus |
| Show Down Fractals | true | Display bullish fractals (support) | Toggle based on trading strategy focus |
| Up Fractal Color | Red | Color for resistance markers | Customize for visual preference |
| Down Fractal Color | Green | Color for support markers | Customize for visual preference |

**Pro Tip:** Williams Fractals work best when combined with other Williams indicators like the Alligator. Trade only in the direction of the Alligator (trend), using fractals as entry points. Fractals against the trend are typically used as profit-taking levels rather than entry signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Williams Fractals identify local extremes in price action using a simple five-bar pattern comparison.

**Technical formula:**

**Up Fractal (Bearish Reversal):**
```
high[2] > high[4] AND
high[2] > high[3] AND
high[2] > high[1] AND
high[2] > high[0]
```
Where bar[2] is the center bar (the potential fractal point).

**Down Fractal (Bullish Reversal):**
```
low[2] < low[4] AND
low[2] < low[3] AND
low[2] < low[1] AND
low[2] < low[0]
```

> 🔍 **Technical Note:** The original Williams Fractal uses strict inequality (> or <), meaning the center bar must be distinctly higher/lower than surrounding bars. If multiple bars have the same high/low, they don't form a valid fractal. The pattern is confirmed two bars after the center bar, creating a 2-bar lag in detection.

## Interpretation Details

Williams Fractals provide multiple analytical perspectives:

* **Support and Resistance:**
  - Up fractals mark resistance levels where price may encounter selling pressure
  - Down fractals mark support levels where price may find buying interest
  - These levels remain relevant until broken or replaced by new fractals

* **Trend Identification:**
  - Series of higher up fractals + higher down fractals = uptrend
  - Series of lower up fractals + lower down fractals = downtrend
  - Break of fractal level signals potential trend change

* **Entry Signals (Williams System):**
  - Buy when price breaks above up fractal in an uptrend (breakout entry)
  - Sell when price breaks below down fractal in a downtrend (breakdown entry)
  - Use fractals against trend as profit targets, not entries

* **Stop Loss Placement:**
  - For long positions: place stop below recent down fractal
  - For short positions: place stop above recent up fractal
  - Fractals provide natural stop loss levels based on market structure

* **Market Structure:**
  - Fractals reveal the "skeleton" of price movement
  - Help identify swing highs and swing lows
  - Show where market participants made decisions to reverse direction

## Limitations and Considerations

* **Confirmation Lag:** Fractals are confirmed two bars after they occur, creating inherent lag in signal generation
* **False Signals:** Not all fractals lead to significant reversals; many are minor retracements within larger trends
* **No Direction Bias:** Fractals appear in both trends and ranging markets without indicating which direction to trade
* **Frequency Variation:** Number of fractals varies by market volatility and timeframe; ranging markets produce more fractals
* **Require Confirmation:** Best used with trend-following indicators rather than as standalone signals
* **Subjective Application:** Rules for trading fractal breaks vary among practitioners

## References

* Williams, B. (1995). Trading Chaos: Maximize Profits with Proven Technical Techniques. John Wiley & Sons.
* Williams, B. (2004). Trading Chaos, 2nd Edition: A New Map for Traders. John Wiley & Sons.
* Williams, J. (2011). Trading Chaos: Apply the Fractal Geometry of Financial Markets. Wiley Trading.
