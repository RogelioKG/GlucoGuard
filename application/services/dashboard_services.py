# standard library
import json

# third party library
import pandas as pd
import plotly # (註: Pylint 會認為 plotly 無法匯入，但事實上是可以的)
import plotly.express as px

# local library
from application.services import volunteer_services
from application.tests.generate import random_var_name


def get_volunteers_dataframe() -> pd.DataFrame:
    """獲取包含所有填表者的 DataFrame

    Returns
    -------
    + (pd.DataFrame)
    """
    volunteers = volunteer_services.get_all_volunteers()
    df_list = [volunteer.standardize() for volunteer in volunteers]
    volunteers_dataframe = pd.concat(df_list, ignore_index=True)
    return volunteers_dataframe

def count_bar_chart(column: str) -> tuple[str, str] | None:
    """數量長條圖

    Parameters
    ----------
    + `column` (str) : Volunteer 欄位名稱

    Returns
    -------
    + `graph` (tuple[str, str] | None)
        + `graph_name` (str) : Plotly chart id
        + `graphJSON` (str) : Plotly JSON chart
    """
    graph_name = random_var_name(32)
    try:
        df = get_volunteers_dataframe()
        ser_column = df.groupby(column)[column].count()
        fig = px.bar(x=ser_column.index, y=ser_column.values, labels={"x": column, "y": "count"})
        fig.update_layout(height=300, width=400)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        graph = (graph_name, graphJSON)
    except ValueError as err: # No objects to concatenate
        graph = None
    return graph
