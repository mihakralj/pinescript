# Moving Average Convergence Divergence (MACD)

## Description

The Moving Average Convergence Divergence (MACD) is one of the most popular momentum indicators, developed by Gerald Appel in the late 1970s. It shows the relationship between two exponential moving averages (EMAs) of a security's price and helps identify momentum, trend direction, and potential reversals.

The MACD consists of three components:
- **MACD Line**: The difference between fast EMA and slow EMA
- **Signal Line**: EMA of the MACD line
- **Histogram**: Difference between MACD line and signal line

## Parameters

- **Fast Length** (default: 12): Period for the fast EMA
- **Slow Length** (default: 26): Period for the slow EMA (must be greater than fast length)
- **Signal Length** (default: 9): Period for the signal line EMA
- **Source** (default: close): Input data series

## Formula

```
Fast EMA = EMA(source, fast_length)
Slow EMA = EMA(source, slow_length)
MACD Line = Fast EMA - Slow EMA
Signal Line = EMA(MACD Line, signal_length)
Histogram = MACD Line - Signal Line
```

## Usage

### Interpretation

1. **Crossovers**:
   - Bullish: MACD line crosses above signal line
   - Bearish: MACD line crosses below signal line

2. **Zero Line Crossovers**:
   - Bullish: MACD line crosses above zero
   - Bearish: MACD line crosses below zero

3. **Divergence**:
   - Bullish: Price makes lower lows while MACD makes higher lows
   - Bearish: Price makes higher highs while MACD makes lower highs

4. **Histogram**:
   - Growing histogram: Increasing momentum
   - Shrinking histogram: Decreasing momentum

### Trading Signals

- **Buy Signal**: MACD line crosses above signal line (bullish crossover)
- **Sell Signal**: MACD line crosses below signal line (bearish crossover)
- **Trend Confirmation**: MACD line position relative to zero line confirms trend direction

## Implementation Details

- Uses custom EMA implementation with proper initialization
- Stand-alone calculation without ta.* dependencies
- Optimized for performance with O(1) complexity
- Handles dirty data (NaN values) gracefully
- Returns valid values from the first bar

## Visualization

- **MACD Line**: Yellow line (linewidth=2)
- **Signal Line**: Orange line (linewidth=2)
- **Histogram**: Column chart with dynamic colors:
  - Bright teal: Positive and increasing
  - Light teal: Positive and decreasing
  - Light red: Negative and increasing
  - Bright red: Negative and decreasing
- **Zero Line**: Gray dashed line at zero level

## References

- Appel, Gerald (2005). *Technical Analysis: Power Tools for Active Investors*
- Murphy, John J. (1999). *Technical Analysis of the Financial Markets*
- [StockCharts: MACD](https://school.stockcharts.com/doku.php?id=technical_indicators:moving_average_convergence_divergence_macd)

## See Also

- [EMA](/indicators/trends_IIR/ema.md) - Exponential Moving Average
- [PPO](/indicators/momentum/ppo.md) - Percentage Price Oscillator (MACD percentage variant)
- [APO](/indicators/oscillators/apo.md) - Absolute Price Oscillator (similar concept)
