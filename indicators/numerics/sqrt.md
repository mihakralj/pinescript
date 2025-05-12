# Square Root Transformation (SQRT)

The SQRT indicator applies a square root transformation to the input series. This transformation is useful for reducing right-skewed data and compressing the range of large values while maintaining the order of the original data.

## Formula

```
SQRT(x) = √x  where x ≥ 0
```

The square root function maps non-negative input values to non-negative output values, creating a concave-down curve that grows more slowly than linear functions.

## Features

- Maps non-negative values to their square roots
- Compresses the range of large values
- Useful for reducing right-skewed distributions
- Returns `na` for negative input values
- Preserves zero values and relative ordering

## Parameters

| Name   | Type         | Description |
|--------|--------------|-------------|
| source | series float | Input series to transform. Must be non-negative. |

## Returns

series float - The square root transformed series. Returns `na` for negative input values.

## Example

```pinescript
//@version=6
indicator("SQRT Example")
sqrtPrice = sqrt(close)
plot(sqrtPrice)
