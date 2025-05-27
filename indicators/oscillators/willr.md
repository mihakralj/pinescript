# WILLR: Williams %R

[Pine Script Implementation of WILLR](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/willr.pine)

## Overview and Purpose

Williams %R (WILLR) is a momentum oscillator developed by Larry Williams that measures the level of the close relative to the highest high for a specified period. Often referred to as the "inverse Fast Stochastic Oscillator," Williams %R identifies overbought and oversold levels in the market, making it particularly useful for timing entries and exits in trading strategies.

The indicator oscillates between -100 and 0, where readings above -20 are typically considered overbought and readings below -80 are considered oversold. Unlike many other oscillators, Williams %R uses a negative scale, with 0 representing the strongest possible reading (close equals the period high) and -100 representing the weakest reading (close equals the period low).

## Core Concepts

* **Inverse stochastic relationship:** Calculated as the inverse of the Fast Stochastic %K, providing a different perspective on price momentum
* **Overbought/oversold identification:** Clear levels at -20 (overbought) and -80 (oversold) for trading signals
* **High sensitivity:** Responds quickly to price changes, making it suitable for short-term trading
* **Mean reversion focus:** Designed to identify when prices may reverse from extreme levels
* **Negative scale interpretation:** Uses -100 to 0 scale where higher values (closer to 0) indicate stronger momentum

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Lookback period for high/low range calculation | Lower (5-10) for more sensitivity, higher (20-30) for smoother signals |
| Overbought Level | -20 | Upper threshold for overbought conditions | Adjust to -10 for more extreme signals, -30 for earlier warnings |
| Oversold Level | -80 | Lower threshold for oversold conditions | Adjust to -90 for more extreme signals, -70 for earlier warnings |

**Pro Tip:** The classic 14-period setting works well for most timeframes, but consider using shorter periods (7-10) for day trading or longer periods (21-28) for swing trading to match your trading style.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Williams %R compares the current close to the highest high over a specified period, expressing this as a percentage of the total range. It essentially asks: "Where is the close positioned within the recent high-low range?"

**Technical formula:**
```
Highest High = Highest high over the last N periods
Lowest Low = Lowest low over the last N periods
%R = -100 × (Highest High - Close) / (Highest High - Lowest Low)
```

Where:
- N = Period (typically 14)
- The negative sign ensures the scale runs from -100 to 0
- When Close = Highest High, %R = 0 (strongest)
- When Close = Lowest Low, %R = -100 (weakest)

**Alternative representation:**
```
%R = -100 + (100 × (Close - Lowest Low) / (Highest High - Lowest Low))
```

> 🔍 **Technical Note:** The implementation uses efficient min/max tracking algorithms to maintain O(1) time complexity per bar. The calculation properly handles edge cases where the high-low range equals zero by returning a neutral reading.

## Interpretation Details

Williams %R provides several analytical perspectives:

* **Overbought conditions:** Readings above -20 suggest the market may be overbought and due for a pullback
* **Oversold conditions:** Readings below -80 suggest the market may be oversold and due for a bounce
* **Momentum confirmation:** The direction of %R movement confirms or questions price momentum
* **Divergence analysis:** Divergences between %R and price often precede reversals
* **Range analysis:** Extended periods near extreme levels may indicate strong trends rather than reversal opportunities
* **Mean reversion signals:** Quick movements from extreme levels back toward the middle range often signal momentum shifts

## Trading Applications

**Primary Uses:**
- **Overbought/oversold trading:** Identify potential reversal points at extreme levels
- **Momentum confirmation:** Validate breakouts and trend continuations
- **Divergence analysis:** Spot momentum divergences that precede price reversals
- **Short-term timing:** Fine-tune entry and exit points for trades

**Advanced Strategies:**
- **Failure swings:** Trade when %R fails to exceed previous extreme levels
- **Multiple timeframe analysis:** Use different periods to capture various momentum cycles
- **Support/resistance confirmation:** Confirm price level breaks with momentum agreement
- **Trend strength assessment:** Evaluate the sustainability of current price movements

## Signal Combinations

**Strong Bullish Signals:**
- Williams %R rises from below -80 (oversold) back above -80
- %R shows positive divergence while price makes lower lows
- %R breaks above -50 after being oversold, confirming upward momentum

