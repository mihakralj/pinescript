# ADXR - Adxr


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ADXR addresses this by implementing `Calculates ADX Rating (ADXR) using current and historical ADX values` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates ADX Rating (ADXR) using current and historical ADX values`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Number of bars used in ADX calculation |
| `rating_period` | Number of bars between current and historical ADX |

### Returns

- tuple of ADXR value, ADX value, +DI, -DI

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `14`, label: "ADX Period" |
| `i_rating_period` | `input.int` | default: `14`, label: "Rating Period" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/dynamics/adxr.pine`
- Documentation file: `indicators/dynamics/adxr.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/adxr.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/adxr.md
