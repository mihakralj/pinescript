# SIGMOID: Logistic Function

[Pine Script Implementation of SIGMOID](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/sigmoid.pine)

## Overview and Purpose

The Sigmoid function, specifically the logistic function, is a mathematical function that produces an "S"-shaped curve (a sigmoid curve). It takes any real-valued number and maps it into a value between 0 and 1. This makes it particularly useful for:

*   **Normalization/Scaling:** Transforming unbounded inputs into a fixed [0, 1] range, which can be useful for comparing different indicators or preparing data for machine learning models.
*   **Probability Estimation:** The output can be interpreted as a probability, as it's bounded between 0 and 1.
*   **Activation Functions:** In neural networks, sigmoid functions are often used as activation functions for neurons, introducing non-linearity into the model.
*   **Creating Bounded Oscillators:** Applying the sigmoid function to an unbounded indicator (like momentum) can create a bounded oscillator that fluctuates between 0 and 1. The script uses a dynamic midpoint (200-period SMA of the source) as an example.

## Core Concepts

*   **S-shaped Curve:** The characteristic shape of the logistic function.
*   **Asymptotes:** The function approaches 0 as the input approaches negative infinity and approaches 1 as the input approaches positive infinity.
*   **Midpoint (x0):** The input value at which the sigmoid function outputs 0.5. In this script, `x0` is dynamically calculated as the 200-period Simple Moving Average (SMA) of the source, allowing the inflection point to adapt to the source's recent mean.
*   **Steepness (k):** Controls how quickly the function transitions from 0 to 1. A higher `k` value results in a steeper, more abrupt transition.

## Common Settings and Parameters

| Parameter     | Default                               | Function                                                                 | When to Adjust                                                                                                                                                              |
| :------------ | :------------------------------------ | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source        | Close                                 | Data point or series to be transformed.                                  | Can be any series, such as price, returns, volume, or another indicator output.                                                                                             |
| Steepness (k) | 0.5                                   | Controls the steepness or "gain" of the sigmoid curve.                   | Increase `k` for a sharper transition around the dynamic midpoint. Decrease `k` for a gentler, more spread-out transition. Must be positive.                                   |
| Midpoint (x0) | `ta.sma(Source, 200)` (Not an input)  | The input value at which the sigmoid function outputs 0.5.               | This is not a direct user input in the script. It's dynamically set to the 200-period SMA of the `Source`. To change this, the script code itself would need to be modified. |

**Pro Tip:** The dynamic `Midpoint (x0)` (200-period SMA of `Source`) makes the SIGMOID function adaptive, centering its "0.5 output" around the recent average of the source. The `Steepness (k)` (default 0.5) determines how sensitively the output reacts to deviations from this moving average. A lower `k` provides a smoother output, while a higher `k` makes it more reactive.

## Calculation and Mathematical Foundation

The logistic function is defined as:

S(x) = 1 / (1 + e<sup>-k(x - x0)</sup>)

Where:
*   `x` is the input value (from the `Source` series).
*   `k` is the `Steepness (k)` parameter (default 0.5).
*   `x0` is the dynamic midpoint, calculated as `ta.sma(Source, 200)`.
*   `e` is Euler's number (the base of natural logarithms, approximately 2.71828).

**Breakdown:**
1.  `(x - x0)`: Centers the input around 0 relative to the dynamic midpoint.
2.  `-k * (x - x0)`: Scales by steepness and negates. If `x > x0`, this term becomes negative. If `x < x0`, this term becomes positive.
3.  `math.exp(-k * (x - x0))`: Calculates e raised to the power of the previous result.
    *   If `x` is much larger than `x0`, `exp(...)` approaches 0.
    *   If `x` is much smaller than `x0`, `exp(...)` approaches +∞.
    *   If `x = x0`, `exp(0)` is 1.
4.  `1 + math.exp(...)`: Adds 1 to the exponential term.
5.  `1 / (1 + math.exp(...))`: The reciprocal, which maps the values to the (0, 1) range.
    *   If `exp(...)` → 0, then S(x) → 1 / (1 + 0) = 1.
    *   If `exp(...)` → +∞, then S(x) → 1 / (+∞) = 0.
    *   If `exp(...)` = 1 (when `x = x0`), then S(x) = 1 / (1 + 1) = 0.5.

> 🔍 **Technical Note:** The Pine Script implementation uses `math.exp()` for the exponential function. The `k` parameter allows for flexible adaptation of the sigmoid curve's steepness around the dynamic `x0` midpoint.

## Interpretation Details

*   **Output Range:** The SIGMOID output will always be between 0 and 1 (exclusive of 0 and 1, but approaching them asymptotically).
*   **Midpoint:** When the `Source` input equals the dynamic `Midpoint (x0)` (i.e., the 200-period SMA of the Source), the SIGMOID output will be 0.5.
*   **Saturation:**
    *   As the `Source` input becomes significantly larger than `x0` (relative to `1/k`), the SIGMOID output approaches 1.
    *   As the `Source` input becomes significantly smaller than `x0` (relative to `1/k`), the SIGMOID output approaches 0.
*   **Steepness:**
    *   A higher `Steepness (k)` value means the transition from 0 to 1 around the `Midpoint (x0)` is more abrupt. The function will saturate more quickly.
    *   A lower `k` value (like the default 0.5) results in a smoother, more gradual transition.

## Limitations and Considerations

*   **Vanishing Gradients:** In the context of training neural networks (less relevant for direct indicator use but good to know), sigmoid functions can suffer from the "vanishing gradient" problem in their saturation regions (where output is close to 0 or 1), as the derivative becomes very small.
*   **Not Zero-Centered:** The output is always positive (0 to 1). If a zero-centered output is needed (e.g., -1 to 1), the Hyperbolic Tangent (TANH) function is often preferred, which is a related sigmoid-shaped function.
*   **Parameter Sensitivity (Steepness k):** The choice of `k` is crucial for meaningful output. Poor choices can lead to the function always outputting values very close to 0 or 1, or not capturing the desired sensitivity in the input data relative to its moving average.
*   **Fixed Midpoint Logic:** The midpoint `x0` is hardcoded to be a 200-period SMA. While this makes it adaptive, users cannot change the midpoint logic (e.g., use a different MA type or a fixed value) without modifying the script's code.
*   **Interpretation of "Probability":** While the output is in the [0,1] range, interpreting it directly as a calibrated probability requires careful consideration of the input data and parameter settings.

## References

*   Wikipedia contributors. (2023). *Sigmoid function*. Wikipedia, The Free Encyclopedia.
*   Wikipedia contributors. (2023). *Logistic function*. Wikipedia, The Free Encyclopedia.
*   Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. (Chapter 6: Deep Feedforward Networks, Activation Functions)
