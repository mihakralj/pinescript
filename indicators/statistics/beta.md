# BETA - Beta


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BETA addresses this by implementing `Calculates the financial Beta indicator comparing src1 volatility to src2` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the financial Beta indicator comparing src1 volatility to src2`

### Parameters

| Parameter | Purpose |
|---|---|
| `src1` | series float Series to analyze |
| `src2` | series float src2 series to compare against |
| `period` | simple int Lookback period for calculation |

### Returns

- float Beta value showing src1 volatility relative to src2

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_symbol` | `input.symbol` | default: `"SPY"`, label: "SPY" |
| `i_period` | `input.int` | default: `14`, label: "Period" |
| `i_src1` | `input.source` | default: `close`, label: "src1" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/statistics/beta.pine`
- Documentation file: `indicators/statistics/beta.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/beta.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/beta.md
