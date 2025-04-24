# Wilder's Moving Average (RMA)

## Historical Background

Wilder's Moving Average (RMA) was developed by J. Welles Wilder Jr. in the late 1970s. Introduced in his influential 1978 book "New Concepts in Technical Trading Systems," RMA quickly became a cornerstone of technical analysis.

Wilder created this moving average specifically for his innovative technical indicators, including RSI (Relative Strength Index), ATR (Average True Range), and DMI/ADX (Directional Movement Index/Average Directional Index). Its adoption has been widespread, particularly in trend-following and volatility-based trading systems. The RMA's unique smoothing approach has made it a standard component in virtually all technical analysis platforms.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/rma.pine)

## Core Concepts

Wilder's RMA was designed specifically for technical indicators requiring:

- Superior noise reduction compared to standard EMAs
- Consistent smoothing behavior across different market conditions
- Specific 1/N smoothing factor for optimal indicator performance
- Balanced approach between responsiveness and stability

Wilder needed a moving average that would be more responsive than SMA but less volatile than EMA for his technical indicators. His solution was to use a modified exponential moving average with a specific smoothing factor of 1/period, which became known as RMA. This smoothing factor creates a more stable line that reduces noise while maintaining sensitivity to signal changes.

## Mathematical Foundation

The RMA calculation uses Wilder's specific smoothing approach:

RMA_n = (RMA_n-1 × (period - 1) + Price_n)/period

Where:
- RMA_n is the current RMA value
- RMA_n-1 is the previous RMA value
- Price_n is the current signal
- period is the lookback period

## Calculation Process

The formula can be rewritten in terms of alpha (α = 1/period):

RMA_n = α × Price_n + (1 - α) × RMA_n-1

This form shows RMA as a specific case of exponential smoothing where α = 1/period.

### Implementation Methods

1. **Traditional Initialization (SMA-based)**
   - Uses SMA for the first period's worth of data
   - Creates a discontinuity when switching from SMA to RMA
   - Requires waiting for a full period before getting meaningful values

2. **Compensated Initialization**
   - Starts calculation from first bar with zero initialization
   - Tracks the influence of missing history through a compensation factor
   - Adjusts the raw RMA value based on this compensation
   - Gradually reduces compensation as more data becomes available

   The corrected RMA is calculated as:
   
   RMA_corrected = RMA_raw/(1 - compensation)
   
   Where:
   - RMA_raw is the standard RMA calculation
   - Compensation decays by (1-α) each bar
   - α = 1/period (Wilder's smoothing factor)

## Advantages and Limitations

### Advantages
- Smoother than EMA, reducing noise in technical indicators
- Only needs previous value, not entire lookback period
- Works exceptionally well with Wilder's technical indicators
- With compensation, provides accurate values from first bar
- Avoids initialization discontinuities

### Limitations
- Slower to respond to signal changes than EMA
- Primarily used in Wilder's indicators
- Less flexible than EMA in terms of smoothing factor
- Calculation errors compound over time
- Each value depends on all previous values

## Sources

1. Wilder, J.W. (1978). *New Concepts in Technical Trading Systems*. Trend Research.
2. Pring, M.J. (2002). *Technical Analysis Explained*, 4th Edition. McGraw-Hill.
3. Kaufman, P.J. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
4. Murphy, J.J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
