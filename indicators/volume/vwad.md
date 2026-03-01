# VWAD - Vwad


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. VWAD addresses this by implementing `Calculates VWAD using volume weighting for enhanced sensitivity` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates VWAD using volume weighting for enhanced sensitivity`

### Parameters

| Parameter | Purpose |
|---|---|
| `src_high` | High price series |
| `src_low` | Low price series |
| `src_close` | Close price series |
| `src_vol` | Volume series |
| `period` | Lookback period for volume weighting |

### Returns

- VWAD value representing volume-weighted accumulation/distribution

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Volume Weight Period" |

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

- Source code: `indicators/volume/vwad.pine`
- Documentation file: `indicators/volume/vwad.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/vwad.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/vwad.md
