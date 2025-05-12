# Exponential Transformation (EXP)

The EXP indicator applies an exponential transformation to the input series. This transformation is useful for exponential growth modeling and reverting logarithmic transformations.

## Formula

```
EXP(x) = e^x
```

The exponential function maps any real number input to a positive real number output, creating a rapidly increasing curve that grows faster than polynomial functions.

## Features

- Maps any real number to a positive real number
- Inverse function of natural logarithm (ln)
- Useful for exponential growth modeling
- Never returns negative values
- Preserves order of input values

## Parameters

| Name   | Type         | Description |
|--------|--------------|-------------|
| source | series float | Input series to transform. Can be any real number. |

## Returns

series float - The exponentially transformed series.

## Example

```pinescript
//@version=6
indicator("EXP Example")
expPrice = math.exp(close)
plot(expPrice)
