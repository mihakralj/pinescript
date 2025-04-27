# JMA: Jurik Moving Average

[Pine Script Implementation of JMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/jma.pine)

## Overview and Purpose

The Jurik Moving Average (JMA) is an advanced technical indicator designed to provide superior smoothing with minimal lag through adaptive volatility-based adjustments. Developed by Mark Jurik in the late 1990s, JMA quickly gained recognition among professional traders for its ability to filter market noise while maintaining responsiveness to genuine price movements.

It's important to note that the original JMA algorithm is proprietary, and Mark Jurik never published the exact calculations. All implementations available in trading platforms and programming languages (including this Pine Script version) are reverse-engineered approximations based on observed behavior. While these approximations often perform similarly to the original, they may differ in certain aspects from Jurik's implementation.

This approximation uses a multi-stage filtering process that adjusts dynamically to market conditions, creating a moving average that effectively balances smoothness and responsiveness across different market environments.

## Core Concepts

* **Adaptive volatility response:** Automatically adjusts smoothing parameters based on recent market volatility measurements
* **Phase parameter control:** Provides a user-adjustable setting to balance between lag reduction and smoothness
* **Multi-stage filtering:** Employs multiple calculation stages with dynamic coefficient adjustments for optimized performance
* **Power factor customization:** Allows fine-tuning of the adaptive response to match specific market characteristics

JMA achieves its performance through a complex volatility normalization process that measures price movements relative to recent volatility trends. This creates a moving average that can quickly adjust its responsiveness during different market conditions - becoming more sensitive during genuine trend movements while filtering out random fluctuations more effectively than standard moving averages.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 10 | Controls base smoothing length | Increase for longer-term trends, decrease for shorter-term signals |
| Phase | 0 | Adjusts lag/smoothness balance (-100 to 100) | Negative values reduce lag but may increase overshoot, positive values increase smoothness |
| Power | 0.45 | Controls adaptivity sensitivity (0.1-1.0) | Lower values create smoother output, higher values increase responsiveness to volatility changes |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** Many professional traders find that using negative phase values between -50 and -30 with slightly reduced power (0.3-0.4) provides an optimal balance of responsiveness and signal quality across most market conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
JMA works by first measuring price volatility using a  sampling method. It then uses this volatility measurement to adjust how quickly the moving average responds to price changes. A complex multi-stage filtering process applies these adaptive parameters to create a smooth output that adjusts automatically to changing market conditions.

**Technical formula:**
Our approximation implements these key calculation stages:

1. Volatility measurement using adaptive upper/lower bands:
   - Calculate price deviations from previous bands
   - Maintain a rolling 10-bar volatility measurement
   - Normalize current volatility relative to average volatility

2. Dynamic parameter adjustment:
   - Adjust smoothing factors based on normalized volatility
   - Apply power function to create non-linear response
   - Scale response based on user parameters

3. Multi-stage filtering with phase adjustment:
   - Apply primary smoothing with adaptive alpha
   - Calculate momentum component with beta coefficient
   - Apply phase shift to create phase-adjusted value
   - Calculate final JMA using squared-alpha smoothing

> 🔍 **Technical Note:** This implementation is an approximation of the proprietary JMA algorithm. While it captures the essential adaptive behavior, the exact calculations used in Jurik's original formula remain unpublished. Our implementation focuses on recreating the practical performance characteristics rather than reverse-engineering the exact proprietary method.

## Interpretation Details

JMA provides several key insights for traders:

- When price crosses above JMA, it often signals the beginning of an uptrend
- When price crosses below JMA, it often signals the beginning of a downtrend
- The slope of JMA provides insight into trend strength and momentum
- JMA creates smooth, reliable support and resistance levels during trending markets
- Multiple JMA lines with different periods create a "ribbon" effect that helps visualize trend strength

JMA is particularly valuable in volatile markets, where its adaptive nature helps distinguish between genuine trend changes and market noise. Its balance of smoothness and responsiveness makes it effective for both trend identification and dynamic support/resistance levels.

## Limitations and Considerations

* **Approximation accuracy:** Being a reverse-engineered approximation of a proprietary algorithm, exact behavior may differ from Jurik's original implementation
* **Computational complexity:** More resource-intensive than simple moving averages due to multi-stage calculations
* **Parameter sensitivity:** Performance highly dependent on phase and power settings, requiring careful optimization
* **Learning curve:** More complex behavior than standard moving averages, requiring time to understand fully
* **Complementary tools:** Works best when combined with volume analysis or momentum indicators for confirmation

## References

1. Jurik, M. "The Jurik Moving Average," (proprietary documentation).
