# BAXTERKING - Baxterking


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BAXTERKING addresses this by implementing `Baxter-King symmetric band-pass filter` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Baxter-King symmetric band-pass filter`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Input series |
| `pLow` | Minimum period of the passband (bars). Must be >= 2. |
| `pHigh` | Maximum period of the passband (bars). Must be > pLow. |
| `K` | Half-length of the symmetric filter (number of leads/lags). |

### Returns

- Cyclical component (oscillates around zero), delayed by K bars.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `pLow` | `input.int` | default: `6`, label: "Min Period (pLow)" |
| `pHigh` | `input.int` | default: `32`, label: "Max Period (pHigh)" |

## Runtime profile

- Declared optimization: O(K) per bar — single weighted sum over 2K+1 lagged values.
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

- Source code: `indicators/filters/baxterking.pine`
- Documentation file: `indicators/filters/baxterking.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/baxterking.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/baxterking.md
