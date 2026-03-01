# ADOSC - Adosc


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ADOSC addresses this by implementing `Calculates the Chaikin Accumulation/Distribution Oscillator (ADOSC), a momentum indicator derived from the ADL` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Chaikin Accumulation/Distribution Oscillator (ADOSC), a momentum indicator derived from the ADL`

### Parameters

| Parameter | Purpose |
|---|---|
| `shortPeriod` | (simple int) Length of the short-term EMA applied to the ADL |
| `longPeriod` | (simple int) Length of the long-term EMA applied to the ADL |

### Returns

- (float) The ADOSC value for the current bar (difference between short and long EMAs of ADL)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `shortPeriod` | `input.int` | default: `3`, label: "Short Period" |
| `longPeriod` | `input.int` | default: `10`, label: "Long Period" |

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

- Source code: `indicators/volume/adosc.pine`
- Documentation file: `indicators/volume/adosc.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/adosc.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/adosc.md
