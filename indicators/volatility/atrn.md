# ATRN - Atrn


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ATRN addresses this by implementing `Calculates the Average True Range Normalized (ATRN) relative to its maximum value over a longer period.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Average True Range Normalized (ATRN) relative to its maximum value over a longer period.`

### Parameters

| Parameter | Purpose |
|---|---|
| `length` | The period length for the ATR calculation. The highest uses a length of 10 * length. |

### Returns

- The ATRN value, normalized relative to its maximum over the longer period.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `14`, label: "Length" |

## Runtime profile

- Declared optimization: Beta precomputation for RMA warmup compensation
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

- Source code: `indicators/volatility/atrn.pine`
- Documentation file: `indicators/volatility/atrn.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/atrn.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/atrn.md
