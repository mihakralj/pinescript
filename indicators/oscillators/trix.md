# TRIX: Triple Exponential Average

[Pine Script Implementation of TRIX](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/trix.pine)

## Overview and Purpose

TRIX (Triple Exponential Average) is a momentum oscillator developed by Jack Hutson that measures the percentage rate of change of a triple exponentially smoothed moving average. By applying exponential smoothing three times, TRIX filters out short-term price fluctuations and noise, focusing on significant trend changes and momentum shifts.

The indicator oscillates around zero, where positive values indicate upward momentum and negative values indicate downward momentum. TRIX is particularly effective at identifying trend reversals and generating trading signals with minimal false signals due to its extensive smoothing process.

## Core Concepts

* **Triple smoothing process:** Applies exponential moving average three consecutive times to eliminate noise
* **Rate of change measurement:** Calculates percentage change of the smoothed average to show momentum
* **Zero-line oscillator:** Values above zero indicate bullish momentum, below zero indicate bearish momentum
* **Lag reduction compensation:** Despite triple smoothing, maintains reasonable responsiveness to significant changes
* **Signal line analysis:** Often used with a signal line (EMA of TRIX) for crossover signals

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Period for triple exponential smoothing | Lower (8-12) for more sensitivity, higher (18-25) for smoother signals |
| Signal Period | 9 | Period for signal line (EMA of TRIX) | Adjust based on desired signal timing |
| Source | Close | Price series to analyze | Use HLOC4 for additional smoothing, high/low for range analysis |

**Pro Tip:** The classic 14-period setting works well for medium-term analysis, but consider shorter periods (8-10) for day trading or longer periods (21-28) for position trading to match your time horizon.

## Calculation and Mathematical Foundation

**Simplified explanation:**
TRIX applies exponential smoothing three times to the price data, then calculates the percentage rate of change of this triple-smoothed series. This process removes short-term noise while preserving longer-term momentum information.

**Technical formula:**
```
EMA1 = EMA(Price, Period)
EMA2 = EMA(EMA1, Period)
EMA3 = EMA(EMA2, Period)
TRIX = 100 × (EMA3 - EMA3[1]) / EMA3[1]
```

Where:
- EMA1 = First exponential moving average
- EMA2 = Second exponential moving average (smoothing of EMA1)
- EMA3 = Third exponential moving average (smoothing of EMA2)
- TRIX = Percentage rate of change of EMA3

**Signal line calculation:**
```
Signal Line = EMA(TRIX, Signal Period)
```

> 🔍 **Technical Note:** The implementation uses optimized exponential smoothing with proper initialization to ensure accurate results from the first bar. The triple smoothing process significantly reduces noise while the rate of change calculation converts the trend into momentum readings.

## Interpretation Details

TRIX provides several analytical perspectives:

* **Zero-line analysis:** Positive TRIX values suggest bullish momentum, negative values suggest bearish momentum
* **Signal line crossovers:** TRIX crossing above its signal line generates bullish signals, crossing below generates bearish signals
* **Divergence analysis:** Divergences between TRIX and price often precede significant reversals
* **Momentum direction:** Rising TRIX indicates strengthening momentum, falling TRIX indicates weakening momentum
* **Trend confirmation:** TRIX direction can confirm or question the sustainability of price trends
* **Overbought/oversold levels:** Extreme TRIX readings may indicate potential reversal points

## Trading Applications

**Primary Uses:**
- **Trend reversal identification:** Detect momentum shifts that precede price reversals
- **Signal line crossovers:** Generate buy/sell signals with TRIX-signal line intersections
- **Momentum confirmation:** Validate breakouts and trend continuations
- **Divergence trading:** Identify momentum divergences for reversal opportunities

**Advanced Strategies:**
- **Zero-line trading:** Trade TRIX crossovers above and below zero for trend following
- **Multiple timeframe analysis:** Use different periods to capture various momentum cycles
- **Momentum filtering:** Use TRIX to filter other trading signals and reduce false entries
- **Trend strength assessment:** Evaluate the sustainability of current price movements

## Signal Combinations

**Strong Bullish Signals:**
- TRIX crosses above zero from negative territory
- TRIX crosses above its signal line while both are rising
- Positive divergence: TRIX makes higher lows while price makes lower lows

