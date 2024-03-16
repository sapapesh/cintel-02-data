import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Sarah's Penguin Data", fillable=True)
with ui.layout_columns():
    
    with ui.sidebar(open="open", bg="#f8f8f8"):  
        ui.h2("Sidebar")

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="sex")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="size")
