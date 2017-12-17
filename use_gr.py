from numpy.random import randn
import pandas as pd
import numpy as np

CYCLE=1000
N_PAR_CYCLE=1000
n=CYCLE*N_PAR_CYCLE

df=pd.DataFrame(
    {
        "idx":np.arange(1, n+1),
        "cycle_no":np.repeat(range(1, CYCLE+1), N_PAR_CYCLE),
        "cycle_cnt":np.tile(np.arange(1, N_PAR_CYCLE+1), CYCLE),
        "val": randn(n)+ np.repeat(range(CYCLE), N_PAR_CYCLE)
    }
)

import gr
from gr.pygr import Plot, PlotAxes, PlotContour, PlotCurve

gr.setwindow(-2, 1000, -2, 1000)
gr.setviewport(0.05, 0.95, 0.05, 0.95)
gr.setfillintstyle(1)
gr.setfillcolorind(208)


# create figure with plot
# fig = plt.Fig()
# ax_left = fig[0, 0]
# ax_right = fig[0, 1]
# ax_left._configure_2d()
# ax_left.title.text = 'Current Clamp Recording'
# ax_left.ylabel.text = 'Membrane Potential (mV)'
# ax_left.xlabel.text = 'Time (ms)'
selected = None

# cmap = get_colormap('hsl', value=0.5)
# colors = cmap.map(np.linspace(0.1, 0.9, df.shape[0]))
# colors = cmap.map(np.linspace(0.1, 0.9, CYCLE))

# ax_right.histogram(df.iloc[:,3])
# df2 = df.copy()
df = df.groupby("cycle_no")
gr.clearws()

for i, (group_name, data) in enumerate(df):
    color_id = i - int(i / 256) * 256
    gr.setlinecolorind(int(color_id))
    gr.polyline(data["cycle_cnt"].tolist(), data["val"].tolist())

gr.updatews()

"""
or
for i, (group_name, data) in enumerate(df):
    gr.pygr.oplot((data["cycle_cnt"], data["val"]))

"""


