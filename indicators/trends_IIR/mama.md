# MESA Adaptive Moving Average (MAMA)

MESA Adaptive Moving Average is an adaptive moving average developed by John Ehlers. It automatically adjusts its smoothing parameter based on the rate-of-change of phase, making it highly responsive to market conditions without requiring manual parameter adjustments.

## Description

The MAMA indicator consists of two lines:

- **MAMA (MESA Adaptive Moving Average)**: The primary adaptive moving average line that responds quickly to price changes
- **FAMA (Following Adaptive Moving Average)**: A slower moving average that follows MAMA, providing confirmation and helping identify trend direction

MAMA dynamically adjusts its smoothing factor based on market conditions. It uses the Hilbert Transform to measure the efficiency of price movement and adapts accordingly:

- In trending markets, it uses faster smoothing to stay close to price and reduce lag
- In sideways markets, it uses slower smoothing to filter out noise and prevent whipsaws
- During trend transitions, it adapts smoothing speed to match the changing market conditions

Unlike traditional moving averages that use fixed parameters, MAMA's adaptive nature means it can:

- Provide earlier and more accurate trend signals
- Remain responsive during fast market moves
- Avoid getting "stuck" in noisy sideways markets
- Reduce false signals during choppy price action

## Key Features

- **Self-adjusting:** Automatically finds the optimal smoothing factor based on price behavior
- **Dual-indicator:** Provides both fast (MAMA) and slow (FAMA) lines for confirmation
- **Phase-aware:** Uses phase information rather than just magnitude for more precise adaptation
- **Cycle-sensitive:** Detects and adapts to dominant market cycles for improved timing
- **Noise-resistant:** Employs sophisticated filtering to distinguish signal from noise

## Calculation

The MAMA algorithm employs the following key steps:

1. Initial price smoothing
2. Hilbert Transform to create quadrature (90-degree phase-shifted) components
3. Phase calculation using I/Q components
4. Computation of delta phase (rate of phase change)
5. Adaptive alpha calculation based on delta phase
6. MAMA and FAMA calculation using the adaptive alpha

## Implementation Notes

The MAMA indicator's implementation involves several mathematical components:

1. **Price smoothing**: A 4-bar weighted averaging filter is applied to reduce noise
2. **Hilbert Transform**: Creates a pair of signals with 90° phase difference (I/Q signals)
3. **Phase detection**: Calculates the instantaneous phase angle of price movement
4. **Dominate cycle detection**: Estimates the current dominant cycle period
5. **Adaptive smoothing**: Derives the optimal alpha value from phase changes
6. **MAMA calculation**: Applies the adaptive alpha to current price and previous MAMA
7. **FAMA calculation**: Uses half the adaptive rate to follow MAMA at a slower pace

## Parameters

- **Source**: Input price series (default: close)
- **Fast Limit**: Maximum adaptation rate (default: 0.5)
  - Higher values make MAMA more responsive but potentially more erratic
  - Range typically between 0.3-0.7
- **Slow Limit**: Minimum adaptation rate (default: 0.05)
  - Higher values prevent MAMA from becoming too slow in sideways markets
  - Range typically between 0.01-0.1

## Trading Applications

MAMA can be used in various trading strategies:

- **Trend following**: Trade in the direction of MAMA slope
- **Crossover signals**: Generate entry/exit signals when price crosses MAMA
- **MAMA/FAMA crossovers**: Buy when MAMA crosses above FAMA, sell when it crosses below
- **Support/resistance**: Use MAMA as dynamic support in uptrends and resistance in downtrends
- **Volatility gauge**: The distance between MAMA and FAMA indicates market volatility

## Performance Notes

MAMA is computationally intensive but provides highly responsive adaptive smoothing.

- Reacts quickly to genuine price movements
- Filters out market noise during congestion
- Adapts to changing market conditions without parameter changes
- Performs well across different timeframes and markets

## References

Ehlers, J. (2001). "MESA and Trading Market Cycles", Chapter 11. John Wiley & Sons.
Ehlers, J. (2002). "Using the MESA Adaptive Moving Average", Technical Analysis of Stocks & Commodities, Volume 20: June.
Ehlers, J. (2005). "Measuring Market Spectra", Technical Analysis of Stocks & Commodities, Volume 23: October.
