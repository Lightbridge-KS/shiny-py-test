from shiny import ui, render, App

app_ui = ui.page_fluid(
    ui.input_text("text", "Text input", "Enter text..."),  
    ui.output_text_verbatim("value"),
)

def server(input, output, session):
    @render.text
    def value():
        return f"{input.text()} is {type(input.text())}"

app = App(app_ui, server)