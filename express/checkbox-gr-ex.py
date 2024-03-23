from shiny import render
from shiny.express import input, ui

ui.input_checkbox_group(  
    "checkbox_group",  
    "Checkbox group",  
    {  
        "a": "A",  
        "b": "B",  
        "c": "C",  
    },  
)  

@render.text
def value():
    res = input.checkbox_group()
    return f"""
raw: {res}
type (tuple): {type(res)}
type (list): {list(res)}
"""