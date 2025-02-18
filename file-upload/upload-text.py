import pandas as pd

from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shiny.types import FileInfo

app_ui = ui.page_fluid(
    ui.input_file("file1", "Choose File", accept=[".txt"], multiple=False),
    ui.output_text_verbatim("output_text"),
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def parsed_file():
        file: list[FileInfo] | None = input.file1()
        print(f"file: {file}, type: {type(file)}")
        if file is None:
            return ""
        with open(file[0]["datapath"], 'r', encoding='utf-8') as f:
            return f.read()
        
    @render.text  
    def output_text():
        return parsed_file()


app = App(app_ui, server)