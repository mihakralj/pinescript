# NOTCH - Notch


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. NOTCH addresses this by implementing `Applies a second-order IIR notch filter to remove a specific frequency component` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Applies a second-order IIR notch filter to remove a specific frequency component`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Input series |
| `period` | The period of the cycle to remove (center frequency of the notch) |
| `bandwidth` | The relative bandwidth of the notch (e.g., 0.1 for 10%) |

### Returns

- Filtered series with the specified frequency component attenuated

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `14`, label: "Period to Remove" |
| `i_bandwidth` | `input.float` | default: `0.3`, label: "Relative Bandwidth" |

## Runtime profile

- Declared optimization: Uses 2nd order IIR notch filter with O(1) complexity per bar
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

- Source code: `indicators/filters/notch.pine`
- Documentation file: `indicators/filters/notch.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/notch.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/notch.md
