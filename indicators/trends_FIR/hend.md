# HEND - Hend


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HEND addresses this by implementing `Computes Henderson Moving Average — a symmetric FIR filter that preserves` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Computes Henderson Moving Average — a symmetric FIR filter that preserves`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to smooth |
| `period` | Lookback window (must be odd >= 5) |

### Returns

- Henderson-weighted moving average

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `src` | `input.source` | default: `close`, label: "Source" |
| `per` | `input.int` | default: `7`, label: "Period" |

## Runtime profile

- Declared optimization: O(period) per bar for convolution; weights precomputed once
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

- Source code: `indicators/trends_FIR/hend.pine`
- Documentation file: `indicators/trends_FIR/hend.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/hend.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/hend.md
