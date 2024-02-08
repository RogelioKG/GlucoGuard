# standard library
import json
import uuid

# third party library
import pandas as pd
import plotly
import plotly.express as px


def count_bar_chart(df: pd.DataFrame, column: str) -> (tuple[str, str] | None):
    """數量長條圖

    Parameters
    ----------
    + `df` (pd.DataFrame) : 所有填表者標準化 DataFrame
    + `column` (str) : Volunteer 欄位名稱

    Returns
    -------
    + `graph` (tuple[str, str] | None)
        - `graph_id`  (str) : Plotly chart id
        - `graphJSON` (str) : Plotly JSON chart
    """
    graph_id = "chart_" + str(uuid.uuid4()).replace("-", "_")
    try:
        ser_column = df.groupby(column)[column].count()
        fig = px.bar(
            x=ser_column.index, y=ser_column.values, labels={"x": column, "y": "count"}
        )
        fig.update_layout(height=300, width=400)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        graph = (graph_id, graphJSON)
    except ValueError:
        graph = None
    return graph
