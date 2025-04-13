# Simple Moving Average (SMA)

The Simple Moving Average (SMA) is a fundamental technical indicator that calculates the average of a selected range of signals over a specified number of periods. As a core building block in technical analysis, the SMA provides a smoothed representation of signal movement by filtering out short-term fluctuations. It assigns equal weight to all data points within the calculation window, making it straightforward to understand but less responsive to recent signal changes compared to weighted averages.

[Pine Script Implementation of SMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/sma.pine)

## Mathematical Foundation

### Basic Formula

The SMA is calculated by summing the signals for a specific number of periods and then dividing by the number of periods:

SMA = (P₁ + P₂ + ... + Pₙ) / n

Where:
- P₁, P₂, ..., Pₙ are signal values in the lookback window
- n is the number of periods (window size)

### Optimized Recursive Formula

For computational efficiency, the SMA can be calculated recursively, which significantly reduces the number of operations needed for each new calculation:

SMA₍ₙ₎ = SMA₍ₙ₋₁₎ + (Pₙ - Pₙ₋ₚ) / p

Where:
- SMA₍ₙ₎ is the current SMA value
- SMA₍ₙ₋₁₎ is the previous SMA value
- Pₙ is the current signal
- Pₙ₋ₚ is the signal p periods ago
- p is the period

This approach requires only 3 arithmetic operations (addition, subtraction, division) regardless of window size, compared to p additions and 1 division in the naive implementation.

## FIR Filter Characteristics

The SMA is a Finite Impulse Response (FIR) filter that processes data through a fixed-size window. Its behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of SMA include:
1. **Roll-off Rate**: Low-pass filtering with -13dB per octave roll-off
2. **Frequency Response**: Contains significant stopband ripple
3. **Phase Response**: Perfect linear phase in passband
4. **Gain**: Sinc function shape in frequency domain

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Fixed window length (exactly p values)
   - Uniform weights (1/p) within window
   - Zero response outside window

2. **Step Response**:
   - Linear ramp over p periods
   - No overshoot or undershoot
   - Symmetric around midpoint

3. **Delay Properties**:
   - Fixed phase delay of (p-1)/2 periods
   - Constant group delay across frequencies
   - Perfect preservation of signal shape

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
- **Predictability**: Each signal has precisely known influence on the average
- **Equal Weighting**: No bias toward recent or old data
- **No Initialization Bias**: Produces valid outputs as soon as window is filled
- **Deterministic Lag**: Precisely (p-1)/2 bars of lag for symmetrical smoothing
- **Linear Phase Response**: Preserves the shape of the signal within the passband

### Disadvantages

- **Lag**: Significant lag in responding to signal changes
- **Equal Weighting**: Recent signals affect the average equally as older signals
- **Sudden Changes**: When a signal leaves the window, it can cause abrupt changes in the SMA
- **Binary Cutoff**: Sharp cutoff between signals that have influence (1/p) and those with no influence (0)
- **Poor Frequency Selectivity**: Relatively poor separation between signal and noise components
