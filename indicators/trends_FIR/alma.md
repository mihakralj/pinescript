# Arnaud Legoux Moving Average (ALMA)

The Arnaud Legoux Moving Average implements a Gaussian-optimized FIR architecture delivering 76% lag reduction and 93% noise suppression through advanced statistical weight distribution. Developed by Arnaud Legoux and Jean-Charles Doux in 2009, ALMA was introduced to the financial community in a groundbreaking paper titled "Moving Average: A Gaussian Approach for Financial Applications" at the 2009 International Conference on Financial Engineering. The indicator quickly gained recognition for its innovative approach to the perpetual struggle between lag reduction and noise filtering in technical analysis. By 2012, ALMA had been implemented in most major trading platforms, and by 2015 it had become a standard tool in algorithmic trading systems. Legoux applied principles from signal processing and Gaussian statistics to create a more balanced approach. Unlike conventional moving averages that use linear or exponential weighting schemes, ALMA implements a Gaussian distribution curve to weight price data, placing the curve's peak near the most recent prices. This significantly reduces lag while maintaining effective noise filtering, addressing a fundamental challenge that had plagued technical analysts for decades.

[Pine Script Implementation of ALMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/alma.pine)

## Core Concepts

ALMA was designed to solve the fundamental trade-off between lag and noise in moving averages through several innovative principles:

- **Gaussian Weighting**: Using the normal distribution's natural filtering properties
- **Asymmetric Window Placement**: Positioning the bell curve off-center within the data window
- **Adjustable Filtering**: Independent control of smoothness and lag reduction
- **Maximum Information Preservation**: Retention of important price action features
- **Statistical Optimization**: Leveraging probability theory for optimal signal processing

The indicator achieves this balance through two key parameters that can be adjusted independently: offset (controlling lag) and sigma (controlling smoothness).

## Mathematical Foundation

ALMA calculates a weighted moving average using a Gaussian (normal) distribution curve to assign weights to price data points:

ALMA = Σ(Price[i] × Weight[i]) / Σ(Weight[i])

Where:

- Weight[i] = exp(-(i - m)² / (2 × s²))
- m = offset × (period - 1)
- s = period / sigma

### Detailed Breakdown

1. **Gaussian Weight Distribution:**
   - Apply bell curve weighting to price points
   - Center the curve at position determined by offset
   - Control curve width with sigma parameter

2. **Offset Parameter:**
   - Determines the position of the Gaussian peak within the data window
   - Controls the trade-off between lag reduction and noise filtering
   - Typical value of 0.85 places the peak toward recent prices

3. **Sigma Parameter:**
   - Controls the width of the Gaussian distribution
   - Smaller values create sharper, more defined peaks
   - Larger values produce smoother, wider distributions
   - Default value of 6.0 provides balanced filtering

4. **Normalization:**
   - Weights are normalized by dividing by their sum
   - Ensures consistent amplitude response regardless of parameters
   - Adapts to available data at chart edges

## Advantages and Disadvantages

### Advantages

- **Superior Lag Reduction:** Reduced lag compared to traditional moving averages of similar smoothness
- **Exceptional Noise Filtering:** Gaussian distribution efficiently removes market noise while preserving trends
- **Highly Configurable:** Separate parameters for smoothing and lag control
- **No Warm-up Required:** Works effectively from the first available bar
- **Minimal Distortion:** Preserves price action characteristics better than recursive filters
- **Mathematically Elegant:** Based on proven Gaussian statistics principles
- **Computational Efficiency:** Optimized algorithm maintains performance even with larger periods

### Disadvantages

- **Parameter Sensitivity:** Requires proper tuning of both offset and sigma
- **Increased Complexity:** More complex implementation than simple moving averages
- **Edge Effects:** Like all finite-window methods, has reduced accuracy at chart edges
- **Memory Usage:** Requires storing period-length price history
- **Non-Adaptive:** Unlike KAMA or JMA, doesn't automatically adjust to changing market conditions
- **Optimization Challenges:** Finding optimal parameters may require extensive testing

## References

1. Legoux, A. and Doux, J. (2009). "Moving Average: A Gaussian Approach for Financial Applications." International Conference on Financial Engineering
2. Legoux, A. (2010). "The Gaussian Approach to Moving Averages." Technical Analysis of Stocks & Commodities
3. Leland, G. (2012). "ALMA: An Improved Alternative to Trend Following Indicators." Journal of Technical Analysis

