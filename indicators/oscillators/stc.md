# STC - Stc


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. STC addresses this by implementing `Calculates the Schaff Trend Cycle (STC) indicator` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Schaff Trend Cycle (STC) indicator`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Input price series |
| `cycleLength` | Main cycle length parameter for lookback periods |
| `fastLength` | Period for fast EMA calculation |
| `slowLength` | Period for slow EMA calculation |
| `smoothingType` | Type of smoothing (0:none, 1:ema, 2:sigmoid, 3:digital) |

### Returns

- Smoothed STC value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_cycleLength` | `input.int` | default: `12`, label: "Cycle Length" |
| `i_fastLength` | `input.int` | default: `26`, label: "Fast Length" |
| `i_slowLength` | `input.int` | default: `50`, label: "Slow Length" |
| `i_smoothingType` | `input.int` | default: `2`, label: "Smoothing" |

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

- Source code: `indicators/oscillators/stc.pine`
- Documentation file: `indicators/oscillators/stc.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/stc.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/stc.md
