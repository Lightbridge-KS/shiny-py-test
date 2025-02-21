from shiny import App, render, ui

app_ui = ui.page_sidebar(
    ui.sidebar(
        "Sidebar",
        ui.input_select(
            "select",
            "Select an option below:",
            {"1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"},
        ),
        ui.input_text("text", "Text input", "Enter text..."),
        position="left",
        bg="#f8f8f8",
    ),
    "Main content",
    ui.output_text("value"),
)  


def server(input, output, session):
    @render.text
    def value():
        return f"{input.select()}"


app = App(app_ui, server)