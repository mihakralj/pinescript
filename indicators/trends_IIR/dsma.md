# DSMA: Deviation-Scaled Moving Average

[Pine Script Implementation of DSMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/dsma.pine)

## Overview and Purpose

The Deviation-Scaled Moving Average (DSMA) is an adaptive technical indicator that automatically adjusts its smoothing factor based on price deviation from the average. Introduced to address the limitations of fixed-parameter moving averages in volatile modern markets, DSMA provides a self-adjusting mechanism that becomes more responsive during significant price movements while maintaining stability during normal market conditions.

Unlike traditional moving averages that apply the same smoothing regardless of market behavior, DSMA uses a second-order IIR filter to measure normalized price deviations and adjust its responsiveness accordingly. This creates a moving average that effectively reduces noise during sideways markets while responding quickly to genuine breakouts or trend changes. The result is an indicator that provides cleaner signals across different market regimes without requiring manual parameter adjustments.

## Core Concepts

* **Deviation-based adaptation:** Automatically adjusts the smoothing factor based on the normalized deviation of price from its moving average
* **Filter-based measurement:** Uses a second-order IIR filter to detect meaningful deviations while filtering out random noise
* **RMS normalization:** Applies root mean square calculations to properly scale deviation measurements across different market conditions
* **Non-linear response:** Creates a proportional response curve that increases sensitivity during significant price movements

DSMA achieves its adaptive nature by filtering the deviation between price and the average, then normalizing this filtered deviation through root mean square calculations. This creates a scaling factor that determines how quickly the average responds to new price information - becoming more responsive during genuine market movements and more stable during normal conditions.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 25 | Controls the base period and filter characteristics | Increase for longer-term trends, decrease for shorter-term signals |
| Scale Factor | 0.9 | Determines the intensity of adaptive behavior | Lower (0.3-0.5) for more conservative adaptation, higher (0.7-0.9) for more aggressive adaptation |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** Many professional traders find that a scale factor around 0.7-0.8 with a slightly longer period (25-30) provides an optimal balance between responsiveness during breakouts and stability during normal market conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
DSMA works by measuring how much price is deviating from its average in a meaningful way. When price makes significant moves away from the average, DSMA becomes more responsive to follow the new trend. When price is moving normally around the average, DSMA maintains a smoother, more stable line.

**Technical formula:**
1. Calculate filter parameters based on period:
   - a₁ = exp(-1.414π/period)
   - b₁ = 2a₁cos(1.414π/period)
   - c₁ = 1 - b₁ + a₁²

2. Calculate filtered deviation between price and average:
   - zeros = price - average
   - filt = c₁/2 × (zeros + previous_zeros) + b₁ × previous_filt - a₁² × previous_filt2

3. Calculate RMS of filtered deviation:
   - Store filt² in a rolling buffer
   - RMS = sqrt(sum(filt²)/period)

4. Calculate adaptive alpha:
   - α = min(scale_factor × |filt/RMS| × (5/period), 1.0)

5. Apply final formula:
   - DSMA = α × price + (1-α) × previous_DSMA

> 🔍 **Technical Note:** The second-order IIR filter used to process deviations provides significant advantages over simple deviation measurements. It effectively passes meaningful trend components while attenuating random noise, creating a much more reliable basis for adaptation. The RMS normalization ensures consistent behavior across different volatility environments, preventing over-response in highly volatile markets.

## Interpretation Details

DSMA provides several key insights for traders:

- When price crosses above DSMA, it often signals the beginning of an uptrend
- When price crosses below DSMA, it often signals the beginning of a downtrend
- The slope of DSMA provides insight into trend strength and momentum
- DSMA responds more quickly to significant breakouts than traditional moving averages
- During consolidation periods, DSMA stabilizes to provide a clearer picture of the underlying trend
- Multiple DSMA lines with different periods can identify key support/resistance levels

DSMA is particularly valuable for trading strategies that need to adapt to changing market conditions. It excels at filtering out noise during consolidations while still responding quickly to genuine breakouts, making it especially useful for breakout trading systems and trend-following strategies.

## Limitations and Considerations

* **Market conditions:** While adaptive, extreme volatility conditions can still create challenges for proper normalization
* **Calculation complexity:** More computationally intensive than simple moving averages due to filtering and RMS calculations
* **Parameter sensitivity:** Scale factor selection can significantly impact behavior despite the adaptive mechanism
* **Initialization period:** Requires a full period of data to properly establish the RMS baseline
* **Complementary tools:** Works best when combined with volume analysis or momentum indicators for confirmation

## References

1. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons.
2. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
3. Zirilli, A. (2001). *Financial Prediction Using Neural Networks*. International Thomson Computer Press.
