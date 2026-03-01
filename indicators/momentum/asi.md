# ASI - Asi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ASI addresses this by implementing `Computes Wilder's Swing Index for a single bar.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Computes Wilder's Swing Index for a single bar.`

### Parameters

| Parameter | Purpose |
|---|---|
| `high` | Current bar high price |
| `low` | Current bar low price |
| `close` | Current bar close price |
| `open` | Current bar open price |
| `prevHigh` | Previous bar high price |
| `prevLow` | Previous bar low price (unused in SI formula but kept for completeness) |
| `prevClose` | Previous bar close price |
| `prevOpen` | Previous bar open price |
| `limitMove` | Maximum daily limit move value (T parameter) |
| `i_limitMove` | Limit move value T — the maximum daily price movement (must be > 0) |

### Returns

- Single-bar Swing Index value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_limitMove` | `input.float` | default: `3.0`, label: "Limit Move" |

## Runtime profile

- Declared optimization: O(1) per bar — no buffer allocation, pure arithmetic
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

- Source code: `indicators/momentum/asi.pine`
- Documentation file: `indicators/momentum/asi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/asi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/asi.md
