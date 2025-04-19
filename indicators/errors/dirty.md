# Dirty Data Injection

Injects NA (Not Available) values into a data series at regular intervals. This indicator is useful for testing indicator robustness against missing data points and data gaps.

## Inputs

- `interval` (default: 10) - Frequency of NA value injections. Every nth bar will be replaced with NA.

## Calculation

The indicator:
1. Sets the first bar to NA
2. Injects NA values every nth bar based on the interval input
3. Plots the resulting series with purple circles to highlight missing data points

## References

No external references - this is a utility indicator for testing purposes.
