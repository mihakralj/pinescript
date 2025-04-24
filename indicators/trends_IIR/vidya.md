# Variable Index Dynamic Average (VIDYA)

The Variable Index Dynamic Average (VIDYA) is an adaptive moving average that adjusts its smoothing factor based on market volatility. It was developed by Tushar Chande to create a more responsive moving average during volatile market periods and a smoother average during low volatility periods.

## Formula

VIDYA uses a volatility index (VI) to adjust the smoothing factor:

```
α = 2 / (period + 1)
VI = StdDev(price, 5) / StdDev(price, period)
VI is clamped to [0,1] range
SC = α * VI
VIDYA_today = VIDYA_yesterday + SC * (Price_today - VIDYA_yesterday)
```

Where:
- α is the base smoothing factor
- VI is the volatility index
- SC is the scaled smoothing constant

## Implementation

The VIDYA indicator introduces adaptive behavior by scaling the EMA smoothing factor based on relative volatility. When volatility is high, VIDYA responds faster to price changes, while during low volatility periods, it produces a smoother line.

Key features of the implementation:
- Uses standard deviation ratios to measure relative volatility
- Includes proper initialization and warmup compensation
- Handles boundary conditions and edge cases
- Clamps the volatility index between 0 and 1 to prevent extreme values

## Parameters

- `source`: The price series to calculate VIDYA from (default: close)
- `period`: The length of the smoothing period (default: 10)
- `std_period`: The length of the standard deviation period (default: same as period)

## Comparison with other Indicators

VIDYA differs from standard moving averages like SMA and EMA by its adaptive nature. Compared to other adaptive indicators:

- Unlike KAMA which uses the Efficiency Ratio, VIDYA uses a volatility ratio
- VIDYA tends to be more responsive than EMA during high volatility periods
- Compared to DEMA, VIDYA uses volatility to adjust its smoothing rather than double smoothing

## Use Cases

VIDYA is particularly useful for:

- Trend following in markets with varying volatility
- Reducing lag during volatile market conditions
- Smoothing price action during consolidation periods
- Signal generation in adaptive trading systems

## Performance Considerations

The implementation is optimized for both performance and proper handling of dirty data. It includes a warmup compensation mechanism to provide accurate results from the first available bar.
