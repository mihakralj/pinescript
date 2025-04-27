# ALMA: Arnaud Legoux Moving Average

[Pine Script Implementation of ALMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/alma.pine)

## Overview and Purpose

The Arnaud Legoux Moving Average (ALMA) is a technical indicator that uses Gaussian distribution principles to reduce lag while maintaining effective noise filtering. Developed by Arnaud Legoux and Jean-Charles Doux in 2009, ALMA was introduced in their paper "Moving Average: A Gaussian Approach for Financial Applications." The indicator addresses a fundamental challenge in technical analysis: balancing smoothness with responsiveness. Unlike conventional moving averages, ALMA applies a Gaussian distribution curve to weight price data, with the ability to position this curve asymmetrically to emphasize more recent prices.

## Core Concepts

* **Gaussian weighting:** ALMA uses a bell curve to assign weights to price points, providing natural filtering properties that reduce noise while preserving important price signals
* **Asymmetric window placement:** The Gaussian curve can be positioned off-center within the data window to reduce lag, with the peak typically placed toward recent prices
* **Parameter flexibility:** Offers independent control of smoothness (sigma) and lag reduction (offset), allowing customization for different market conditions

The core innovation of ALMA is its application of signal processing principles to financial data. By implementing a Gaussian distribution with adjustable positioning, ALMA achieves better noise reduction with less lag than traditional moving averages of similar length. The shape and position of the weighting curve can be fine-tuned through two key parameters that work independently.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 9 | Controls the lookback period | Increase for smoother signals, decrease for more responsiveness |
| Offset | 0.85 | Positions the Gaussian curve peak (0-1) | Higher values (closer to 1) reduce lag but may increase noise |
| Sigma | 6 | Controls the width of the Gaussian curve | Lower values create sharper filters, higher values create smoother curves |

**Pro Tip:** Start with the default parameters (9, 0.85, 6) and then adjust offset first - values above 0.85 emphasize recent price action, while lower values provide more smoothing with increased lag.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ALMA creates a weighted average of prices where the weights follow a bell curve shape. This curve can be shifted toward recent prices and made narrower or wider. By controlling the curve's position and width, ALMA can reduce lag while still filtering out market noise effectively.

**Technical formula:**
1. Weight[i] = exp(-(i - m)² / (2 × s²))
2. m = offset × (period - 1)
3. s = period / sigma
4. ALMA = Σ(Price[i] × Weight[i]) / Σ(Weight[i])

> 🔍 **Technical Note:** The offset parameter determines where the Gaussian peak is positioned. An offset of 1.0 places maximum weight on the most recent price, while 0.0 places it on the oldest price. The default 0.85 balances responsiveness with smoothness.

## Interpretation Details

ALMA can be used in various ways:

* **Trend identification:** The direction of ALMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and ALMA generate trade signals similar to other moving averages
* **Support/resistance levels:** ALMA can act as dynamic support in uptrends and resistance in downtrends
* **Trend strength assessment:** The angle of the ALMA line and its distance from price can indicate trend strength
* **Filter optimization:** Adjusting offset and sigma allows for customization to specific trading styles and market conditions

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Parameter sensitivity:** Performance highly dependent on parameter selection
* **Complexity:** More complex to understand and optimize than simple moving averages
* **Computational demands:** More intensive calculations than traditional moving averages
* **Complementary tools:** Best used alongside momentum indicators and volume analysis for confirmation

## References

* Legoux, A. and Doux, J. (2009). "Moving Average: A Gaussian Approach for Financial Applications." International Conference on Financial Engineering
* [TradingView - ALMA Indicator](https://www.tradingview.com/script/vStKO5HK-ALMA-Arnaud-Legoux-Moving-Average/)

