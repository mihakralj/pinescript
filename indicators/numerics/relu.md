# ReLU: Rectified Linear Unit

[Pine Script Implementation of ReLU](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/relu.pine)

## Overview and Purpose

The Rectified Linear Unit (ReLU) is an activation function commonly used in neural networks and other machine learning models. Its primary purpose is to introduce non-linearity into a model. When applied to a financial time series or an indicator, ReLU transforms the data by outputting the input value directly if it is positive, and outputting zero if the input value is negative or zero.

This transformation can be useful for:
*   Highlighting positive regimes or signals while nullifying negative ones.
*   Creating one-sided indicators (e.g., focusing only on upward momentum).
*   Preprocessing data for machine learning models that expect non-negative inputs or benefit from ReLU's properties.

## Core Concepts

*   **Activation Function:** A function that determines the output of a node given an input or set of inputs. ReLU is one of the simplest and most effective activation functions.
*   **Non-linearity:** ReLU introduces non-linearity because its response is not a straight line across its entire domain (it's zero for x ≤ 0 and x for x > 0).
*   **Sparsity:** By outputting zero for negative inputs, ReLU can lead to sparse activations in neural networks, which can be computationally efficient. In a time series context, it means periods with negative values in the source series are "turned off."

## Common Settings and Parameters

| Parameter | Default | Function                                      | When to Adjust                                                                                                |
| :-------- | :------ | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| Source    | Close   | Data point or series for ReLU transformation. | Can be any series, such as price, returns, momentum, or another indicator output.                             |

**Pro Tip:** Applying ReLU to an oscillator can effectively isolate its positive phases. For example, `relu(rsi(close, 14) - 50)` would show values only when RSI is above 50, and zero otherwise, highlighting bullish momentum relative to the 50-level.

## Calculation and Mathematical Foundation

**Simplified explanation:**
If the input number is positive, ReLU gives you that number back. If the input number is negative or zero, ReLU gives you zero.

**Technical formula:**

ReLU(x) = max(0, x)

Where:
*   `x` is the input value (from the `Source` series).

> 🔍 **Technical Note:** The core `relu(series float src)` function in Pine Script is straightforward, implemented as `math.max(0, src)`. The accompanying indicator script (`relu.pine`) demonstrates a practical application by calculating two series:
> 1. `reluUp = relu(i_source - ta.sma(i_source, 20))`: This captures the positive deviations of the source from its 20-period SMA.
> 2. `reluDn = -relu(ta.sma(i_source, 20) - i_source)`: This captures the negative deviations (as positive values, then negated) of the source from its 20-period SMA.
> These two series are then plotted, effectively showing upward and downward "energy" or divergence from the moving average, with periods of no significant deviation (or movement towards the average) being zeroed out by the ReLU function.

## Interpretation Details

*   **Output > 0:** The input `Source` value was positive, and the ReLU output is equal to that `Source` value.
*   **Output = 0:** The input `Source` value was negative or zero.

When applied to financial data:
*   If `Source` is price change: ReLU will show positive price changes and zero for negative or no change.
*   If `Source` is an oscillator centered around zero (e.g., MACD histogram): ReLU will show only the positive values of the oscillator.

## Limitations and Considerations

*   **Dying ReLU Problem (Neural Networks):** In deep neural networks, if a neuron gets stuck outputting zero (e.g., due to a large negative bias or a large gradient update), it may never activate again. This is less of a direct concern when applying ReLU as a simple transformation to a time series but is a key consideration in its original context.
*   **Information Loss:** By zeroing out negative values, information contained in those negative values is lost. This may or may not be desirable depending on the application.
*   **Non-Zero Centered:** The output of ReLU is always non-negative, which can sometimes be an issue for subsequent processing layers in neural networks that expect zero-centered inputs.
*   **No Upper Bound:** Unlike sigmoid or tanh functions, ReLU does not saturate at high positive values.

## References

*   Nair, V., & Hinton, G. E. (2010). Rectified linear units improve restricted boltzmann machines. *Proceedings of the 27th International Conference on Machine Learning (ICML-10)*, 807-814.
*   Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. (Chapter 6: Deep Feedforward Networks)
