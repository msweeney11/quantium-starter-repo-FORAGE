from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(by="date")

fig = px.line(df, x="date", y="sales", color="region",
              title="Sales Data Visualization",
              labels={"date": "Date", "sales": "Total Sales", "region": "Region"})

app = Dash()

app.layout = html.Div(children=[
    html.H1(children="Sales Data Dashboard"),

    html.Div(children="""
        A visualization of total sales per day across different regions.
    """),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
