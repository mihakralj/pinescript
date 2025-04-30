# LOG: Logarithmic Transformation

[Pine Script Implementation of LOG](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/log.pine)

## Overview and Purpose

The Logarithmic Transformation indicator applies the natural logarithm (ln) function to price data, creating a normalized representation that emphasizes percentage changes rather than absolute price movements. This transformation is particularly valuable for analyzing securities with wide price ranges, long histories of exponential growth, or during periods of high volatility. By compressing the scale of price data, logarithmic transformation helps visualize long-term trends more clearly while minimizing the visual impact of volatile price swings in high-value regions.

The implementation provided offers a clean, efficient way to apply logarithmic scaling to any data series, with proper handling of edge cases such as zero or negative values. This transformation can be used as a preprocessing step for other technical indicators or as a standalone visualization tool to gain alternative perspectives on price behavior.

## Core Concepts

* **Scale compression:** Converts multiplicative relationships into additive ones, making equal percentage changes appear as equal absolute distances
* **Visual normalization:** Reduces the visual dominance of recent price movements in long-term uptrends
* **Percentage emphasis:** Highlights relative changes rather than absolute price movements
* **Domain transformation:** Maps values from (0, ∞) to (-∞, ∞), creating a more symmetric distribution for positively skewed data

Logarithmic transformation is especially useful in financial analysis because markets often exhibit exponential growth over long periods, while traders and investors typically think in terms of percentage returns rather than absolute price changes. This transformation aligns the visual representation with the mental model most market participants use when evaluating performance.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | Close | Price data to transform | Change to analyze different aspects of price action (e.g., volume for log-volume analysis) |

**Pro Tip:** For securities with extreme price ranges (like Bitcoin or certain tech stocks), applying a log transformation before calculating other technical indicators can help normalize their behavior and make their signals more consistent across different price scales.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The logarithmic transformation applies the natural logarithm function to each value in the source series, effectively converting multiplicative patterns into additive ones.

**Technical formula:**

For each value x in the source series:
y = ln(x)

Where:
- ln is the natural logarithm function (base e)
- x must be positive (x > 0)

> 🔍 **Technical Note:** The implementation includes proper handling for negative or zero values, returning NA (Not Available) in these cases to prevent invalid calculations. This approach ensures that the transformation remains mathematically sound while clearly indicating where the domain constraints of the logarithm function are violated.

## Interpretation Details

Logarithmic transformation provides several analytical insights:

* **Equal visual distances for equal percentage changes:** A 10% increase appears the same size regardless of the absolute price level
* **Trend linearity:** Exponential growth appears as a straight line, making trend identification simpler
* **Comparative analysis:** Easier visual comparison of securities with different price scales
* **Pattern recognition:** Some chart patterns become more apparent on logarithmically scaled charts
* **Volatility normalization:** Dampens the visual impact of volatility at higher price levels
* **Long-term perspective:** Provides better visibility of historical price action in long-term uptrends

## Limitations and Considerations

* **Domain restriction:** Cannot process zero or negative values, requiring special handling for these cases
* **Scale warping:** Compresses higher values while expanding lower values, which may obscure some patterns
* **Reversibility concerns:** Converting back from log space requires careful handling to avoid precision loss
* **Interpretation adjustments:** Linear thinking must be adjusted when analyzing logarithmic charts
* **Zero problem:** Cannot represent zero directly, creating discontinuities near zero
* **Fixed ratio emphasis:** Equal distances represent equal ratios, which may not always be the most relevant measure
* **Cognitive burden:** Requires mental conversion to understand absolute magnitudes

## References

* Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.
* Box, G. E. P., & Cox, D. R. (1964). An analysis of transformations. Journal of the Royal Statistical Society, Series B, 26(2), 211-252.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Mandelbrot, B. (1963). The variation of certain speculative prices. Journal of Business, 36, 394-419.
