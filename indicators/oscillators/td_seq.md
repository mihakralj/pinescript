# TD_SEQ - Td Seq


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. TD_SEQ addresses this by implementing `Calculates TD Sequential — Tom DeMark's exhaustion counting system` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates TD Sequential — Tom DeMark's exhaustion counting system`

### Parameters

| Parameter | Purpose |
|---|---|
| `comparePeriod` | Lookback for setup comparison (close vs close[comparePeriod]) |

### Returns

- [setupCount, countdownCount] signed setup (1-9) and countdown (1-13) values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_comparePeriod` | `input.int` | default: `4`, label: "Compare Period" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/oscillators/td_seq.pine`
- Documentation file: `indicators/oscillators/td_seq.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/td_seq.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/td_seq.md
