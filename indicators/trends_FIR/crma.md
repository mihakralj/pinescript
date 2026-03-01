# CRMA - Crma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. CRMA addresses this by implementing `Computes Cubic Regression Moving Average — fits a degree-3 polynomial` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Computes Cubic Regression Moving Average — fits a degree-3 polynomial`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to analyze |
| `period` | Lookback window for the cubic regression |

### Returns

- Fitted value at the most recent bar (x = 0)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `14`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: O(period) per bar for accumulating sums; O(1) for solve
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

- Source code: `indicators/trends_FIR/crma.pine`
- Documentation file: `indicators/trends_FIR/crma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/crma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/crma.md
