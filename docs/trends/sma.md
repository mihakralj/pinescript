# Simple Moving Average (SMA)

The Simple Moving Average (SMA) is a fundamental technical indicator that calculates the average of a selected range of prices over a specified number of periods. As a core building block in technical analysis, the SMA provides a smoothed representation of price movement by filtering out short-term fluctuations. It assigns equal weight to all price points within the calculation window, making it straightforward to understand but less responsive to recent price changes compared to weighted averages.

[Pine Script Implementation of SMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/sma.pine)

## Mathematical Foundation

### Basic Formula

The SMA is calculated by summing the prices for a specific number of periods and then dividing by the number of periods:

SMA = (P₁ + P₂ + ... + Pₙ) / n

Where:
- P₁, P₂, ..., Pₙ are price values in the lookback window
- n is the number of periods (window size)

### Optimized Recursive Formula

For computational efficiency, the SMA can be calculated recursively, which significantly reduces the number of operations needed for each new calculation:

SMA₍ₙ₎ = SMA₍ₙ₋₁₎ + (Pₙ - Pₙ₋ₚ) / p

Where:
- SMA₍ₙ₎ is the current SMA value
- SMA₍ₙ₋₁₎ is the previous SMA value
- Pₙ is the current price
- Pₙ₋ₚ is the price p periods ago
- p is the period

This approach requires only 3 arithmetic operations (addition, subtraction, division) regardless of window size, compared to p additions and 1 division in the naive implementation.

## FIR Filter Nature

The SMA is a Finite Impulse Response (FIR) filter, a fundamental concept from signal processing theory. Understanding this property helps explain the behavior and limitations of the SMA:

### Key FIR Characteristics

1. **Fixed Window**: The SMA output depends only on a finite number of past inputs (exactly p values).
2. **Zero Weight Outside Window**: Values outside the window have zero influence on the current SMA.
3. **Impulse Response**: If a single impulse (spike) enters the system, its effect on the output lasts exactly p periods and then completely disappears.

### Transfer Function Properties

As a filter, the SMA has specific frequency domain characteristics:
- Acts as a low-pass filter, attenuating high-frequency components (noise)
- Has poor stop-band attenuation (only 13dB per octave)
- Exhibits significant ripple in the frequency response
- Introduces a phase delay of exactly (p-1)/2 periods

## Initialization Properties

Unlike IIR filters (such as EMA), the SMA has straightforward initialization characteristics:

### Full Window Requirement

The SMA requires a minimum of p data points before producing its first "true" output. For a period of p, several approaches exist for handling the first p-1 values:

1. **NA Values**: Return "not available" until enough data points exist

2. **Padding**: Use pre-period values (e.g., repeat first value) to enable calculation from bar 1

3. **Partial Window Calculation**: (used by this implementation) Calculate averages with available data points until the window is filled:
SMA₍ₙ₎ = (P₁ + P₂ + ... + Pₙ) / n, where n < p

## Window Size Considerations

The window size (period) directly controls the filter properties:

1. **Smoothness vs. Responsiveness**: Larger windows produce smoother outputs but with more lag
2. **Signal-to-Noise Ratio**: Increasing the period improves SNR at the cost of responsiveness
3. **Computational Efficiency**: The recursive formulation maintains O(1) time complexity regardless of window size
4. **Memory Requirements**: O(p) space complexity to store the window values

Common window sizes and their typical applications:

| Period | Common Applications                            | Characteristics                     |
|--------|------------------------------------------------|-------------------------------------|
| 5-10   | Short-term trends, intraday signals            | Responsive, noisy                   |
| 20-50  | Medium-term trend identification               | Balanced smoothness and delay       |
| 100-200| Long-term trend identification                 | Very smooth, significant lag        |
| 200+   | Support/resistance, secular trend detection    | Extreme smoothing, maximum delay    |

## Advantages and Disadvantages of SMA

### Advantages

- **Simplicity**: Easy to understand, calculate, and implement
- **Predictability**: Each price has precisely known influence on the average
- **Equal Weighting**: No bias toward recent or old data
- **No Initialization Bias**: Produces valid outputs as soon as window is filled
- **Deterministic Lag**: Precisely (p-1)/2 bars of lag for symmetrical smoothing
- **Linear Phase Response**: Preserves the shape of the signal within the passband

### Disadvantages

- **Lag**: Significant lag in responding to price changes
- **Equal Weighting**: Recent prices affect the average equally as older prices
- **Sudden Changes**: When a price leaves the window, it can cause abrupt changes in the SMA
- **Binary Cutoff**: Sharp cutoff between prices that have influence (1/p) and those with no influence (0)
- **Poor Frequency Selectivity**: Relatively poor separation between signal and noise components
