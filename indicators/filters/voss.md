# VOSS - Voss


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. VOSS addresses this by implementing `Ehlers Voss Predictive Filter — negative group delay bandpass predictor` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Ehlers Voss Predictive Filter — negative group delay bandpass predictor`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to filter |
| `period` | Primary cycle period (bars) |
| `predict` | Prediction bars (negative delay amount) |
| `bandwidth` | Bandpass tolerance (fraction of period) |

### Returns

- [filt, voss] — bandpass output and predictive filter output

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_predict` | `input.int` | default: `3`, label: "Predict" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Two-pole BPF + weighted feedback predictor, O(Order) per bar
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

- Source code: `indicators/filters/voss.pine`
- Documentation file: `indicators/filters/voss.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/voss.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/voss.md
