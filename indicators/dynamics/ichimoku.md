# ICHIMOKU - Ichimoku


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ICHIMOKU addresses this by implementing `Calculate Ichimoku Cloud components` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculate Ichimoku Cloud components`

### Parameters

| Parameter | Purpose |
|---|---|
| `tenkan_period` | Tenkan-sen (Conversion Line) period |
| `kijun_period` | Kijun-sen (Base Line) period |
| `senkou_b_period` | Senkou Span B (Leading Span B) period |

### Returns

- [tenkan, kijun, senkou_a, senkou_b, chikou] Five Ichimoku components

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_tenkan` | `input.int` | default: `9`, label: "Tenkan Period" |
| `i_kijun` | `input.int` | default: `26`, label: "Kijun Period" |
| `i_senkou_b` | `input.int` | default: `52`, label: "Senkou B Period" |
| `i_displacement` | `input.int` | default: `26`, label: "Displacement" |

## Runtime profile

- Declared optimization: Single-pass calculation of all three Donchian midpoints
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

- Source code: `indicators/dynamics/ichimoku.pine`
- Documentation file: `indicators/dynamics/ichimoku.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/ichimoku.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/ichimoku.md
