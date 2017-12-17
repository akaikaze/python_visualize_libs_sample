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

from vispy import plot as vp
from vispy.color import get_colormap
import vispy

# create figure with plot
fig = vp.Fig()
ax_left = fig[0, 0]
ax_right = fig[0, 1]
ax_left._configure_2d()
ax_left.title.text = 'Current Clamp Recording'
ax_left.ylabel.text = 'Membrane Potential (mV)'
ax_left.xlabel.text = 'Time (ms)'
selected = None

cmap = get_colormap('hsl', value=0.5)
# colors = cmap.map(np.linspace(0.1, 0.9, df.shape[0]))
colors = cmap.map(np.linspace(0.1, 0.9, CYCLE))

ax_right.histogram(df.iloc[:,3])

df = df.groupby("cycle_no")
for i, (group_name, data) in enumerate(df):
    line = ax_left.plot((data["cycle_cnt"],data["val"]), color=colors[i])
    line.interactive = True
    line.unfreeze()  # make it so we can add a new property to the instance
    line.data_index = i
    line.freeze()


if __name__ == '__main__':
    fig.app.run()