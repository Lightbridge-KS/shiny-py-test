from pathlib import Path
from shiny import App, ui, render, reactive, Inputs, Outputs, Session
import pandas as pd
from pandas import read_csv

app_ui = ui.page_fluid(
    ui.download_button("download", "Download CSV"),
    ui.output_table("table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Calc
    def ts_data():
        return read_csv(
            "https://gist.githubusercontent.com/slopp/ce3b90b9168f2f921784de84fa445651/raw/4ecf3041f0ed4913e7c230758733948bc561f434/penguins.csv"
        )

    @output
    @render.table()
    def table():
        return ts_data()

    @session.download(filename="data.csv")
    def download():
        yield ts_data().to_csv()


app = App(app_ui, server)