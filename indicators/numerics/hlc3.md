# HLC3 - Hlc3


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HLC3 addresses this by implementing `Calculates the typical price as the average of high, low, and close prices` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the typical price as the average of high, low, and close prices`

### Parameters

| Parameter | Purpose |
|---|---|
| `h` | High price series |
| `l` | Low price series |
| `c` | Close price series |

### Returns

- float The typical price (high + low + close) * 0.333333

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

- Source code: `indicators/numerics/hlc3.pine`
- Documentation file: `indicators/numerics/hlc3.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/hlc3.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/hlc3.md
