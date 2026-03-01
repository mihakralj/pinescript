# MOM - Mom


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MOM addresses this by implementing `Calculates price momentum over specified period` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates price momentum over specified period`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Source series to calculate momentum for |
| `len` | Lookback period for momentum calculation |

### Returns

- Momentum value measuring rate of price change

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `10`, label: "Length" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

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

- Source code: `indicators/momentum/mom.pine`
- Documentation file: `indicators/momentum/mom.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/mom.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/mom.md
