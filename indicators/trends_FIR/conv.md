# Convolution Moving Average (CONV)

The Convolution Moving Average implements a flexible, user-customizable filter that can apply any arbitrary kernel to price data. This generalized FIR filter allows traders to create specialized moving averages with unique frequency-domain characteristics by designing their own weight distributions or using predefined kernels. CONV enables superior control over noise reduction and signal preservation characteristics through direct kernel manipulation.

[Pine Script Implementation of CONV](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/conv.pine)

## Mathematical Foundation

The CONV calculation applies a custom kernel as the weight distribution across a sliding window:

CONV = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:

- P₁, P₂, ..., Pₙ are data values in the lookback window
- w₁, w₂, ..., wₙ are the kernel weights (user-defined or from built-in presets)
- n is the kernel size

### Kernel Definition and Normalization

The kernel is an array of weights that defines the relative importance of each data point in the convolution. All kernels are automatically normalized to ensure their weights sum to 1.0, maintaining the scale of the original data:

w'ᵢ = wᵢ / Σwⱼ

This normalization ensures that the resulting moving average maintains proper scaling regardless of the magnitude of the original kernel weights.

## Built-in Kernel Presets

The implementation provides several built-in kernel options:

1. **Rectangular Kernel** - Equivalent to Simple Moving Average (SMA)
   - All values in the window have equal weight
   - Example: [1, 1, 1, 1, 1]

2. **Triangular Kernel** - Higher weights in the middle, tapering at edges
   - Example: [1, 2, 3, 2, 1]

3. **Gaussian Kernel** - Normal distribution shaped weighting
   - Controlled by a sigma parameter that adjusts the bell curve width
   - Excellent frequency characteristics with minimal side lobes

4. **Custom Kernel** - User-defined weight array
   - Entered as comma-separated values
   - Full flexibility for customized filtering characteristics

## Initialization Properties

### Full Window Requirement

CONV requires a minimum of kernel_size data points for a complete calculation. For periods with insufficient data, the implementation handles the initialization by:

1. Using available data points with the corresponding kernel weights
2. Normalizing weights based on available valid (non-NA) values

## Advantages and Disadvantages

### Advantages

- **Ultimate Flexibility**: Create any weight distribution to achieve specific filtering requirements
- **Customizable Frequency Response**: Direct control over spectral properties
- **Adaptable to Different Markets**: Design specialized kernels for different market conditions
- **Educational Value**: Helps understand how different weight distributions affect moving average behavior
- **Unified Implementation**: Can replicate many standard moving averages through appropriate kernel selection
- **Experimental Capabilities**: Enables testing novel weight distributions not available in standard indicators

### Disadvantages

- **Parameter Complexity**: Requires understanding of convolution and filter design principles
- **Higher Cognitive Load**: More parameters to consider compared to standard moving averages
- **Potential Over-optimization**: Easy to create kernels that fit historical data but don't generalize well
- **Performance Cost**: Slightly higher computational requirements than hardcoded implementations
- **Validation Needs**: Custom kernels require validation to ensure desired filtering characteristics
