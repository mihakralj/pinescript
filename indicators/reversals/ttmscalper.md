# TTMSCALPER - Ttmscalper


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. TTM_SCALPER addresses this by implementing `Detects 3-bar pivot patterns for scalping entry signals` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Detects 3-bar pivot patterns for scalping entry signals`

### Parameters

| Parameter | Purpose |
|---|---|
| `use_closes` | Use close prices instead of high/low for pivot detection |

### Returns

- [pivot_high_price, pivot_low_price] Pivot values (na if no pivot)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_use_closes` | `input.bool` | default: `false`, label: "Use Closes" |
| `i_show_high` | `input.bool` | default: `true`, label: "Show Pivot Highs" |
| `i_show_low` | `input.bool` | default: `true`, label: "Show Pivot Lows" |
| `i_color_high` | `input.color` | default: `color.red`, label: "Pivot High Color" |
| `i_color_low` | `input.color` | default: `color.green`, label: "Pivot Low Color" |

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

- Source code: `indicators/reversals/ttmscalper.pine`
- Documentation file: `indicators/reversals/ttmscalper.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/ttmscalper.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/ttmscalper.md
