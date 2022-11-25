import matplotlib.pyplot as plt
import numpy as np
from texttable import Texttable
#collected data
resistance_angle = {0: 1543,
                    10: 1615,
                    20: 1740,
                    30: 1950,
                    40: 2320,
                    50: 2880,
                    60: 3670,
                    70: 5080,
                    80: 6810,
                    90: 15010
                    }
#data processing
angles = resistance_angle.keys()
resistance = [value for (key, value) in resistance_angle.items()]
intensity = [1/value for value in resistance]

rmin = min(resistance)
rmax = max(resistance)

measured_intensity_norm = [(1/value - 1/rmax)/(1/rmin - 1/rmax)
                           for (key, value) in resistance_angle.items()]
theorectical_intensity_norm = [(np.cos(np.deg2rad(i))**2) for i in angles]

#output data in tabular format
t = Texttable()
rows = [[angle, resistance[idx]/1000, intensity[idx]*1000, measured_intensity_norm[idx]]
        for (idx, angle) in enumerate(angles)]

rows.insert(0, ["θ", "Resistance(R, kΩ)", "Intensity Estimate(1/R)",
                "Normalized(1/R -1/R_90)"])
t.add_rows(rows)
print(t.draw())

#plot data
plt.xlabel("Degree")
plt.ylabel("Normalized Intensity")
plt.scatter(angles, theorectical_intensity_norm, label='Theorectical')
plt.scatter(angles, measured_intensity_norm, label='Measured')
plt.xticks(np.arange(0, 100, 10))
plt.ylim([0, 1.2])
plt.legend()
plt.show()
