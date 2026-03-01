# NVI - Nvi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. NVI addresses this by implementing `Calculates Negative Volume Index, tracks price changes on days with lower volume` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Negative Volume Index, tracks price changes on days with lower volume`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Price series to use for calculation |
| `vol` | Volume series |
| `start_value` | Starting value for NVI (typically 100 or 1000) |

### Returns

- float The NVI value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `src` | `input.source` | default: `close`, label: "Price Source" |

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

- Source code: `indicators/volume/nvi.pine`
- Documentation file: `indicators/volume/nvi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/nvi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/nvi.md