**Strong Bearish Signals:**
- Williams %R falls from above -20 (overbought) back below -20
- %R shows negative divergence while price makes higher highs
- %R breaks below -50 after being overbought, confirming downward momentum

**Caution Signals:**
- %R remains in extreme territory for extended periods (may indicate strong trend)
- Multiple false signals at the same level (may indicate ranging market)
- %R moves opposite to clear price direction (may signal momentum loss)

## Comparison with Related Oscillators

| Indicator | Scale | Calculation Focus | Best Use Case |
|-----------|-------|------------------|---------------|
| **Williams %R** | -100 to 0 | Close vs period high | Overbought/oversold timing |
| **Fast Stochastic %K** | 0 to 100 | Close vs period range | Momentum confirmation |
| **RSI** | 0 to 100 | Average gains vs losses | Trend strength |
| **Commodity Channel Index** | Unbounded | Deviation from mean | Cyclical analysis |

**Relationship to Stochastic:**
Williams %R = -100 + Fast Stochastic %K
This inverse relationship means when Fast Stochastic shows 80 (overbought), Williams %R shows -20 (overbought).

## Advanced Configurations

**Day Trading Setup:**
- Period: 7, Overbought: -15, Oversold: -85

**Standard Swing Trading:**
- Period: 14, Overbought: -20, Oversold: -80

**Conservative Long-Term:**
- Period: 21, Overbought: -30, Oversold: -70

**Scalping Setup:**
- Period: 5, Overbought: -10, Oversold: -90

## Market-Specific Adjustments

**Volatile Markets:**
- Use longer periods (21-28) to reduce false signals
- Consider more extreme thresholds (-10/-90) for signal quality
- Focus on divergences rather than absolute levels

**Trending Markets:**
- Be cautious of sustained readings in extreme territory
- Look for failure swings rather than simple reversals from extremes
- Use shorter periods to stay responsive to momentum changes

**Range-Bound Markets:**
- Standard settings (14-period, -20/-80) work well
- Trade reversals from extreme levels with tight stops
- Combine with support/resistance analysis for confirmation

## Limitations and Considerations

* **False signals in trends:** Can remain overbought/oversold for extended periods during strong trends
* **Whipsaw potential:** High sensitivity can generate multiple false signals in choppy markets
* **No directional bias:** Doesn't indicate the strength or sustainability of trends
* **Period dependency:** Performance varies significantly with different period settings
* **Extreme level interpretation:** Extreme readings may indicate trend strength rather than reversal opportunities

## Best Practices

**Effective Usage:**
- Combine with trend analysis to avoid counter-trend trades in strong markets
- Use multiple timeframes to confirm signals across different horizons
- Focus on divergences for higher-probability reversal signals
- Consider market context when interpreting extreme readings

**Common Mistakes:**
- Trading every overbought/oversold signal without trend context
- Using inappropriate periods for the trading timeframe
- Ignoring divergences in favor of absolute level readings
- Failing to adjust thresholds for different market volatility conditions

**Signal Enhancement:**
- Combine with volume analysis for confirmation
- Use price action context (support/resistance) for validation
- Consider multiple oscillator confirmation for higher-probability trades
- Adjust sensitivity based on current market volatility

## Historical Context and Development

Williams %R was developed by Larry Williams, a renowned trader and technical analyst, as part of his research into market timing and momentum analysis. Williams designed the indicator to:

- Provide a clear overbought/oversold framework for trading decisions
- Offer an alternative perspective to the popular Stochastic Oscillator
- Create a sensitive momentum tool suitable for short-term trading
- Simplify the interpretation of price momentum relative to recent ranges

The indicator gained popularity due to its simplicity, effectiveness in identifying short-term reversal opportunities, and Larry Williams' successful trading track record. It remains a standard tool in most technical analysis platforms and is widely used by both discretionary and systematic traders.

## References

* Williams, L. R. (1973). How I Made One Million Dollars... Last Year... Trading Commodities. Windsor Books.
* Williams, L. R. (1999). Long-Term Secrets to Short-Term Trading. Wiley Trading.
