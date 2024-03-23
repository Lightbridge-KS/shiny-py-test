from shiny import render
from shiny.express import ui
import pandas as pd

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
        
frame = pd.DataFrame(data)

ui.h2("Data Grid")

@render.data_frame  
def states_df():
    return render.DataGrid(frame)  