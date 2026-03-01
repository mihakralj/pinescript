# GHLA - Ghla


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. GHLA addresses this by implementing `Calculates Gann High-Low Activator using SMA of Highs/Lows with trend-state switching` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Gann High-Low Activator using SMA of Highs/Lows with trend-state switching`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Lookback period for SMA calculation (Krausz default: 3) |

### Returns

- Tuple [activator, trend] where trend is 1 (bullish) or -1 (bearish)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `3`, label: "Period" |

## Runtime profile

- Declared optimization: O(period) SMA via ta.sma built-in; O(1) state transition with hysteresis
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

- Source code: `indicators/dynamics/ghla.pine`
- Documentation file: `indicators/dynamics/ghla.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/ghla.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/ghla.md
