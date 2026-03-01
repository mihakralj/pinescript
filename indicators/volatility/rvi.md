# RVI - Rvi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. RVI addresses this by implementing `Calculates the Relative Volatility Index (RVI).` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Relative Volatility Index (RVI).`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | The source series to calculate RVI from. Default is `close`. |
| `stdevLength` | The lookback period for calculating the standard deviation of source prices. Default is 10. |
| `rmaLength` | The lookback period for Wilder's smoothing (RMA) of the upward and downward standard deviations. Default is 14. |

### Returns

- float The Relative Volatility Index value.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_src_rvi` | `input.source` | default: `close`, label: "Source" |
| `i_stdevLength_rvi` | `input.int` | default: `10`, label: "StdDev Length" |
| `i_rmaLength_rvi` | `input.int` | default: `14`, label: "RMA Length (Wilder's Smoothing)" |

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

- Source code: `indicators/volatility/rvi.pine`
- Documentation file: `indicators/volatility/rvi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/rvi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/rvi.md
