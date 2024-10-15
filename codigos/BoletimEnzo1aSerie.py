# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

import matplotlib.pyplot as plt
import numpy as np

disciplinas = ["LÍNGUA PORTUGUESA", "HISTÓRIA", "GEOGRAFIA", "CIÊNCIAS / MAKER", "MATEMÁTICA", "ED.FÍSICA", "ARTE", "LÍNGUA INGLESA"]
bimestre= {
    "1bim": (8, 8, 8, 8, 9, 8, 7, 0),
    "2bim": (9, 8, 8, 8, 8, 10, 7, 8),
    "3bim": (7, 8, 8, 8, 7, 9, 8, 8)
}

x=np.arange(len(disciplinas))
width=0.25
multiplier=0

fig, ax = plt.subplots(layout='constrained')
for attribute, measurement in bimestre.items():
    offset=width*multiplier
    rects=ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier+=1

ax.set_xticks(x+width, disciplinas)
plt.show()