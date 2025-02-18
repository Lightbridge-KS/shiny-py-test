from shiny import App, render, ui, reactive
import random  # For demonstration purposes

app_ui = ui.page_fixed(
    ui.input_numeric("num", "Enter a number:", value=5),
    ui.input_select(
        "select",
        "Select an option below:",
        {"1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"},
    ),
    ui.output_text("value"),
)

def server(input, output, session):
    # Effect to update select choices
    @reactive.Effect
    def _():
        # Get the input value
        num = input.num()
        
        # Perform some calculation to determine new choices
        # For example, create choices based on the input number
        new_choices = {
            f"{num}{letter}": f"Choice {num}{letter}" 
            for letter in ['A', 'B', 'C']
        }
        
        # Update the select input with new choices
        ui.update_select(
            "select",
            choices=new_choices,
            # Optionally set a new selected value
            selected=f"{num}A"  
        )

    @render.text
    def value():
        return f"Selected value: {input.select()}"

app = App(app_ui, server)