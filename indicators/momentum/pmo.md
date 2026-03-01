# PMO - Pmo


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PMO addresses this by implementing `Calculates Price Momentum Oscillator using double-smoothed ROC` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Price Momentum Oscillator using double-smoothed ROC`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Source series to calculate PMO for |
| `roc_len` | Lookback period for ROC calculation |
| `smooth1_len` | First smoothing period |
| `smooth2_len` | Second smoothing period |

### Returns

- PMO value measuring smoothed momentum

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_roc_len` | `input.int` | default: `35`, label: "ROC Length" |
| `i_smooth1_len` | `input.int` | default: `20`, label: "First Smoothing Length" |
| `i_smooth2_len` | `input.int` | default: `10`, label: "Second Smoothing Length" |
| `i_signal_len` | `input.int` | default: `10`, label: "Signal Line Length" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `lookback parameter`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/momentum/pmo.pine`
- Documentation file: `indicators/momentum/pmo.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/pmo.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/pmo.md
