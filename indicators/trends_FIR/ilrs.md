# ILRS - Ilrs


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ILRS addresses this by implementing `Computes the Integral of Linear Regression Slope — cumulative sum of the` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Computes the Integral of Linear Regression Slope — cumulative sum of the`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to analyze |
| `period` | Lookback window for slope calculation (>= 2) |

### Returns

- Cumulative integral of the rolling linear regression slope

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `src` | `input.source` | default: `close`, label: "Source" |
| `per` | `input.int` | default: `14`, label: "Period" |

## Runtime profile

- Declared optimization: O(period) per bar for slope via circular buffer accumulation
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

- Source code: `indicators/trends_FIR/ilrs.pine`
- Documentation file: `indicators/trends_FIR/ilrs.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/ilrs.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/ilrs.md
