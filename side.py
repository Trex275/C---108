import csv 
import plotly.figure_factory as pf
import pandas as pd

df = pd.read_csv("data.csv")
#fig = pf.create_distplot([df["Height(Inches)"].tolist()],["Height"], show_hist = False)
fig = pf.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist = False)
fig.show()