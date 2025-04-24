# MESA Adaptive Moving Average (MAMA)

## Historical Background

The MESA Adaptive Moving Average (MAMA) was developed by John Ehlers and introduced in 2001 in his book "MESA and Trading Market Cycles." Ehlers, known for his background in electrical engineering and signal processing, applied concepts from these fields to create an innovative technical indicator.

MAMA quickly gained recognition among technical analysts for its sophisticated approach to adaptive smoothing based on cycle analysis. Its adoption has grown significantly in algorithmic trading systems and professional trading platforms. The indicator's innovative use of the Hilbert Transform and phase analysis has influenced the development of numerous adaptive indicators in technical analysis.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/mama.pine)

## Core Concepts

MAMA represents a significant advancement in moving average technology through:

- Hilbert Transform application to market data
- Phase-based adaptation rather than simple volatility measures
- Dual-line system for confirmation and trend identification
- Cycle-sensitive adaptation for optimal market timing

The MAMA indicator consists of two lines:

- **MAMA (MESA Adaptive Moving Average)**: The primary adaptive moving average line that responds quickly to price changes
- **FAMA (Following Adaptive Moving Average)**: A slower moving average that follows MAMA, providing confirmation and helping identify trend direction

## Mathematical Foundation

The MAMA calculation is based on the Hilbert Transform to determine cycle periods and phase angles. The key mathematical components include:

1. **Hilbert Transform Calculations:**
   - Creates quadrature (90-degree phase-shifted) components
   - Allows measurement of instantaneous phase

2. **Phase Rate-of-Change:**
   - Measures how quickly market cycles are evolving
   - Determines appropriate adaptation speed

3. **Adaptive Alpha Formula:**
   - α = FastLimit / (PhaseRatio + 1)
   - Constrained between SlowLimit and FastLimit
   - PhaseRatio derived from dominant cycle period

## Calculation Process

1. **Price Smoothing:**
   - Apply initial 4-bar weighted average filter to reduce noise

2. **Hilbert Transform:**
   - Generate in-phase and quadrature components
   - I/Q signals represent market cycles

3. **Phase Calculation:**
   - Determine instantaneous phase angle from I/Q components
   - Calculate delta phase (rate of phase change)

4. **Dominant Cycle Detection:**
   - Estimate current dominant cycle period
   - Use cycle period to adjust adaptation rate

5. **Adaptive Alpha Determination:**
   - Calculate optimal alpha based on cycle characteristics
   - Constrain within user-defined limits (FastLimit, SlowLimit)

6. **MAMA Calculation:**
   - MAMA_t = α × Price_t + (1 - α) × MAMA_t-1

7. **FAMA Calculation:**
   - FAMA_t = 0.5 × α × MAMA_t + (1 - 0.5 × α) × FAMA_t-1

## Advantages and Limitations

### Advantages
- Automatically adapts to changing market conditions
- Based on cycle analysis rather than simple volatility or efficiency measures
- Dual-line system provides confirmation signals
- Reduces whipsaws in choppy markets while remaining responsive in trends
- No need for manual parameter adjustments as market conditions change

### Limitations
- Computationally intensive compared to simpler moving averages
- Complex implementation requiring multiple calculation stages
- Can be less predictable than fixed-parameter indicators
- May produce irregular results during cycle transitions
- Requires careful implementation of the Hilbert Transform components

## Sources

1. Ehlers, J. (2001). *MESA and Trading Market Cycles*. John Wiley & Sons.
2. Ehlers, J. (2002). "Using the MESA Adaptive Moving Average," *Technical Analysis of Stocks & Commodities*, Volume 20: June.
3. Ehlers, J. (2005). "Measuring Market Spectra," *Technical Analysis of Stocks & Commodities*, Volume 23: October.
4. Ehlers, J. (2013). *Cycle Analytics for Traders*. Wiley Trading.
