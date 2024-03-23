from shiny import render, reactive
from shiny.express import input, ui

ui.input_radio_buttons(  
    "radio",  
    "Radio buttons",  
    {"1": "Option 1", "2": "Option 2", "3": "Option 3"},  
    selected=None
)  


@render.ui
@reactive.event(input.radio)
def md_render():
    
    return ui.markdown(
    f"""
    # Hello World

    This is **markdown** and here is some `code`:
    You choose: {input.radio()}

    ```python
    print('Hello world!')
    ```
    """
    )



