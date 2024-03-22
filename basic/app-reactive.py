from shiny import ui, render, reactive, App

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 0, 100, 40),
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @reactive.calc
    def n():
      return input.n()

    @output
    @render.text
    def txt():
        return f"n*2 is {n() * 2}"

app = App(app_ui, server)