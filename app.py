import plotly.express as px
from shiny import render
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()
import pandas as pd
import seaborn as sns
from shiny import reactive, render, req

ui.page_opts(title="Sarah's Penguin Data", fillable=True)
    
with ui.sidebar(open="open"):  
        ui.h2("Sidebar")
        
        ui.input_selectize(  
        "selectize",  
        "Select an option below:",  
        ["Adelie", "Gentoo", "Chinstrap"],
    )
        ui.input_numeric("plotly_bin_count", "Bin Count", 10, min=1, max=20)
        (ui.input_slider("seaborn_bin_count", "Seaborn Slider", 0, 50, 25),)

        ui.input_checkbox_group(  
        "checkbox_group",  
        "Checkbox group",  
        {  
        "bill_depth_mm":"Bill Depth",  
        "flipper_length_mm": "Flipper Length",  
        "body_mass_g": "Body Mass",  
        },  
    )  
        ui.hr()
        ui.a(
        "GitHub",
         href="https://github.com/sapapesh/cintel-02-data",
         target="_blank",
         )

with ui.layout_columns():
    
    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="sex")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="size")
