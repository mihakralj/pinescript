# STOCH - Stoch


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. STOCH addresses this by implementing `Calculates the Stochastic Oscillator (%K and %D). %K = 100 * (close - lowest_low(kLength)) / (highest_high(kLength) - lowest_low(kLength)). %D = SMA(%K, dPeriod). Uses efficient deque implementation for min/max and buffer-based SMA.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Stochastic Oscillator (%K and %D). %K = 100 * (close - lowest_low(kLength)) / (highest_high(kLength) - lowest_low(kLength)). %D = SMA(%K, dPeriod). Uses efficient deque implementation for min/max and buffer-based SMA.`

### Parameters

| Parameter | Purpose |
|---|---|
| `kLength` | `simple int` The lookback period for calculating highest high and lowest low. |
| `dPeriod` | `simple int` The smoothing period for the %D line (SMA of %K). |

### Returns

- `[float, float]` A tuple containing the %K value and the %D value.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `kPeriod` | `input.int` | default: `14`, label: "K Length" |
| `dPeriod` | `input.int` | default: `3`, label: "D Smooth" |

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

- Source code: `indicators/oscillators/stoch.pine`
- Documentation file: `indicators/oscillators/stoch.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/stoch.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/stoch.md
