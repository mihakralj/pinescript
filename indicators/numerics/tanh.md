# TANH: Hyperbolic Tangent

[Pine Script Implementation of TANH](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/tanh.pine)

## Overview and Purpose

The Hyperbolic Tangent (tanh) function is a mathematical activation function that produces an "S"-shaped curve, similar to the logistic sigmoid function, but maps any real-valued number into a value between -1 and 1. This makes it particularly useful for:

*   **Normalization/Scaling:** Transforming unbounded inputs into a fixed [-1, 1] range. This is often preferred over the [0, 1] range of the logistic sigmoid if a zero-centered output is desirable.
*   **Activation Functions:** In neural networks, tanh is a common activation function, especially in hidden layers, as its zero-centered output can help with the learning dynamics of some models.
*   **Creating Bounded Oscillators:** Applying the tanh function to an unbounded indicator can create a bounded oscillator that fluctuates between -1 and 1, with 0 as its natural midpoint. The script uses a dynamic midpoint (200-period SMA of the source) by default.

## Core Concepts

*   **S-shaped Curve:** The characteristic shape of the hyperbolic tangent function.
*   **Asymptotes:** The function approaches -1 as the input approaches negative infinity and approaches 1 as the input approaches positive infinity.
*   **Inflection Point (x0):** The input value at which the tanh function outputs 0. In this script, `x0` is dynamically calculated as the 200-period Simple Moving Average (SMA) of the source, allowing the inflection point to adapt to the source's recent mean.
*   **Steepness (k):** Controls how quickly the function transitions from -1 to 1. A higher `k` value results in a steeper, more abrupt transition around the inflection point.

## Common Settings and Parameters

| Parameter     | Default                               | Function                                                                 | When to Adjust                                                                                                                                                              |
| :------------ | :------------------------------------ | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source        | Close                                 | Data point or series to be transformed.                                  | Can be any series, such as price, returns, volume, or another indicator output.                                                                                             |
| Steepness (k) | 0.5                                   | Controls the steepness or "gain" of the tanh curve.                      | Increase `k` for a sharper transition around the dynamic midpoint. Decrease `k` for a gentler, more spread-out transition. Must be positive (minval set to 0.1 in script).     |
| Midpoint (x0) | `ta.sma(Source, 200)` (Not an input)  | The input value at which the tanh function outputs 0 (inflection point). | This is not a direct user input in the script. It's dynamically set to the 200-period SMA of the `Source`. To change this, the script code itself would need to be modified. |

**Pro Tip:** The dynamic `Midpoint (x0)` (200-period SMA of `Source`) makes the TANH function adaptive, centering its "zero output" around the recent average of the source. The `Steepness (k)` (default 0.5) determines how sensitively the output reacts to deviations from this moving average. A lower `k` provides a smoother output, while a higher `k` makes it more reactive.

## Calculation and Mathematical Foundation

The generalized hyperbolic tangent function used in the script is:

Output = tanh(k * (x - x0))

Where:
*   `x` is the input value (from the `Source` series).
*   `k` is the `Steepness (k)` parameter (default 0.5).
*   `x0` is the dynamic midpoint, calculated as `ta.sma(Source, 200)`.

The standard hyperbolic tangent function itself is defined as:

tanh(y) = (e<sup>y</sup> - e<sup>-y</sup>) / (e<sup>y</sup> + e<sup>-y</sup>)

Where:
*   `y = k * (x - x0)`
*   `e` is Euler's number (the base of natural logarithms, approximately 2.71828).

**Breakdown of tanh(y):**
1.  `exp(y)`: Calculates e<sup>y</sup>.
2.  `exp(-y)`: Calculates e<sup>-y</sup>.
3.  `exp(y) - exp(-y)`: Numerator.
4.  `exp(y) + exp(-y)`: Denominator.
5.  The ratio of these two gives the tanh value.
    *   If `y` is very large positive, `exp(-y)` → 0, so tanh(y) → `exp(y) / exp(y)` = 1.
    *   If `y` is very large negative (e.g., `y = -z` where `z` is large positive), `exp(y)` → 0, so tanh(y) → `-exp(-y) / exp(-y)` = -1.
    *   If `y = 0` (i.e., `x = x0`), tanh(0) = (e<sup>0</sup> - e<sup>0</sup>) / (e<sup>0</sup> + e<sup>0</sup>) = (1 - 1) / (1 + 1) = 0 / 2 = 0.

> 🔍 **Technical Note:** The Pine Script implementation calculates `tanh` using `math.exp()` as Pine Script does not have a built-in `math.tanh()` function. The `k` parameter allows for flexible adaptation of the tanh curve's steepness around the dynamic `x0` midpoint.

## Interpretation Details

*   **Output Range:** The TANH output will always be between -1 and 1 (exclusive, but approaching them asymptotically).
*   **Inflection Point:** When the `Source` input equals the dynamic `Midpoint (x0)` (i.e., the 200-period SMA of the Source), the TANH output will be 0.
*   **Saturation:**
    *   As the `Source` input becomes significantly larger than `x0` (relative to `1/k`), the TANH output approaches 1.
    *   As the `Source` input becomes significantly smaller than `x0` (relative to `1/k`), the TANH output approaches -1.
*   **Steepness:**
    *   A higher `Steepness (k)` value means the transition from -1 to 1 around the `Midpoint (x0)` is more abrupt. The function will saturate more quickly.
    *   A lower `k` value (like the default 0.5) results in a smoother, more gradual transition.

## Limitations and Considerations

*   **Vanishing Gradients:** Similar to the logistic sigmoid, tanh can suffer from vanishing gradients in its saturation regions when used in training neural networks. However, its derivatives are generally larger than sigmoid's.
*   **Parameter Sensitivity (Steepness k):** The choice of `k` is crucial for meaningful output. Poor choices can lead to the function always outputting values very close to -1 or 1, or not capturing the desired sensitivity in the input data relative to its moving average.
*   **Fixed Midpoint Logic:** The midpoint `x0` is hardcoded to be a 200-period SMA. While this makes it adaptive, users cannot change the midpoint logic (e.g., use a different MA type or a fixed value) without modifying the script's code.

## References

*   Wikipedia contributors. (2023). *Hyperbolic functions*. Wikipedia, The Free Encyclopedia. (Specifically, Hyperbolic Tangent)
*   Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. (Chapter 6: Deep Feedforward Networks, Activation Functions)
