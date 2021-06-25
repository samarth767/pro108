import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv("data4.csv")
digram = pff.create_distplot([df["Avg Rating"].tolist()],["Rating"],show_hist=False)
digram.show()