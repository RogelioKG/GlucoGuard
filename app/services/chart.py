# standard library
import json

# third party library
import pandas as pd
import plotly # (註: Pylint 會認為 plotly 無法匯入，但事實上是可以的)
import plotly.express as px

# local library
from app import db
from app.models.volunteer import Volunteer
from app.services import generate



def get_all_volunteers_dataframe() -> pd.DataFrame:
    """獲取包含所有填表者的 DataFrame

    Returns
    -------
    + `volunteers_dataframe` (pd.DataFrame)
    """
    # 取得所有填表者資料
    volunteers = db.session.query(Volunteer).all()
    df_list = [volunteer.standardize() for volunteer in volunteers]
    volunteers_dataframe = pd.concat(df_list, ignore_index=True)
    return volunteers_dataframe


def count_bar_chart(column: str) -> (tuple[str, str] | None):
    """數量長條圖

    Parameters
    ----------
    + `column` (str) : Volunteer 欄位名稱

    Returns
    -------
    + `graph` (tuple[str, str] | None)
        - `graph_name` (str) : Plotly chart id
        - `graphJSON` (str) : Plotly JSON chart
    """
    graph_name = generate.random_var_name(32)
    try:
        df = get_all_volunteers_dataframe()
        ser_column = df.groupby(column)[column].count()
        fig = px.bar(x=ser_column.index, y=ser_column.values, labels={"x": column, "y": "count"})
        fig.update_layout(height=300, width=400)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        graph = (graph_name, graphJSON)
    except ValueError as err:
        graph = None
    return graph
