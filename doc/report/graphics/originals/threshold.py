#!/usr/bin/env python3

'''aionfpga ~ threshold graphic
Copyright (C) 2020 Dominik Müller and Nico Canzani
'''

import numpy as np
import matplotlib.pyplot as plt

def y(t):
    return 0.4*np.sin(2*np.pi/4*t + np.pi/6) + 1.7

t1 = np.linspace(-0.5, 8.5, 1001)
y1 = y(t1)

t2 = np.linspace(1, 8, 8)
y2 = y(t2)

t3 = np.linspace(0, 8, 9)
y3 = y(t3)

diff = [abs(y3[i+1] - y3[i]) for i in range(8)]
diff = np.asarray(diff)+1.7

avg = np.sum(diff)/8

fig, ax1 = plt.subplots(figsize=[8, 4])
ax1.grid(b=True, which='major', color='#666666', linestyle='-')
ax1.grid(b=True, which='minor', color='#bbbbbb', linestyle='-')
plt.xlim(-0.5, 8.5)
ax1.set_xticks([])
ax1.set_yticks([])
ax2 = ax1.twinx()
ax1.axis('equal')
ax1.set_ylim(-0.5, 3)
ax2.axis('equal')
ax2.set_yticks([])
# ax1.plot(t1, y1, color=(0.8500, 0.3250, 0.0980))
ax2.scatter(t2, diff, color=(0, 0.4470, 0.7410))
ax2.set_ylim(-0.5, 3)

ax1.arrow(-0.5, 0, 9, 0, color='black', head_width=0.1, head_length=0.2)
ax1.text(8.8, -0.1, 'FID', ha='center', va='top')
ax1.arrow(0, -0.5, 0, 3.5, color='black', head_width=0.1, head_length=0.2)
ax1.text(-0.3, 3.4, 'DIFF', ha='center', va='top')

ax1.hlines(avg, -0.5, 8.5, color='gray', linestyles='dashed')
ax1.text(3, avg+0.1, 'MEAN DIFF', ha='center',)
ax1.hlines(2.6, -0.5, 8.5, color='gray', linestyles='dashed')
ax1.text(3, 2.7, 'THRESHOLD = 1.1 $\\cdot$ MEAN DIFF', ha='center')

ax1.text(0.1, -0.1, 0, ha='left', va='top')
for i in range(1, 9):
    ax1.vlines(i, 0, diff[i-1], color='gray', linestyles='dotted')
    ax1.text(i, -0.1, i, ha='center', va='top')

for ax in [ax1, ax2]:
    for key in ['left', 'right', 'top', 'bottom']:
        ax.spines[key].set_visible(False)

plt.savefig('threshold.pdf', transparent=True, bbox_inches='tight', pad_inches=0)
plt.show()
