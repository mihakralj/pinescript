# MLP - Mlp


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MLP addresses this by implementing `Compresses an unbounded value to the range [-1, 1] using tanh or scaled sigmoid` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Compresses an unbounded value to the range [-1, 1] using tanh or scaled sigmoid`
- `Calculates and normalizes input features in one step`
- `Converts price format to return format`
- `Converts return format back to price format`
- `Expands a value from the range [-1, 1] back to its original unbounded range`
- `Calculates Huber loss value that is less sensitive to outliers than MSE squared error`
- `Calculates gradient of Huber loss for backpropagation`
- `Initializes neural network layer weights using Xavier/Glorot initialization`
- `Initializes neural network weights and biases using Xavier initialization`
- `Creates a new matrix with activation applied to all elements`
- `Performs forward pass through the neural network`
- `Performs backpropagation to update network weights and biases`

### Parameters

| Parameter | Purpose |
|---|---|
| `x` | The input value (can be any real number) |
| `useTanh` | Whether to use tanh (true) or scaled sigmoid (false) |
| `off` | Offset value |
| `reference_price` | The reference price to compare against |
| `new_price` | The current price value |
| `algo_type` | Algorithm type: 1=absolute change, 2=return ratio, 3=percentage change, 4=log return |
| `reference_price` | The reference price value |
| `price_return` | The return value |
| `algo_type` | Algorithm type: 1=absolute change, 2=return ratio, 3=percentage change, 4=log return |
| `y` | The compressed value in range [-1, 1] |
| `useTanh` | Whether y was produced by tanh (true) or scaled sigmoid (false) |
| `predicted` | The model's predicted value |
| `actual` | The true target value |
| `delta` | The threshold where loss function changes from quadratic to linear (default: 0.7) |
| `predicted` | The model's predicted value |
| `actual` | The true target value |
| `delta` | The threshold where gradient changes from linear to constant (default: 0.7) |
| `inputSize` | Number of neurons in the input layer |
| `outputSize` | Number of neurons in the output layer |
| `seed` | Random seed |
| `nodeLayerArray` | Array containing the number of nodes in each layer |
| `numInputsInt` | Number of input features |
| `seed` | Random seed |
| `this` | The input matrix with raw values |
| `useTanh` | Whether to use tanh activation |
| `input_arr` | Array of input features |
| `prediction` | The predicted output value from forward pass |
| `target` | The target value for training |
| `z_values` | Matrices object containing pre-activation values |
| `a_values` | Matrices object containing activation values |

### Returns

- A compressed value in range [-1, 1]

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

- Source code: `indicators/forecasts/mlp.pine`
- Documentation file: `indicators/forecasts/mlp.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/forecasts/mlp.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/forecasts/mlp.md
