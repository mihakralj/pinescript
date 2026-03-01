# ADR - Adr


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ADR addresses this by implementing `Calculates Average Daily Range with choice of smoothing method` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Average Daily Range with choice of smoothing method`

### Parameters

| Parameter | Purpose |
|---|---|
| `length` | Period for smoothing calculations |
| `method` | Smoothing method (1=SMA, 2=EMA, 3=WMA) |

### Returns

- float ADR value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `14`, label: "Length" |
| `i_method` | `input.int` | default: `1`, label: "Method" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/volatility/adr.pine`
- Documentation file: `indicators/volatility/adr.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/adr.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/adr.md
