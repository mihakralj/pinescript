# MACD - Macd


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MACD addresses this by implementing `Calculates MACD with fast and slow EMAs and signal line` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates MACD with fast and slow EMAs and signal line`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Source series to calculate MACD from |
| `fast_length` | Period for fast EMA |
| `slow_length` | Period for slow EMA |
| `signal_length` | Period for signal line EMA |

### Returns

- Tuple [macd, signal, histogram] values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_fast` | `input.int` | default: `12`, label: "Fast Length" |
| `i_slow` | `input.int` | default: `26`, label: "Slow Length" |
| `i_signal` | `input.int` | default: `9`, label: "Signal Length" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: for performance and dirty data with embedded EMA calculations
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

- Source code: `indicators/momentum/macd.pine`
- Documentation file: `indicators/momentum/macd.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/macd.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/macd.md
