# MPE - Mpe


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MPE addresses this by implementing `Calculates Mean Percentage Error between two sources using SMA for averaging` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Mean Percentage Error between two sources using SMA for averaging`

### Parameters

| Parameter | Purpose |
|---|---|
| `source1` | First series to compare (actual) |
| `source2` | Second series to compare (predicted) |
| `period` | Lookback period for error averaging |

### Returns

- MPE value averaged over the specified period using SMA

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source1` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `100`, label: "Period" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/errors/mpe.pine`
- Documentation file: `indicators/errors/mpe.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/errors/mpe.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/errors/mpe.md
