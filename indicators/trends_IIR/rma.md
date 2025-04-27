# RMA: Wilder's Moving Average

[Pine Script Implementation of RMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/rma.pine)

## Overview and Purpose

Wilder's Moving Average (RMA), also known as the Smoothed Moving Average (SMMA), is a specialized technical indicator designed to provide superior noise reduction while maintaining sensitivity to meaningful price changes. Developed by J. Welles Wilder Jr. in the late 1970s and introduced in his influential 1978 book "New Concepts in Technical Trading Systems," RMA was specifically created to power Wilder's revolutionary technical indicators like RSI, ATR, and DMI/ADX.

RMA achieves its distinctive smoothing characteristics by using a specific smoothing factor of 1/period, positioning it as an intermediate option between the simple moving average (SMA) and the standard exponential moving average (EMA). This unique approach provides the consistent, well-behaved smoothing necessary for Wilder's indicators to function properly.

## Core Concepts

* **Specialized smoothing:** Uses a fixed 1/period smoothing factor that creates more stable output than standard EMA
* **Noise reduction:** Superior filtering of market noise compared to EMA while maintaining better responsiveness than SMA
* **Indicator foundation:** Forms the mathematical basis for Wilder's suite of technical indicators (RSI, ATR, ADX)
* **Balanced response:** Provides an optimal middle ground between the responsiveness of EMA and the stability of SMA

RMA achieves its unique characteristics by applying a smoothing factor (α = 1/period) that is consistently lower than the standard EMA formula (α = 2/(period+1)). This makes RMA approximately twice as slow to react compared to a standard EMA of the same period length, creating a smoother line that better filters out market noise.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the amount of smoothing | Wilder's original indicators used 14; increase for more smoothing, decrease for more responsiveness |
| Source | Close | Data point used for calculation | Change to High/Low for volatility measures or HL2/HLC3 for balanced price representation |
| Alpha override | auto | Direct control of smoothing factor | Set manually to fine-tune behavior beyond standard period settings |

**Pro Tip:** When replacing RMA in Wilder's original indicators with other moving averages, remember that an EMA with twice the period length (e.g., EMA(28)) will approximate the smoothing behavior of RMA(14).

## Calculation and Mathematical Foundation

**Simplified explanation:**
RMA works by taking a small portion (1/period) of the current price and adding it to a large portion ((period-1)/period) of the previous RMA value. This creates a very smooth moving average that reduces market noise while still adapting to price changes over time.

**Technical formula:**
RMA = (Previous RMA × (period - 1) + Current Price) / period

Which can be rewritten as:

RMA = α × Current Price + (1 - α) × Previous RMA

Where α = 1/period

> 🔍 **Technical Note:** Advanced implementations use mathematical compensation methods that correct initialization bias, providing accurate values from the first bar without waiting for a "warm-up" period. This compensation is calculated as: RMA_corrected = RMA_raw/(1 - compensation), where compensation decays by (1-α) on each bar.

## Interpretation Details

RMA provides several key benefits for technical analysis:

- Creates smoother trend lines compared to EMA, making trend direction easier to identify
- Reduces whipsaws and false signals in indicator calculations
- Maintains consistency across all of Wilder's indicators, enabling proper interpretation
- Functions as an effective dynamic support/resistance level in trending markets
- Provides stable baselines for measuring price momentum and volatility

RMA is particularly effective when used as the calculation engine for Wilder's suite of indicators (RSI, ATR, ADX) and as a standalone moving average for identifying medium to long-term trends with reduced noise.

## Limitations and Considerations

* **Market conditions:** Slower response makes it less suitable for fast-moving markets or short timeframes
* **Lag factor:** Exhibits more lag than standard EMA due to the smaller smoothing factor (approximately twice as much)
* **Specialized use:** Primarily designed for Wilder's indicators rather than as a general-purpose moving average
* **Parameter inflexibility:** Using the fixed 1/period smoothing factor reduces tuning options
* **Complementary tools:** Best used with faster indicators or price action analysis to compensate for the lag

## References

1. Wilder, J.W. (1978). *New Concepts in Technical Trading Systems*. Trend Research.
2. Murphy, J.J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
3. Kaufman, P.J. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
