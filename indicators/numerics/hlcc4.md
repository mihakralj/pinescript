# HLCC4 - Hlcc4


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HLCC4 addresses this by implementing `Calculates the weighted close price with double weight on close` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the weighted close price with double weight on close`

### Parameters

| Parameter | Purpose |
|---|---|
| `h` | High price series |
| `l` | Low price series |
| `c` | Close price series |

### Returns

- float The weighted close (high + low + close × 2) * 0.25

## Runtime profile

- Declared optimization: Uses multiplication instead of division for performance
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

- Source code: `indicators/numerics/hlcc4.pine`
- Documentation file: `indicators/numerics/hlcc4.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/hlcc4.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/hlcc4.md
