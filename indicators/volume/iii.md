# III - Iii


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. III addresses this by implementing `Calculates Intraday Intensity Index` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Intraday Intensity Index`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Smoothing period for the intensity index |
| `cumulative` | Whether to accumulate intensity values |
| `h` | High price series |
| `l` | Low price series |
| `c` | Close price series |
| `vol` | Volume series |

### Returns

- Smoothed or raw intensity value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `period` | `input.int` | default: `14`, label: "Period" |
| `cumulative` | `input.bool` | default: `false`, label: "Cumulative Mode" |

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

- Source code: `indicators/volume/iii.pine`
- Documentation file: `indicators/volume/iii.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/iii.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/iii.md
