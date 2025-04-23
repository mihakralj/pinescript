# Schaff Trend Cycle (STC)

The Schaff Trend Cycle (STC) is a technical analysis indicator developed by Doug Schaff. It's an oscillator that combines elements of MACD (Moving Average Convergence Divergence) and stochastics to create a cyclical indicator designed to identify market trends and potential reversal points.

[Pine Script Implementation of STC](https://github.com/mihakralj/pinescript/blob/main/indicators/cycles/stc.pine)

## Mathematical Foundation

The STC calculation involves several steps:

1. Calculate a MACD line by taking the difference between fast and slow EMAs:
  
   MACD = EMA(Source, Fast_Length) - EMA(Source, Slow_Length)

2. Apply a double stochastic calculation to the MACD line:

   Stoch_1 = EMA((MACD - min(MACD, Cycle_Length))/(max(MACD, Cycle_Length) - min(MACD, Cycle_Length)) × 100, 3)
  
   Stoch_2 = (Stoch_1 - min(Stoch_1, Cycle_Length))/(max(Stoch_1, Cycle_Length) - min(Stoch_1, Cycle_Length)) × 100

3. Apply optional smoothing to the final output:
   - None: STC = Stoch_2
   - EMA: STC = EMA(Stoch_2, 3)
   - Sigmoid: STC = 100/(1 + e^(-0.1 × (Stoch_2 - 50)))
   - Digital:
  
     - If Stoch_2 > 75, then STC = 100
     - If Stoch_2 < 25, then STC = 0
     - Otherwise, STC = previous STC value

## Key Components

- **Cycle Length**: The main parameter that determines the lookback period for the stochastic calculations
- **Fast Length**: Period for the fast EMA in the MACD calculation
- **Slow Length**: Period for the slow EMA in the MACD calculation
- **Smoothing Type**: Method used to smooth the final STC value (None, EMA, Sigmoid, or Digital)
- **Thresholds**: 25 and 75 levels commonly used to identify oversold and overbought conditions

## Advantages and Disadvantages

### Advantages

- Combines trend-following and momentum indicators for potentially more accurate signals
- Reduces whipsaws by filtering out some of the noise in price action
- The smoothing options allow traders to customize the sensitivity of the indicator
- Works well in both trending and ranging markets when properly configured
- Dynamic enough to adapt to changing market conditions

### Disadvantages

- Like most oscillators, can generate false signals during strong trends
- Multiple parameters require optimization for different markets and timeframes
- Lagging indicator due to the multiple moving averages and smoothing operations
- Digital smoothing option can mask important nuances in the indicator's movement
- May not provide early enough entry signals in rapidly changing market conditions
