from numpy.random import randn
import pandas as pd
import numpy as np

CYCLE=1000
N_PAR_CYCLE=100
n=CYCLE*N_PAR_CYCLE

df=pd.DataFrame(
    {
        "idx":np.arange(1, n+1),
        "cycle_no":np.repeat(range(1, CYCLE+1), N_PAR_CYCLE),
        "cycle_cnt":np.tile(np.arange(1, N_PAR_CYCLE+1), CYCLE),
        "val": randn(n)+ np.repeat(range(CYCLE), N_PAR_CYCLE)
    }
)

import matplotlib.pyplot as plt

# create figure with plot
fig, axes = plt.subplots(1, 2)
ax_left = axes[0]
ax_right = axes[1]
ax_left.set_title = 'Current Clamp Recording'
# ax_left.set_ylab = 'Membrane Potential (mV)'
# ax_left.xlabel.text = 'Time (ms)'

ax_right.hist(df.iloc[:,3])

df = df.groupby("cycle_no")
for i, (group_name, data) in enumerate(df):
    line = ax_left.plot((data["cycle_cnt"],data["val"]))

if __name__ == '__main__':
    fig.show()