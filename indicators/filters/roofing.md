# ROOFING - Roofing


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ROOFING addresses this by implementing `Calculates Ehlers Roofing Filter (2-pole HPF → Super Smoother composite)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Ehlers Roofing Filter (2-pole HPF → Super Smoother composite)`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate Roofing Filter from |
| `hpLength` | Cutoff period for the highpass stage (removes trend below this period) |
| `ssLength` | Cutoff period for the super smoother stage (removes noise above this period) |

### Returns

- Bandpass-filtered value oscillating around zero

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_hpLength` | `input.int` | default: `48`, label: "HP Length" |
| `i_ssLength` | `input.int` | default: `10`, label: "SS Length" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses two cascaded 2-pole IIR filters with O(1) complexity per bar
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

- Source code: `indicators/filters/roofing.pine`
- Documentation file: `indicators/filters/roofing.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/roofing.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/roofing.md
