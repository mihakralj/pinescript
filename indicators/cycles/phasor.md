# Phasor Analysis (Ehlers)

The Phasor Analysis indicator, developed by John Ehlers, is designed to identify the phase of the dominant cycle component in a time series. This implementation is based on Ehlers' work on cycle analysis and uses his specific correlation method to determine the real and imaginary components of the signal, which are then used to calculate the phase angle.

The indicator provides an unwrapped phase angle that continuously accumulates, helping to visualize cycle progression. It also includes Ehlers' specific logic to prevent the angle from moving backward under certain conditions, aiming for a more stable representation of the cycle phase. Optional plots for a "Derived Period" and a "Trend State Variable" offer further insights into market dynamics. All core calculations are encapsulated within a single `phasor()` function.

## Calculation

The primary `phasor(src, period)` function performs all calculations and returns three series: the final Phasor Angle, the Derived Period, and the Trend State.

### 1. Core Unwrapped Phasor Calculation (Internal to `phasor()` function)

   - **Correlation (Ehlers' Method):**
     For a given `period`, the function calculates correlation sums to determine the real and imaginary parts of the signal relative to cosine and sine waves of that period.
     - **Real Part Calculation:**
       The real part is derived from correlating the source (`src`) with a cosine wave of the specified `period`. The formula involves sums of `src`, `cos_wave`, `src*src`, `src*cos_wave`, and `cos_wave*cos_wave` over the lookback `period`.
       ```pine
       // sx_corr = sum(x_val, period)
       // sy_cos_corr = sum(y_val_cos, period)
       // sxx_corr = sum(x_val*x_val, period)
       // sxy_cos_corr = sum(x_val*y_val_cos, period)
       // syy_cos_corr = sum(y_val_cos*y_val_cos, period)

       den_cos = (period * sxx_corr - sx_corr * sx_corr) * (period * syy_cos_corr - sy_cos_corr * sy_cos_corr)
       if den_cos > 0
           real_part := (period * sxy_cos_corr - sx_corr * sy_cos_corr) / math.sqrt(den_cos)
       ```
     - **Imaginary Part Calculation:**
       The imaginary part is derived similarly, correlating `src` with a negative sine wave (`-sin_wave`) of the `period`.
       ```pine
       // sx_corr = sum(x_val, period) (re-initialized)
       // sy_sin_corr = sum(y_val_sin, period)
       // sxx_corr = sum(x_val*x_val, period) (re-initialized)
       // sxy_sin_corr = sum(x_val*y_val_sin, period)
       // syy_sin_corr = sum(y_val_sin*y_val_sin, period)

       den_sin = (period * sxx_corr - sx_corr * sx_corr) * (period * syy_sin_corr - sy_sin_corr * sy_sin_corr)
       if den_sin > 0
           imag_part := (period * sxy_sin_corr - sx_corr * sy_sin_corr) / math.sqrt(den_sin)
       ```
   - **Phase Angle Conversion:**
     The real and imaginary parts are converted to a raw phase angle in degrees:
     ```pine
     current_raw_phase = 0.0
     if real_part != 0.0
         current_raw_phase := 90.0 - math.atan(imag_part / real_part) * 180.0 / math.pi
         if real_part < 0.0
             current_raw_phase -= 180.0
     else if imag_part != 0.0 // real_part is 0
         current_raw_phase := imag_part > 0.0 ? 0.0 : 180.0
     ```
   - **Unwrapping:**
     The raw phase angle is unwrapped to ensure it accumulates continuously. This result is stored internally as `calculated_Phasor_val`.
     ```pine
     var float core_Phasor_unwrapped_state = na // State for unwrapping
     // ... unwrapping logic ...
     core_Phasor_unwrapped_state := na(core_Phasor_unwrapped_state[1]) ? current_raw_phase : core_Phasor_unwrapped_state[1] + (current_raw_phase - core_Phasor_unwrapped_state[1])
     float calculated_Phasor_val = core_Phasor_unwrapped_state
     ```

### 2. Ehlers' "Angle Cannot Go Backwards" Condition (Internal to `phasor()` function)
The `calculated_Phasor_val` is then processed by Ehlers' specific condition:
   ```pine
   var float final_Phasor_state = na
   if na(final_Phasor_state[1])
       final_Phasor_state := calculated_Phasor_val
   else
       if calculated_Phasor_val < final_Phasor_state[1] and ((calculated_Phasor_val > -135 and final_Phasor_state[1] < 135) or (calculated_Phasor_val < -90 and final_Phasor_state[1] < -90))
           final_Phasor_state := final_Phasor_state[1] // Keep previous angle
       else
           final_Phasor_state := calculated_Phasor_val // Use new angle
   ```
   This `final_Phasor_state` is the first value returned by the `phasor()` function.

### 3. Derived Period Calculation (Internal to `phasor()` function)
   The Derived Period is calculated from the rate of change of `final_Phasor_state`.
   ```pine
   var float derivedPeriod_calc_state = na 
   angle_Change_For_Period = final_Phasor_state - nz(final_Phasor_state[1], final_Phasor_state)
   // Logic to handle zero or negative angle_Change_For_Period by referencing derivedPeriod_calc_state[1]
   if nz(angle_Change_For_Period) != 0.0
       derivedPeriod_calc_state := 360.0 / angle_Change_For_Period
   // ... (clamping and default logic) ...
   derivedPeriod_calc_state := math.max(1.0, math.min(derivedPeriod_calc_state, 60.0))
   ```
   This `derivedPeriod_calc_state` is the second value returned by the `phasor()` function.

### 4. Trend State Variable Calculation (Internal to `phasor()` function)
   The Trend State is calculated based on the rate of change of `final_Phasor_state` and its current level.
   ```pine
   var int trendState_calc_state = 0 
   angle_Change_For_State = final_Phasor_state - nz(final_Phasor_state[1], final_Phasor_state)
   currentTrendState_calc = 0 // Default to cycling
   if angle_Change_For_State <= 6.0: // Trend Mode (period >= 60)
       if final_Phasor_state >= 90.0 or final_Phasor_state <= -90.0:
           currentTrendState_calc := 1 // Long trend
       else if final_Phasor_state > -90.0 and final_Phasor_state < 90.0:
           currentTrendState_calc := -1 // Short trend (or out of trend)
   trendState_calc_state := currentTrendState_calc
   ```
   This `trendState_calc_state` is the third value returned by the `phasor()` function.

### 5. Plotting
In the global scope, the script calls `phasor()` once:
```pine
[phasorAngle, derivedPeriodValue, trendStateValue] = phasor(i_source, i_period)
```
These returned values are then used in `plot()` calls.

## Interpretation

- **Phasor Angle (Red Line):** This line represents the unwrapped phase of the dominant cycle, after Ehlers' conditions.
  - Crossing upwards through +90° can indicate a cycle peak.
  - Crossing downwards through -90° can indicate a cycle trough.
  - The continuous nature of the unwrapped phase helps in observing the cycle's progression over time.
- **Reference Lines:**
  - +90° (Green Dashed): Potential peak reference.
  - -90° (Blue Dashed): Potential valley reference.
  - 0° (Gray Dotted): Mid-cycle reference.
- **Derived Period (Orange Line, Optional):** Shows the calculated period of the cycle based on the rate of change of the Phasor Angle. It is clamped between 1 and 60 bars. When the market is trending strongly, this derived period may become very long (clamped at 60).
- **Trend State (Purple Histogram, Optional):**
  - `1`: Indicates a potential long trend when the Phasor Angle's rate of change is slow (≤ 6° per bar) and the angle itself is in an extreme zone (≥ +90° or ≤ -90°).
  - `-1`: Indicates a potential short trend or market indecision when the rate of change is slow, but the angle is between -90° and +90°.
  - `0`: Indicates the market is primarily in a cycling mode (Phasor Angle changing by more than 6° per bar).

## Usage

The Phasor Analysis indicator can be used to:
- Identify potential turning points in cyclical markets.
- Gauge the current phase of the dominant cycle.
- Determine if the market is in a trending or cycling mode using the optional Trend State variable.
- Estimate the period of the dominant cycle using the optional Derived Period plot.

Combine with other indicators for confirmation. The choice of `Period` input is crucial and may need adjustment based on the asset and timeframe being analyzed.

## Parameters

- **Period:** (Default: 28) The fixed cycle period to correlate against for the phase calculation.
- **Source:** (Default: `close`) The source data series for the calculation.
- **Show Derived Period:** (Default: `false`) Toggles the visibility of the Derived Period plot.
- **Show Trend State Variable:** (Default: `false`) Toggles the visibility of the Trend State histogram.

## Remarks

This indicator implements John Ehlers' specific correlation method for calculating the real and imaginary components. The unwrapping, the "angle cannot go backwards" logic, derived period, and trend state calculations are all encapsulated within the main `phasor()` function.
The `//@version=6` is used, aligning with modern Pine Script practices.
