# EXP: Exponential Transformation

[Pine Script Implementation of EXP](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/exp.pine)

## Overview and Purpose

The Exponential Transformation (EXP) indicator applies the mathematical exponential function to input data series, providing a non-linear transformation that amplifies larger values while compressing smaller ones. This transformation is fundamental in financial modeling for exponential growth processes, volatility modeling, and converting logarithmic returns back to price levels. The exponential function creates a convex mapping that dramatically increases the range of positive input values.

## Core Concepts

*   **Non-Linear Amplification** — Dramatically increases the magnitude of larger positive values
*   **Growth Modeling** — Natural representation of exponential growth processes
*   **Logarithmic Inverse** — Reverses natural logarithm transformations
*   **Positive Range** — Always produces positive output regardless of input sign

Market Applications:
*   **Volatility Modeling** — Converting log-volatility back to volatility levels
*   **Growth Analysis** — Modeling exponential growth in earnings, revenue, or assets
*   **Return Conversion** — Converting log returns to multiplicative price factors

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Source | Close | Input series for transformation | Use log returns, standardized data, or growth rates |
| Domain | (-∞, ∞) | Mathematical domain | Accepts any real number input |
| Output Range | (0, ∞) | Transformed value range | Results always positive |

## Calculation and Mathematical Foundation

**Technical Formula:**

For input value $x \in \mathbb{R}$:
$$\text{EXP}(x) = e^x$$

where $e \approx 2.71828$ is Euler's number.

**Properties of Exponential Transformation:**
- **Domain**: $x \in (-\infty, \infty)$
- **Range**: $y \in (0, \infty)$
- **Monotonicity**: Strictly increasing function
- **Convexity**: Convex function (increasing marginal rate)

**Transformation Effects:**
$$\frac{d}{dx}e^x = e^x$$

The derivative equals the function itself, showing exponential growth rate properties.

**Key Mathematical Relationships:**
- $e^0 = 1$ (neutral transformation point)
- $e^{ln(x)} = x$ (inverse of natural logarithm)
- $e^{x+y} = e^x \cdot e^y$ (multiplicative property)
- $e^{-x} = \frac{1}{e^x}$ (reciprocal relationship)

**Financial Applications:**
For continuously compounded returns $r$:
$$P_t = P_0 \cdot e^{rt}$$

Converting log returns to price multiples:
$$\text{Price Factor} = e^{\ln(\text{return})}$$

> 🔍 **Technical Note:** The exponential transformation is particularly valuable for converting logarithmic scales back to original scales and modeling processes with multiplicative rather than additive growth patterns.

## Interpretation Details

*   **Value Transformation:**
    - Negative values: Compression toward zero (e^(-2) ≈ 0.135)
    - Zero value: Maps to unity (e^0 = 1)
    - Positive values: Exponential amplification (e^2 ≈ 7.389)

*   **Scale Effects:**
    - Small negative inputs → Values between 0 and 1
    - Small positive inputs → Values greater than 1
    - Large positive inputs → Very large exponential growth
    - Large negative inputs → Values approaching zero

*   **Growth Interpretation:**
    - Input represents growth rate or log change
    - Output represents multiplicative factor or level
    - Linear changes in input create multiplicative changes in output

## Applications

*   **Volatility Modeling:**
    - Convert log-volatility estimates to volatility levels
    - Transform GARCH model outputs to standard deviations
    - Create volatility surfaces from log-space parameters

*   **Return Analysis:**
    - Convert log returns to price multiples
    - Transform continuously compounded returns to simple returns
    - Create cumulative return series from log return differences

*   **Growth Modeling:**
    - Model exponential growth in financial metrics
    - Transform growth rates to multiplicative factors
    - Create compound growth projections

## Limitations and Considerations

*   **Numerical Sensitivity:**
    - Large positive inputs can cause numerical overflow
    - Very small negative inputs approach machine precision limits
    - Requires careful input scaling for extreme values

*   **Interpretation Challenges:**
    - Non-linear scale requires careful interpretation
    - Small input changes can create large output changes for positive inputs
    - Output scale may become impractical for large positive inputs

*   **Model Assumptions:**
    - Assumes exponential growth process is appropriate
    - May not be suitable for bounded or cyclical processes
    - Requires understanding of underlying logarithmic relationships

Complementary Transformations:
* Natural logarithm (inverse transformation)
* Power transformations (alternative non-linear mappings)
* Logistic transformation (bounded exponential-like growth)

## References

1. Euler, L. "Introductio in analysin infinitorum." 1748.
2. Hull, J.C. "Options, Futures, and Other Derivatives." Pearson, 2017.
3. Tsay, R.S. "Analysis of Financial Time Series." Wiley, 2010.

### Pine Script™ Implementation

```pinescript
// The MIT License (MIT)
// © mihakralj
//@version=6
indicator("Exponential Transformation (EXP)", shorttitle="EXP", overlay=false)

//@function Applies exponential transformation to input series.
//@doc https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/exp.md
//@param source series float Input series to transform. Can be any real number.
//@returns series float The exponentially transformed series.
exp_transform(series float source) =>
    math.exp(source)

// Inputs
i_source = input.source(close, "Source", tooltip="Input series for exponential transformation. Can be any real number.")

// Calculation
expValue = exp_transform(i_source)

// Plot
plot(expValue, "EXP", color=color.new(color.orange, 0), linewidth=2)

// Optional: Add reference lines for interpretation
hline(1, "Unity Reference (e^0)", color=color.gray, linestyle=hline.style_dashed)
hline(2.71828, "Euler's Number (e^1)", color=color.blue, linestyle=hline.style_dotted)
