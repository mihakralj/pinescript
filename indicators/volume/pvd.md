# PVD: Price Volume Divergence

[Pine Script Implementation of PVD](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/pvd.pine)

## Overview and Purpose

Price Volume Divergence (PVD) is a systematic indicator designed to automatically detect and quantify divergences between price movements and volume activity. Unlike traditional volume indicators that focus on absolute volume levels, PVD specifically identifies instances where price action contradicts volume patterns, providing early warning signals for potential trend reversals or continuation failures.

The indicator works by comparing the directional momentum of price with the directional momentum of volume over specified periods, creating a divergence score that highlights when these two critical market forces move in opposite directions. This systematic approach removes the subjectivity from divergence analysis and provides quantifiable signals for traders.

## Core Concepts

* **Systematic divergence detection**: Automated identification of price-volume disconnects
* **Momentum comparison**: Analyzes rate of change in both price and volume
* **Quantified signals**: Numerical divergence scores rather than visual interpretation
* **Multi-timeframe analysis**: Configurable periods for different trading strategies
* **Early warning system**: Identifies potential reversals before they become obvious

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Price Period | 14 | Lookback period for price momentum calculation | Shorter periods (5-10) for sensitive signals, longer (20-30) for major trends |
| Volume Period | 14 | Lookback period for volume momentum calculation | Can differ from price period to detect varying timeframe divergences |
| Divergence Threshold | 50 | Minimum divergence score to trigger signals | Lower values (20-40) for more signals, higher (60-80) for stronger signals only |
| Smoothing Period | 3 | Period for smoothing divergence signals | Reduce noise with higher values, increase responsiveness with lower |

**Pro Tip:** Use different price and volume periods to detect divergences across multiple timeframes. For example, 10-period price with 20-period volume can reveal short-term price moves unsupported by underlying volume trends.

## Calculation and Mathematical Foundation

**Simplified explanation:**
PVD calculates the rate of change for both price and volume over specified periods, then compares their directions and magnitudes. When price momentum is positive but volume momentum is negative (or vice versa), a divergence signal is generated with intensity based on the degree of opposition.

**Technical formula:**
```
Price_ROC = (Close - Close[price_period]) / Close[price_period] * 100
Volume_ROC = (Volume - Volume[volume_period]) / Volume[volume_period] * 100

Price_Momentum = Price_ROC > 0 ? 1 : Price_ROC < 0 ? -1 : 0
Volume_Momentum = Volume_ROC > 0 ? 1 : Volume_ROC < 0 ? -1 : 0

Divergence_Raw = Price_Momentum * -Volume_Momentum * (abs(Price_ROC) + abs(Volume_ROC))
PVD = SMA(Divergence_Raw, smoothing_period)

Signal_Strength = abs(PVD)
Bullish_Divergence = PVD > threshold (price down, volume up)
Bearish_Divergence = PVD < -threshold (price up, volume down)
```

**Implementation considerations:**
- Rate of change calculations use percentage change to normalize different scales
- Momentum direction is simplified to -1, 0, or 1 for clear comparison
- Signal strength incorporates both direction opposition and magnitude
- Smoothing reduces noise while maintaining signal integrity

> 🔍 **Technical Note:** The divergence calculation multiplies price momentum by negative volume momentum, creating positive values when they oppose each other. The magnitude component ensures stronger moves generate stronger signals.

## Interpretation Details

PVD provides multiple analytical perspectives:

* **Positive PVD Values (Bullish Divergence):**
  - Price declining while volume increasing
  - Suggests accumulation during price weakness
  - Potential bullish reversal signal
  - Stronger values indicate higher probability

* **Negative PVD Values (Bearish Divergence):**
  - Price rising while volume declining
  - Suggests distribution during price strength
  - Potential bearish reversal signal
  - More negative values indicate stronger warning

* **PVD Signal Strength:**
  - **Above threshold**: Significant divergence worthy of attention
  - **High magnitude**: Strong opposing forces, higher reversal probability
  - **Sustained signals**: Multi-period divergences more reliable than single spikes
  - **Zero line**: No divergence, price and volume in harmony

* **PVD Patterns:**
  - **Increasing divergence**: Building opposition between price and volume
  - **Decreasing divergence**: Forces coming back into alignment
  - **Oscillating signals**: Conflicting short-term vs. longer-term trends

## Trading Applications

**Primary Uses:**
- **Reversal warning system**: Early detection of potential trend changes
- **Trend strength assessment**: Identify when trends lack volume support
- **Entry timing**: Use divergence signals to time position entries
- **Risk management**: Exit positions when divergences suggest trend weakness

**Advanced Strategies:**
- **Divergence confirmation**: Wait for price confirmation before acting on signals
- **Multiple timeframe analysis**: Compare divergences across different periods
- **Volume quality assessment**: Distinguish between meaningful and noise volume
- **Pattern validation**: Use PVD to confirm or reject chart pattern signals

## Signal Combinations

**Strong Bullish Signals:**
- High positive PVD + price at support level
- Sustained bullish divergence + oversold momentum indicators
- Volume spike during price decline + positive PVD confirmation

**Strong Bearish Signals:**
- High negative PVD + price at resistance level
- Sustained bearish divergence + overbought momentum indicators
- Volume decline during price rally + negative PVD confirmation

**Warning Signals:**
- Oscillating PVD without clear direction (conflicting timeframes)
- Low magnitude signals (may be noise rather than meaningful divergence)
- Divergence without price pattern confirmation

## Comparison with Manual Divergence Analysis

| Aspect | PVD (Systematic) | Manual Analysis |
|--------|------------------|-----------------|
| **Objectivity** | Quantified, rules-based | Subjective interpretation |
| **Speed** | Instant calculation | Time-consuming visual analysis |
| **Consistency** | Same criteria always applied | Varies by analyst experience |
| **Sensitivity** | Adjustable through parameters | Fixed by visual perception |
| **Backtesting** | Easily tested and optimized | Difficult to backtest systematically |
| **False Signals** | Quantifiable and filterable | Hard to measure objectively |

## Limitations and Considerations

* **Parameter sensitivity:** Results can vary significantly with different settings
* **Market context:** Divergences mean different things in trending vs. ranging markets
* **Volume quality:** Requires clean, reliable volume data for accurate signals
* **False signals:** Not all divergences lead to reversals; confirmation needed
* **Lag consideration:** Uses historical data, signals may come after optimal entry
* **Market hours:** Extended trading sessions can distort volume comparisons

## Advanced Configurations

**Sensitive Setup (Short-term trading):**
- Price Period: 7, Volume Period: 7, Threshold: 30, Smoothing: 2

**Standard Setup (Swing trading):**
- Price Period: 14, Volume Period: 14, Threshold: 50, Smoothing: 3

**Conservative Setup (Position trading):**
- Price Period: 21, Volume Period: 21, Threshold: 70, Smoothing: 5

**Cross-timeframe Setup:**
- Price Period: 10, Volume Period: 20, Threshold: 40, Smoothing: 3

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Elder, Alexander (1993). Trading for a Living. John Wiley & Sons.
* Schwager, J. D. (1996). Technical Analysis. John Wiley & Sons.
* Pring, Martin J. (2002). Technical Analysis Explained. McGraw-Hill.
* Achelis, Steven B. (2000). Technical Analysis from A to Z. McGraw-Hill.
