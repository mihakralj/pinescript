# KDJ - Kdj


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. KDJ addresses this by implementing `Calculates KDJ (K, D, J) lines - enhanced Stochastic Oscillator` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates KDJ (K, D, J) lines - enhanced Stochastic Oscillator`

### Parameters

| Parameter | Purpose |
|---|---|
| `high` | Series of high prices |
| `low` | Series of low prices |
| `close` | Series of close prices |
| `length` | Lookback period for highest/lowest calculation |
| `signal` | Smoothing period for K and D lines |

### Returns

- Tuple [K line, D line, J line]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `9`, label: "Length" |
| `i_signal` | `input.int` | default: `3`, label: "Signal" |

## Runtime profile

- Declared optimization: Uses Wilder's RMA smoothing and deque min/max for highest/lowest, O(n) amortized
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `length`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/oscillators/kdj.pine`
- Documentation file: `indicators/oscillators/kdj.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/kdj.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/kdj.md
