# TVI - Tvi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. TVI addresses this by implementing `Calculates Trade Volume Index` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Trade Volume Index`

### Parameters

| Parameter | Purpose |
|---|---|
| `price` | Price series for tick direction analysis |
| `vol` | Volume series for weighting |
| `min_tick` | Minimum price movement to register direction change |

### Returns

- Trade Volume Index value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_price_source` | `input.source` | default: `close`, label: "Price Field" |
| `i_min_tick` | `input.float` | default: `0.125`, label: "Min. Move" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/volume/tvi.pine`
- Documentation file: `indicators/volume/tvi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/tvi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/tvi.md
