# AOBV - Aobv


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. AOBV addresses this by implementing `Computes AOBV Fast and Slow from OBV using custom EMA calculations without helper functions.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Computes AOBV Fast and Slow from OBV using custom EMA calculations without helper functions.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | (series float) Price source. |
| `vol` | (series float) Volume data. |

### Returns

- ([float, float]) Tuple with AOBV Fast and AOBV Slow values.

## Runtime profile

- Declared optimization: Beta precomputation for EMA warmup compensation
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

- Source code: `indicators/volume/aobv.pine`
- Documentation file: `indicators/volume/aobv.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/aobv.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/aobv.md
