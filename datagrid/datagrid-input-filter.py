import pandas as pd
from shiny import ui, render, App, reactive, req
from palmerpenguins import load_penguins

penguins = load_penguins()
penguins_mini = penguins[["species", "island", "sex"]]

def query_any_column_df(df, query_text: str, case=False):
    """
    Filters the rows of a DataFrame based on whether any column contains the query text.
    """
    import pandas as pd
    # Create a mask for each column and combine them using 'any' along the columns
    mask = df.apply(lambda column: column.str.contains(query_text, case=case)).any(axis=1)
    # Filter the DataFrame using the combined mask
    filtered_df = df[mask]
    return filtered_df


app_ui = ui.page_fluid(
    
    ui.h2("Palmer Penguins"),
    ui.input_text("text", "Search term"),  
    ui.output_text_verbatim("value"),
    
    ui.output_data_frame("df_rendered"),  
)

def server(input, output, session):
    @render.text
    def value():
        return f"{input.text()}, {type(df_filt())}"
    
    @reactive.calc
    def df_filt():
        req(input.text())
        penguins_filt = query_any_column_df(penguins_mini, input.text())
        return penguins_filt
    
    @render.data_frame  
    def df_rendered():
        req(len(df_filt().index) != 0)
        return render.DataGrid(df_filt())  

app = App(app_ui, server)