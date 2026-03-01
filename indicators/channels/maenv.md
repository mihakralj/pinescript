# MAENV - Maenv


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MAE addresses this by implementing `Calculates MA Envelope bands using a fixed percentage` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates MA Envelope bands using a fixed percentage`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate moving average from |
| `length` | Lookback period for MA calculation |
| `percentage` | Distance of bands from MA as percentage |
| `ma_type` | Type of moving average (0:SMA, 1:EMA, 2:WMA) |

### Returns

- tuple with [middle, upper, lower] band values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_length` | `input.int` | default: `20`, label: "Length" |
| `i_percentage` | `input.float` | default: `1.0`, label: "Percentage" |
| `i_ma_type` | `input.int` | default: `1`, label: "MA Type" |

## Runtime profile

- Declared optimization: SMA uses circular buffer O(1), EMA uses warmup O(1), WMA is O(n)
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

- Source code: `indicators/channels/maenv.pine`
- Documentation file: `indicators/channels/maenv.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/maenv.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/maenv.md
