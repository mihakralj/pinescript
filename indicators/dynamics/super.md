# SUPER - Super


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SUPER addresses this by implementing `Calculates SuperTrend using ATR-based dynamic support/resistance` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates SuperTrend using ATR-based dynamic support/resistance`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Price series for calculation (typically hlc3 or close) |
| `atr_period` | Lookback period for ATR calculation |
| `multiplier` | Multiplier applied to ATR for band calculation |

### Returns

- Tuple [supertrend, direction] where direction is 1 (bullish) or -1 (bearish)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_atr_period` | `input.int` | default: `10`, label: "ATR Period" |
| `i_multiplier` | `input.float` | default: `3.0`, label: "Multiplier" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: O(1) with proper warmup handling
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

- Source code: `indicators/dynamics/super.pine`
- Documentation file: `indicators/dynamics/super.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/super.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/super.md
