from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash()

app.layout = html.Div(children=[
    html.H1("Sales Data Dashboard"),

    html.Div(children="Enter a date range to filter sales data:"),

    html.Div([
        dcc.Input(id="start-date", type="text", placeholder="YYYY-MM-DD"),
        dcc.Input(id="end-date", type="text", placeholder="YYYY-MM-DD"),
    ], style={"display": "flex", "gap": "10px", "margin-bottom": "20px"}),

    dcc.Graph(id="sales-chart")
])


@app.callback(
    Output("sales-chart", "figure"),
    Input("start-date", "value"),
    Input("end-date", "value")
)
def update_graph(start_date, end_date):
    if not start_date or not end_date:
        return px.line(df, x="date", y="sales", color="region",
                       title="Sales Data Visualization",
                       labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
                       markers=True)

    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        fig = px.line(filtered_df, x="date", y="sales", color="region",
                      title=f"Sales Data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}",
                      labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
                      markers=True)

        return fig

    except Exception as e:
        return px.line(df, x="date", y="sales", color="region",
                       title="Invalid Date Format - Please Use YYYY-MM-DD",
                       labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
                       markers=True)


if __name__ == "__main__":
    app.run(debug=True)


