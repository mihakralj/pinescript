# CONV: Convolution

[Pine Script Implementation of CONV](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/conv.pine)

## Overview and Purpose

The Convolution (CONV) is a flexible technical indicator that allows traders to apply any arbitrary weighting scheme (kernel) to price data. Rooted in signal processing principles developed in the 1950-60s, convolution filtering was later adapted to financial markets in the 1990s as digital signal processing techniques gained popularity in technical analysis. Convolution provides a generalized framework that enables traders to create customized moving averages with specific filtering characteristics, either by designing their own weight distributions or using predefined kernels.

## Core Concepts

* **Customizable weighting:** Convolution allows any sequence of weights to be applied to price data, enabling precise control over filtering behavior
* **Kernel flexibility:** Supports both simple weight distributions (like those used in SMA) and complex multi-lobe designs with specialized filtering properties
* **Market application:** Particularly valuable for traders who need to design specialized filters for specific market conditions or trading strategies

The core innovation of convolution is its implementation of the fundamental convolution operation from signal processing. This provides a unified framework that can replicate many standard moving averages through appropriate kernel selection, while also allowing for experimentation with novel weight distributions that aren't available in standard indicators.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | Varies | Controls the kernel size | Increase for smoother signals, decrease for responsiveness |
| Kernel | Custom | Defines the weight distribution | Change based on desired filtering characteristics |
| Source | close | Price data used for calculation | Typically left at default; can be changed based on analysis focus |

**Pro Tip:** Start with established kernels like Gaussian or Blackman, then gradually modify weights to achieve your specific filtering needs. Keep a record of kernel configurations that work well in different market conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Convolution calculates a weighted average of prices where you can specify exactly how much importance to give each price in the lookback period. The weights can follow any pattern you design, giving complete control over how the moving average behaves.

**Technical formula:**
CONV = Σ(Price[i] × Kernel_Weight[i]) / Σ(Kernel_Weight[i])

Where:
- Kernel_Weight[i] is the user-defined weight for position i in the lookback window
- All weights are normalized to ensure they sum to 1.0, maintaining proper scaling

> 🔍 **Technical Note:** Kernel normalization ensures that the resulting moving average maintains consistent amplitude regardless of the absolute values of the kernel weights, making it easier to compare results across different kernel designs.

## Interpretation Details

Convolution can be used in various ways depending on the kernel design:

* **Trend identification:** With appropriate kernels, convolution can identify trends while filtering out noise
* **Specialized filtering:** Custom kernels can be designed to target specific price patterns or cycles
* **Moving average replication:** Convolution can replicate virtually any other moving average by using the appropriate kernel
* **Educational tool:** Helps understand how different weight distributions affect moving average behavior
* **Experimental strategies:** Enables testing of novel filtering approaches not available in standard indicators

## Limitations and Considerations

* **Knowledge requirement:** Requires understanding of convolution and filter design principles
* **Parameter complexity:** More parameters to optimize compared to standard moving averages
* **Potential overfitting:** Easy to create kernels that work well on historical data but fail on future data
* **Computational demands:** Slightly higher computational requirements than hardcoded implementations
* **Validation necessity:** Custom kernels require thorough testing to ensure desired filtering characteristics

## References

* Smith, S.W. "The Scientist and Engineer's Guide to Digital Signal Processing," Chapter 7: Properties of Convolution
* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
