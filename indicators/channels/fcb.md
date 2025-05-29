# FCB: Fractal Chaos Bands

[Pine Script Implementation of FCB](https://github.com/mihakralj/pinescript/blob/main/indicators/channels/fcb.pine)

## Overview and Purpose

FCB (Fractal Chaos Bands) is a channel indicator based on fractal geometry that captures market volatility and trends by identifying fractal highs and lows in price action. The indicator helps traders determine whether the market is trending or consolidating by analyzing the slope and behavior of the fractal-based bands.

When a market is trending, the FCB bands will exhibit a clear slope in the direction of the trend. During non-trending, choppy market conditions, the bands flatten out and compress. As the slope of the bands decreases, it signifies that the market is becoming more choppy, insecure, and variable. Conversely, as the bands develop a steeper slope, it indicates the market is becoming more trendy and stable.

## Core Concepts

* **Fractal geometry foundation:** Based on Bill Williams' fractal theory identifying turning points
* **Custom highest/lowest functions:** Uses optimized deque-based algorithms for performance
* **Trend identification:** Band slope indicates market trending vs. consolidation phases
* **Volatility measurement:** Band width reflects current market volatility levels
* **Support/resistance levels:** Bands act as dynamic support and resistance zones
* **Noise filtering:** Filters out insignificant price fluctuations by focusing on fractals
* **Market structure analysis:** Provides panoramic view of overall price movement patterns

The key advantage of FCB is its ability to distinguish between trending and non-trending market conditions while providing clear support and resistance levels based on fractal price structure.

## FCB Function Parameters

| Parameter | Type | Function | Validation |
|-----------|------|----------|------------|
| period | simple int | Lookback period for highest/lowest fractal calculation | Must be > 0 |

**Returns:** `[upper_band, lower_band]`

## Indicator Input Settings

| Input | Default | Options | Purpose |
|-------|---------|---------|---------|
| Period | 20 | Integer 1-999 | Lookback period for fractal band calculation |
| Show Fractal Points | false | true/false | Display fractal high/low markers (input only, not implemented in plots) |

## Calculation and Mathematical Foundation

**Simplified explanation:**
FCB identifies fractal highs and lows in price action, then tracks the highest fractal high and lowest fractal low over a specified period using custom optimized functions to create dynamic bands. The bands' slope and width indicate market trending behavior and volatility.

**Fractal identification:**
- **Fractal High:** `high[1] > high[2] AND high[1] > high[0]`
- **Fractal Low:** `low[1] < low[2] AND low[1] < low[0]`

**Technical formula:**
1. Identify fractal highs: center bar higher than 2 bars on each side
2. Identify fractal lows: center bar lower than 2 bars on each side
3. Track most recent fractal high and low values using var variables
4. Upper Band = Custom highest() function of fractal highs over period
5. Lower Band = Custom lowest() function of fractal lows over period

**Detailed calculation steps:**
1. For each bar, check if previous bar forms a fractal high or low using 5-bar pattern
2. Update `hi_fractal` variable when new fractal high is identified: `hi_fractal := high[1]`
3. Update `lo_fractal` variable when new fractal low is identified: `lo_fractal := low[1]`
4. Calculate highest fractal high using custom deque-based `highest()` function over specified period
5. Calculate lowest fractal low using custom deque-based `lowest()` function over specified period
6. Return upper and lower bands based on these optimized calculations

> 🔍 **Technical Note:** This implementation uses custom `highest()` and `lowest()` functions with deque-based algorithms for superior performance compared to built-in Pine Script functions. The functions use circular buffers and maintain sorted indices for O(1) amortized complexity.

## Embedded Algorithm Implementation

**Optimized Highest/Lowest Functions:**
- **Deque-based tracking:** Maintains indices of potential maximum/minimum values
- **Circular buffer:** Efficient memory usage with fixed-size arrays
- **Performance optimization:** O(1) amortized time complexity for real-time calculations
- **Dirty data handling:** Uses `nz()` for robust null value processing
- **Runtime validation:** Error checking for invalid period parameters

**Key Performance Features:**
- Monotonic deque maintains only relevant candidate values
- Automatic cleanup of expired indices outside the lookback window
- Efficient array operations using modular indexing
- Optimized for Pine Script's execution model

## Visual Elements

* **Upper FCB Band:** Blue line (width 1) representing highest fractal high over period
* **Lower FCB Band:** Blue line (width 1) representing lowest fractal low over period  
* **Fill Area:** Semi-transparent blue fill (85% transparency) between bands for easy visualization
* **Clean Design:** Minimal visual elements focusing on essential band structure
* **No fractal markers:** Current implementation doesn't plot fractal points despite input option

## Interpretation Details

FCB provides multiple layers of market analysis:

* **Trend Analysis:**
  - Bands with upward slope: Bullish trend in progress
  - Bands with downward slope: Bearish trend in progress
  - Flat/horizontal bands: Consolidation or sideways market
  - Steepening slope: Trend acceleration
  - Flattening slope: Trend deceleration or potential reversal

* **Band Interaction Signals:**
  - Price above upper band: Strong bullish momentum, potential overbought
  - Price below lower band: Strong bearish momentum, potential oversold
  - Price between bands: Normal market behavior within fractal range
  - Price touching bands: Potential support/resistance levels

* **Volatility Analysis:**
  - Wide bands: High volatility, large price swings expected
  - Narrow bands: Low volatility, potential breakout setup
  - Expanding bands: Increasing volatility
  - Contracting bands: Decreasing volatility, market stabilization

* **Market Structure:**
  - Band slope direction indicates dominant market force
  - Band width reflects current volatility regime
  - Fractal-based levels show key turning points in market structure

## Trading Applications

**Trend Following Strategy:**
- Enter long positions when price breaks above upper band with volume
- Enter short positions when price breaks below lower band with volume
- Use band slope to confirm trend direction and strength
- Exit when bands begin to flatten or reverse slope

**Mean Reversion Strategy:**
- Buy when price touches lower band in flat/sideways markets
- Sell when price touches upper band in flat/sideways markets
- Target the opposite band for profit-taking
- Use stops beyond the bands for risk management

**Breakout Strategy:**
- Monitor periods of narrow, flat bands for potential breakouts
- Enter positions on volume-confirmed breaks beyond the bands
- Use initial band width to set position size (wider bands = smaller positions)
- Trail stops using the bands as dynamic support/resistance

**Trend Strength Analysis:**
- Measure band slope angle to assess trend strength
- Steeper slopes indicate stronger, more sustainable trends
- Flattening slopes suggest trend weakness or exhaustion
- Use slope changes as early warning signals for trend reversals

## Signal Combinations

**High-Probability Long Signals:**
- Price breaks above upper band with steep upward band slope
- Price bounces off lower band with bands beginning to slope upward
- Fractal highs forming at progressively higher levels
- Volume expansion on band breakout to upside

**High-Probability Short Signals:**
- Price breaks below lower band with steep downward band slope
- Price fails at upper band with bands beginning to slope downward
- Fractal lows forming at progressively lower levels
- Volume expansion on band breakout to downside

**Consolidation/Range Signals:**
- Flat, horizontal bands with price oscillating between them
- Decreasing band width over time
- Multiple failed attempts to break beyond bands
- Low volume during band touches

## Advanced Techniques

**Multi-Timeframe Analysis:**
- Use higher timeframe FCB for major trend direction
- Combine daily FCB with intraday bands for precise entry timing
- Look for alignment between different timeframe band slopes
- Scale position sizes based on multi-timeframe band analysis

**Band Slope Measurement:**
- Calculate rate of change in band levels to quantify slope
- Use slope derivatives to identify trend acceleration/deceleration
- Monitor slope convergence/divergence between upper and lower bands
- Apply slope-based filters for trade entry and exit signals

**Performance Optimization:**
- Leverage the custom deque-based algorithms for faster calculations
- Monitor computational efficiency for high-frequency trading applications
- Use the optimized functions as building blocks for more complex indicators
- Adapt the algorithm for different timeframes and instruments

**Volatility Regime Trading:**
- Adjust trading strategies based on current band width
- Use band expansion/contraction cycles for position sizing
- Monitor volatility breakouts from narrow band periods
- Apply different risk management rules for different volatility regimes

## Limitations and Considerations

* **Lagging indicator:** Based on historical fractals, creating inherent lag
* **False breakouts:** Can generate whipsaws during volatile consolidations
* **Period sensitivity:** Performance varies with different period settings
* **Market type dependency:** More effective in trending markets than ranging conditions
* **Fractal lag:** Fractal identification requires 2-bar confirmation delay
* **Implementation note:** Fractal point display input exists but is not implemented in plots

## Comparison with Related Indicators

**FCB vs. Bollinger Bands:**
- FCB: Based on fractal highs/lows with optimized algorithms, focuses on market structure
- Bollinger Bands: Based on standard deviation, focuses on statistical extremes

**FCB vs. Donchian Channels:**
- FCB: Uses fractal-filtered highs/lows with custom optimization for noise reduction
- Donchian Channels: Uses simple highest/lowest values over period

**FCB vs. Keltner Channels:**
- FCB: Fractal-based bands with slope analysis capability and performance optimization
- Keltner Channels: ATR-based bands around moving average center

**FCB vs. Standard Highest/Lowest:**
- FCB: Custom deque-based algorithms for superior performance
- Standard functions: Basic Pine Script functions with lower efficiency

## Best Practices

**Parameter Optimization:**
- Start with default 20-period setting and adjust based on market timeframe
- Use shorter periods (10-15) for faster, more responsive signals
- Use longer periods (30-50) for smoother, less noisy signals
- Test different periods across various market conditions

**Performance Considerations:**
- Leverage the optimized custom functions for better execution speed
- Monitor computational resources when using multiple instances
- Consider the algorithm's efficiency for real-time trading applications
- Use as a foundation for building more complex trading systems

**Trend Analysis:**
- Focus on band slope direction for primary trend identification
- Use slope steepness to gauge trend strength and sustainability
- Monitor slope changes for early trend reversal warnings
- Combine with momentum indicators for comprehensive trend analysis

**Risk Management:**
- Set stops beyond the opposite band when trading breakouts
- Use band width for position sizing (wider bands = smaller positions)
- Monitor fractal-based support/resistance levels for reversal zones
- Adjust trade size based on current volatility regime

## References

* Williams, B. (1995). Trading Chaos: Applying Expert Techniques to Maximize Your Profits. John Wiley & Sons.
* Mandelbrot, B. (1982). The Fractal Geometry of Nature. W.H. Freeman.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
