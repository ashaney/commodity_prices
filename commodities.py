import pandas as pd
import altair as alt
import datapane as dp
import os
import glob

alt.data_transformers.disable_max_rows()

path = os.getcwd()

df = pd.read_csv(path+'all_prices.csv')
df['Date'] = pd.to_datetime(df['Date'])
commodity_list = list(df['Commodity'].unique())

print(df)
print(commodity_list)

input_dropdown = alt.binding_select(options=commodity_list)
selection = alt.selection_single(name='Commodity', fields=['Commodity'], bind=input_dropdown)

alt_plot = alt.Chart(df).mark_line().encode(
    x='Date',
    y='Price'
).add_selection(
    selection
).transform_filter(
    selection
)

report = dp.Report(
    "## Commodity Prices",
    dp.Plot(alt_plot, caption="Commodity prices over time"),
  ).upload(name="Commodity Prices",
  open=True,
  description = "Commodity Price Data from World Bank")