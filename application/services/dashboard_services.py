# standard library
import json

# third party library
import pandas as pd
import plotly # (註: Pylint 會認為 plotly 無法匯入，但事實上是可以的)
import plotly.express as px

# local library
from application.models.volunteer import Volunteer


def get_chart(volunteers: list[Volunteer]) -> str:
    """未完成

    Parameters
    ----------
    + `volunteers` (list[Volunteer]) : 所有填表者

    Returns
    -------
    + `graphJSON` (str) : Plotly JSON chart
    """
    
    try:
        df_list = [volunteer.standardize() for volunteer in volunteers]
        df = pd.concat(df_list, ignore_index=True)
        income_df = df.groupby("Income")["Income"].count()
        fig = px.bar(x=income_df.keys(), y=income_df.values)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    except ValueError as err: # No objects to concatenate
        graphJSON = ""

    return graphJSON
