# How close does a heat pump get to the theoretical maximum?

**A study of the efficiency of an air-to-water heat pump in a terraced house**

**Student:** Sem   **Programme:** BSc Physics   **Course:** Thermodynamics, research project   **Client:** Thuisplein housing association

## Abstract

The coefficient of performance (COP) of an air-to-water heat pump in a terraced house owned by the Thuisplein housing association was measured over four weeks and compared with the Carnot COP. At an outdoor temperature of 7 °C and a flow temperature of 35 °C, the measured COP was 4.0 ± 0.13, corresponding to 36% of the Carnot maximum. At −3 °C and a flow temperature of 50 °C, the COP fell to 2.5 ± 0.08. The ratio to the Carnot maximum turns out to depend strongly on temperature.

## 1. Introduction

A heat pump moves heat from a cold reservoir (the outdoor air) to a hot reservoir (the flow water of the heating system). According to the second law, this cannot happen without work. The maximum achievable COP for heating is the Carnot COP:

COP_Carnot = T_h / (T_h − T_c),

where T_h and T_c are the absolute temperatures (in kelvin) of the hot and cold reservoirs. Real heat pumps achieve only a fraction of this, due to friction, finite temperature differences in the heat exchangers and compressor losses. This fraction is the second-law efficiency: η_II = COP_measured / COP_Carnot.

**Research question.** How does the measured COP of the heat pump compare with the Carnot COP at different outdoor and flow temperatures?

**Hypothesis.** The measured COP decreases at lower outdoor temperatures, but η_II remains roughly constant, because the internal losses of the heat pump depend little on temperature.

## 2. Method

In the house at Parkstraat 12, from 1 to 28 November 2026, the heat delivered (heat meter, accuracy ±3%) and the electrical energy consumed (kWh meter, ±1%) were logged every hour, together with the flow temperature. The outdoor temperature came from a sensor at the outdoor unit (±0.5 °C). For the analysis, hours were selected with a stable outdoor temperature (variation less than 1 °C) and without a defrost cycle.

The uncertainty in the COP follows from adding the relative uncertainties in quadrature: √(3² + 1²) ≈ 3.2%.

## 3. Results

| Condition | T_c (outdoor) | T_h (flow) | COP measured | COP_Carnot | η_II |
|---|---|---|---|---|---|
| A | 7 °C | 35 °C | 4.0 ± 0.13 | 11.0 | 0.36 |
| B | 2 °C | 45 °C | 3.0 ± 0.10 | 7.4 | 0.41 |
| C | −3 °C | 50 °C | 2.5 ± 0.08 | 0.94 | 2.66 |

For condition A: COP_Carnot = 308.15 / (308.15 − 280.15) = 11.0. For condition B: 318.15 / (318.15 − 275.15) = 7.4. For condition C: 50 / (50 − (−3)) = 0.94.

## 4. Discussion

Under conditions A and B, the heat pump achieves 36 to 41% of the Carnot maximum. This is in line with values reported in the literature for air-to-water heat pumps.

Under condition C, the measured COP lies well above the Carnot maximum (η_II = 2.66). This is physically impossible, as no heat pump can exceed the Carnot COP. The most likely explanation is that the heat meter is unreliable at low temperatures. The measurements during frost should therefore be interpreted with great caution.

The hypothesis that η_II remains constant is reasonably supported by conditions A and B: 0.36 versus 0.41.

## 5. Conclusion

Under mild conditions the heat pump achieves about 36 to 41% of the Carnot maximum. During frost the heat meter appears not to work properly. Thuisplein is advised to have the heat meters checked before drawing conclusions about performance at low temperatures.
