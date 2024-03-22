from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 0, 100, 40),
    ui.output_text_verbatim("txt"),
    ui.input_action_button("reset", "Reset"),
)

def server(input, output, session):
    @reactive.calc  # Same as `reactive()` in R
    def val():
        return input.n()

    @reactive.effect # Same as `observe()` in R
    def _():
        input.reset()
        ui.update_slider("n", value=40)

    @output
    @render.text
    def txt():
        return f"n*2 is {val() * 2}"

app = App(app_ui, server)