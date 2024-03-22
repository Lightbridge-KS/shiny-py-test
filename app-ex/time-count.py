# Core
from shiny import App, reactive, render, ui
from datetime import datetime

app_ui = ui.page_fixed(
    ui.h1("Title"),
    ui.output_code("greeting"),
)

def server(input, output, session):
    @reactive.calc
    def time():
        reactive.invalidate_later(1)
        return datetime.now()

    @render.code
    def greeting():
        return f"Hello, world!\nIt's currently {time()}."

app = App(app_ui, server)