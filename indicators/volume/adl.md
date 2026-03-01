# ADL - Adl


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ADL addresses this by implementing `Calculates the Accumulation/Distribution Line (ADL), a volume-based indicator that measures money flow into and out of a security` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Accumulation/Distribution Line (ADL), a volume-based indicator that measures money flow into and out of a security`

### Parameters

| Parameter | Purpose |
|---|---|
| `src_high` | The high price (default: built-in high) |
| `src_low` | The low price (default: built-in low) |
| `src_close` | The close price (default: built-in close) |
| `src_vol` | The volume (default: built-in volume) |

### Returns

- The cumulative ADL value representing buying/selling pressure

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

- Source code: `indicators/volume/adl.pine`
- Documentation file: `indicators/volume/adl.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/adl.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/adl.md
