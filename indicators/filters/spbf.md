# SPBF - Spbf


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SPBF addresses this by implementing `Ehlers Super Passband Filter — wide-band bandpass via differenced z-transformed EMAs` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Ehlers Super Passband Filter — wide-band bandpass via differenced z-transformed EMAs`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to filter |
| `shortPeriod` | Short EMA period (alpha1 = 5/shortPeriod) |
| `longPeriod` | Long EMA period (alpha2 = 5/longPeriod) |
| `rmsPeriod` | RMS averaging period for trigger envelope |

### Returns

- [pb, rms] — passband oscillator and RMS trigger level

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: O(rmsPeriod) per bar for RMS, O(1) for passband
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

- Source code: `indicators/filters/spbf.pine`
- Documentation file: `indicators/filters/spbf.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/spbf.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/spbf.md
