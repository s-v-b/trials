



# %%
import bokeh
# %%



# %%
from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)
# %%



# %%
# prepare some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y0 = [i**2 for i in x]
y1 = [10**i for i in x]
y2 = [10**(i**2) for i in x]

# output to static HTML file
output_file("log_lines.html", mode="inline")

# create a new plot
p = figure(
   tools="pan,box_zoom,reset,save",
   y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
   x_axis_label='sections', y_axis_label='particles'
)

# add some renderers
p.line(x, x, legend="y=x")
p.circle(x, x, legend="y=x", fill_color="white", size=8)
p.line(x, y0, legend="y=x^2", line_width=3)
p.line(x, y1, legend="y=10^x", line_color="red")
p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
p.line(x, y2, legend="$y=10^x^2$", line_color="orange", line_dash="4 4")
# show the results
show(p)
# %%




# %%
import numpy as np

from bokeh.sampledata.stocks import AAPL

# prepare some data
aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

# output to static HTML file
output_file("stocks.html", title="stocks.py example")

# create a new plot with a a datetime axis type
p = figure(plot_width=800, plot_height=350, x_axis_type="datetime")

# add renderers
p.circle(aapl_dates, aapl, size=4, color='darkgrey', alpha=0.2, legend='close')
p.line(aapl_dates, aapl_avg, color='navy', legend='avg')

# NEW: customize by setting attributes
p.title.text = "AAPL One-Month Average"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# show the results
show(p)
# %%


```python
# %%
from scipy.stats import norm
import numpy as np
sam = sorted(norm.rvs(size=100))
p = figure(plot_width=600, plot_height=400,
    tools="pan,box_zoom,reset,save",
    y_range=[0., 1.1], title="Fonction de répartition, échantillon gaussien de taille 100",
    x_axis_label='x', y_axis_label='y')
# add a steps renderer
p.step(sam, np.linspace(1.0, len(sam), len(sam))/float(len(sam)),
    line_width=2, mode="after",
    legend="Fonction de répartition empirique")
p.line(sam, norm.cdf(sam), color='red', line_width=1,
    legend="Fonction de répartition gaussienne standard")
show(p)
# %%
```



# %%
from scipy.stats import norm
import numpy as np
sam = sorted(norm.rvs(size=1000))
p = figure(plot_width=600, plot_height=400,
    tools="pan,box_zoom,reset,save",
    y_range=[0.,1.1], title="Pont empirique, échantillon gaussien de taille 100",
    x_axis_label='x', y_axis_label='y')
# add a steps renderer
p.line(sam, np.sqrt(len(sam))*np.abs(np.linspace(1.0, len(sam), len(sam))/float(len(sam)) - norm.cdf(sam)), color='red', line_width=1)
show(p)
# %%


# %%
from scipy.stats import norm
import numpy as np
sam = sorted(norm.rvs(size=1000))
p = figure(plot_width=600, plot_height=400,
    tools="pan,box_zoom,reset,save",
    title="Pont empirique standardisé, échantillon gaussien de taille 100",
    x_axis_label='x', y_axis_label='y')
for col in ['blue', 'red', 'green', 'black', 'olive']:
    p.line(norm.cdf(sam),
        np.sqrt(len(sam))*np.abs(np.linspace(1.0/len(sam), 1.0, len(sam), endpoint=True) - norm.cdf(sam)),
        color=col,
        line_width=1)

show(p)
# %%


# %%
# from bokeh.plotting import figure
from pweave.bokeh import output_pweave, show

output_pweave()

from scipy.stats import norm
import numpy as np
n = 1000
p = figure(plot_width=600, plot_height=400,
    tools="pan,box_zoom,reset,save",
    title="Pont empirique standardisé, échantillon gaussien de taille {0:4d}".format(n),
    x_axis_label='x', y_axis_label='y')
for col in ['blue', 'red', 'green', 'black', 'olive']:
    sam = sorted(norm.rvs(size=n))
    p.line(norm.cdf(sam),
        np.sqrt(len(sam))*np.abs(np.linspace(1.0/len(sam), 1.0, len(sam), endpoint=True) - norm.cdf(sam)),
        color=col,
        line_width=1,
        alpha=.5)
x = np.linspace(1.0/n, 1.0, n, endpoint=True)
p.line(x, 2*np.sqrt(x * (1-x)), color='black', line_dash="4 4", legend='$2\sqrt{x(1-x)}$')
show(p)
# %%
