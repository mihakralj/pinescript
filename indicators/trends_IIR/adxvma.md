# ADXVMA - Adxvma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ADXVMA addresses this by implementing `Calculates ADXVMA using ADX as adaptive smoothing constant for a variable moving average` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates ADXVMA using ADX as adaptive smoothing constant for a variable moving average`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate ADXVMA from |
| `period` | Length of the ADX calculation period |

### Returns

- ADXVMA value that adapts smoothing based on trend strength measured by ADX

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `14`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: O(1) per bar using Wilder's RMA with warmup compensation for all smoothed components
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `period`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/trends_IIR/adxvma.pine`
- Documentation file: `indicators/trends_IIR/adxvma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/adxvma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/adxvma.md
