# ULTOSC - Ultosc


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ULTOSC addresses this by implementing `Calculates the Ultimate Oscillator using three weighted time periods` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Ultimate Oscillator using three weighted time periods`

### Parameters

| Parameter | Purpose |
|---|---|
| `fastPeriod` | Short-term period for momentum calculation |
| `mediumPeriod` | Medium-term period for momentum calculation |
| `slowPeriod` | Long-term period for momentum calculation |
| `fastWeight` | Weight applied to fast period calculation |
| `mediumWeight` | Weight applied to medium period calculation |
| `slowWeight` | Weight applied to slow period calculation |

### Returns

- Ultimate Oscillator value (0-100 scale)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_fastPeriod` | `input.int` | default: `7`, label: "Fast Period" |
| `i_mediumPeriod` | `input.int` | default: `14`, label: "Medium Period" |
| `i_slowPeriod` | `input.int` | default: `28`, label: "Slow Period" |
| `i_fastWeight` | `input.float` | default: `4.0`, label: "Fast Weight" |
| `i_mediumWeight` | `input.float` | default: `2.0`, label: "Medium Weight" |
| `i_slowWeight` | `input.float` | default: `1.0`, label: "Slow Weight" |

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

- Source code: `indicators/oscillators/ultosc.pine`
- Documentation file: `indicators/oscillators/ultosc.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/ultosc.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/ultosc.md