**Strong Bearish Signals:**
- TRIX crosses below zero from positive territory
- TRIX crosses below its signal line while both are falling
- Negative divergence: TRIX makes lower highs while price makes higher highs

**Trend Continuation Signals:**
- TRIX remains above zero with occasional pullbacks that don't cross below zero
- TRIX signal line acts as dynamic support/resistance during trends
- TRIX maintains directional bias consistent with the underlying trend

## Comparison with Related Oscillators

| Indicator | Smoothing | Scale | Best Use Case |
|-----------|-----------|-------|---------------|
| **TRIX** | Triple EMA | Centered on zero | Trend reversal, low noise |
| **MACD** | Double EMA | Centered on zero | Momentum, faster signals |
| **PPO** | Double EMA | Percentage scale | Relative momentum |
| **ROC** | None | Percentage scale | Raw momentum |

**Advantages over MACD:**
- Less noise due to triple smoothing
- Fewer false signals in choppy markets
- Better for longer-term trend analysis

**Disadvantages compared to MACD:**
- More lag due to additional smoothing
- May miss short-term momentum shifts
- Requires more data for accurate signals

## Advanced Configurations

**Short-term Trading Setup:**
- Period: 8, Signal: 5, Source: Close

**Standard Medium-term:**
- Period: 14, Signal: 9, Source: Close

**Long-term Position Trading:**
- Period: 21, Signal: 13, Source: HLOC4

**Ultra-smooth Configuration:**
- Period: 28, Signal: 15, Source: HLOC4

## Market-Specific Adjustments

**Volatile Markets:**
- Use longer periods (18-25) to reduce noise
- Focus on zero-line crossovers rather than signal line crossovers
- Require stronger momentum confirmation before acting

**Trending Markets:**
- Use standard settings (14/9) for good balance
- Focus on signal line as dynamic support/resistance
- Look for trend continuation patterns rather than reversals

**Range-Bound Markets:**
- Use shorter periods (8-12) to capture range reversals
- Trade TRIX extremes rather than crossovers
- Combine with support/resistance levels for confirmation

## Limitations and Considerations

* **Lag factor:** Triple smoothing creates significant lag, may miss quick reversals
* **Whipsaw potential:** Can generate false signals during transitional market phases
* **Period dependency:** Performance varies significantly with different period settings
* **Trend bias:** Works best in trending markets, less effective in ranging conditions
* **Signal timing:** May enter trends late due to confirmation requirements

## Best Practices

**Effective Usage:**
- Combine with trend analysis to avoid counter-trend trades
- Use multiple timeframes to confirm signals across different horizons
- Focus on divergences for higher-probability reversal opportunities
- Wait for clear momentum confirmation before entering positions

**Common Mistakes:**
- Acting on every signal line crossover without trend context
- Using inappropriate periods for the trading timeframe
- Ignoring the underlying trend when interpreting TRIX signals
- Expecting immediate price action after TRIX signals due to inherent lag

**Signal Enhancement:**
- Combine with volume analysis for momentum confirmation
- Use price action context (support/resistance) for entry timing
- Consider multiple oscillator confirmation for higher-probability trades
- Adjust periods based on current market volatility and trend characteristics

## Historical Context and Development

TRIX was developed by Jack Hutson and published in Technical Analysis of Stocks & Commodities magazine. Hutson designed the indicator to:

- Filter out market noise through extensive smoothing
- Provide cleaner momentum signals with fewer false positives
- Create a trend-following momentum oscillator suitable for longer-term analysis
- Offer an alternative to MACD with reduced whipsaw potential

The indicator gained popularity among traders seeking a smoother momentum oscillator that could identify significant trend changes while filtering out short-term price noise. It remains particularly valuable for swing traders and position traders who prefer fewer, higher-quality signals over frequent trading opportunities.

## References

* Hutson, J. (1983). "TRIX - Triple Exponential Smoothing Oscillator." Technical Analysis of Stocks & Commodities.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2001). Technical Analysis from A to Z (2nd ed.). McGraw-Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Pring, M. J. (2002). Technical Analysis Explained (4th ed.). McGraw-Hill.
