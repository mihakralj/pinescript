# ABBER: Aberration

[Pine Script Implementation of ABBER](https://github.com/mihakralj/pinescript/blob/main/indicators/channels/abber.pine)

## Overview and Purpose

ABBER (Aberration) is a channel indicator that measures the deviation of price from a central moving average, creating dynamic bands that adapt to market volatility. Unlike standard deviation-based indicators like Bollinger Bands, ABBER uses the average absolute deviation from the moving average, providing a more intuitive and robust measure of price dispersion that is less sensitive to extreme outliers.

The indicator creates upper and lower bands by adding and subtracting a multiple of the average deviation from the central moving average. This approach provides a cleaner representation of normal price behavior around the trend line, making it particularly effective for identifying overbought/oversold conditions and potential reversal points.

## Core Concepts

* **Absolute deviation measurement:** Uses the absolute difference between price and moving average rather than squared differences
* **Modular design:** Moving average is calculated externally and passed to the ABBER function
* **Outlier resistance:** Less sensitive to extreme price movements compared to standard deviation methods
* **Dynamic adaptation:** Bands automatically adjust to changing market volatility conditions
* **Simplicity and clarity:** Provides intuitive visual representation of price dispersion
* **Data robustness:** Uses nz() functions for proper handling of null/NA values

The key advantage of ABBER is its robustness against outliers and its intuitive interpretation - the bands represent the typical range of price movement around the central trend line.

## ABBER Function Parameters

| Parameter | Type | Function | Validation |
|-----------|------|----------|------------|
| source | series float | Price data to calculate aberration from | Any price series (close, hl2, hlc3, etc.) |
| ma_line | series float | Pre-calculated moving average line | Must be calculated externally |
| period | simple int | Lookback period for deviation calculation | Must be > 0 |
| multiplier | simple float | Multiplier for deviation bands | Must be > 0.0 |

**Returns:** `[upper_band, lower_band, avg_deviation]`

## Indicator Input Settings

The main indicator provides these user inputs:

| Input | Default | Options | Purpose |
|-------|---------|---------|---------|
| Source | close | Any price series | Price data for calculations |
| Period | 20 | Integer ≥ 1 | Lookback period for deviation |
| Moving Average Type | "SMA" | SMA, EMA, WMA, RMA, HMA | Type of MA calculated externally |
| Deviation Multiplier | 2.0 | Float ≥ 0.1 | Band distance multiplier |
| Show Moving Average Line | true | true/false | Display central MA line |

## Calculation and Mathematical Foundation

**Simplified explanation:**
ABBER takes a pre-calculated moving average as input, then measures how far price typically deviates from this average. This modular design allows for maximum flexibility in moving average selection. The bands are plotted at a multiple of this typical deviation distance above and below the moving average.

**Technical formula:**
1. MA = Pre-calculated moving average (external calculation)
2. Deviation = |Source - MA| (absolute difference)
3. Average Deviation = Simple Moving Average of Deviation over period
4. Upper Band = MA + (Multiplier × Average Deviation)
5. Lower Band = MA - (Multiplier × Average Deviation)

**Detailed calculation steps:**
1. Calculate the desired moving average externally using any method (SMA, EMA, custom MA, etc.)
2. Pass the pre-calculated MA line to the ABBER function along with the source price
3. For each bar, compute the absolute deviation: |source - MA| using nz() for null handling
4. Calculate the simple moving average of these absolute deviations over the specified period
5. Multiply the average deviation by the specified multiplier
6. Add/subtract this value from the MA to create upper/lower bands

> 🔍 **Technical Note:** Using absolute deviation instead of standard deviation makes ABBER more robust to outliers and provides a more intuitive measure of typical price dispersion. The function includes input validation and uses nz() for proper null value handling.

## Visual Elements

* **Central MA Line:** Yellow line (width 2) representing the moving average - can be toggled on/off
* **Aberration Bands:** Blue lines (width 1) showing the upper and lower deviation boundaries
* **Fill Area:** Semi-transparent blue fill between the bands for easy visual identification
* **Clean Design:** No information tables or overlays, focusing on essential band structure

## Interpretation Details

ABBER provides multiple layers of market analysis:

* **Central Line Analysis:**
  - Price above MA: Bullish bias, upward momentum
  - Price below MA: Bearish bias, downward momentum
  - Price oscillating around MA: Balanced market, consolidation phase

* **Band Interaction Signals:**
  - Price touching upper band: Potential resistance, overbought condition
  - Price touching lower band: Potential support, oversold condition
  - Price between bands: Normal market behavior
  - Price outside bands: Extreme conditions, potential reversal opportunity

* **Band Width Analysis:**
  - Expanding bands: Increasing volatility, larger price movements expected
  - Contracting bands: Decreasing volatility, potential breakout setup
  - Stable band width: Consistent volatility environment

## Trading Applications

**Mean Reversion Strategy:**
- Buy when price touches or exceeds the lower band
- Sell when price reaches the upper band or central MA
- Use stops beyond the bands to account for extended moves
- Target the opposite band or central line for profit-taking

**Trend Following Strategy:**
- Enter long positions when price breaks above upper band with momentum
- Enter short positions when price breaks below lower band with momentum
- Use the central MA as a dynamic support/resistance level
- Trail stops using the bands or central line

**Volatility Breakout Strategy:**
- Monitor periods of contracting bands for potential breakouts
- Enter positions on confirmed breaks beyond the bands
- Use band width as a volatility filter for trade selection
- Avoid trading during extremely low volatility periods

**Moving Average Experimentation:**
- Test different MA types (SMA, EMA, WMA, RMA, HMA) for varying responsiveness
- Use EMA-based ABBER for faster signals, SMA for stability
- Apply HMA-based ABBER for reduced lag in trend identification

## Signal Combinations

**High-Probability Long Signals:**
- Price bounces off lower ABBER band with volume confirmation
- Price reclaims central MA after period below with strong momentum
- ABBER and Bollinger Band lower bands align as support
- RSI oversold condition coincides with lower band touch

**High-Probability Short Signals:**
- Price fails at upper ABBER band with declining volume
- Price breaks below central MA after period above with conviction
- ABBER and Bollinger Band upper bands align as resistance
- RSI overbought condition coincides with upper band touch

**Breakout Confirmation:**
- Band width contraction followed by expansion
- Price closes beyond bands with increased volume
- Multiple timeframe band alignment supporting direction
- Momentum indicators confirming the breakout direction

## Advanced Techniques

**Multi-Moving Average Analysis:**
- Compare ABBER bands using different MA types (SMA vs EMA vs HMA)
- Use EMA-based ABBER for faster signals, SMA for stability
- Apply HMA-based ABBER for reduced lag in trend identification
- Look for convergence between different MA-based band systems

**Volatility Regime Analysis:**
- Use band width as a volatility filter for strategy selection
- Apply mean reversion strategies during low volatility (narrow bands)
- Use breakout strategies during high volatility (wide bands)
- Monitor volatility transitions for strategy adjustments

**Multi-Timeframe Integration:**
- Use higher timeframe ABBER for major support/resistance levels
- Combine daily ABBER with intraday bands for precision timing
- Look for confluence between different timeframe band levels
- Scale position sizes based on multi-timeframe band alignment

## Limitations and Considerations

* **Lagging indicator:** Based on moving averages, creating inherent lag in signals
* **False signals:** Can generate whipsaws in choppy, trendless markets
* **Parameter sensitivity:** Performance varies significantly with period and multiplier settings
* **Market regime dependency:** More effective in trending markets than ranging conditions
* **No directional bias:** Provides levels but not trend direction confirmation
* **Requires confirmation:** Best used with momentum or volume indicators for validation

## Comparison with Related Indicators

**ABBER vs. Bollinger Bands:**
- ABBER: Uses average absolute deviation, less sensitive to outliers
- Bollinger Bands: Uses standard deviation, more statistically rigorous

**ABBER vs. Keltner Channels:**
- ABBER: Deviation-based bands with flexible MA center
- Keltner Channels: ATR-based bands with EMA center

**ABBER vs. Moving Average Envelopes:**
- ABBER: Dynamic bands based on actual price behavior
- MA Envelopes: Fixed percentage bands regardless of volatility

**ABBER vs. ATR Bands:**
- ABBER: Measures deviation from trend line
- ATR Bands: Measures absolute volatility range

## Best Practices

**Parameter Optimization:**
- Start with standard settings (20-period, 2.0 multiplier) and adjust based on results
- Use shorter periods for more responsive signals in fast markets
- Increase multiplier for volatile assets, decrease for stable instruments
- Test different MA types to match the asset's characteristics

**Risk Management:**
- Use bands for position sizing (larger positions near support bands)
- Set stops beyond the bands rather than at exact band levels
- Watch for extreme price movements beyond the bands
- Avoid trading during periods of extremely narrow bands

**Market Context:**
- Consider overall market trend when interpreting band signals
- Use volume confirmation for band interaction signals
- Account for fundamental events that may cause sustained moves beyond bands
- Adjust expectations based on current volatility regime

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. Trend Research.
* Bollinger, J. (2001). Bollinger on Bollinger Bands. McGraw-Hill.
