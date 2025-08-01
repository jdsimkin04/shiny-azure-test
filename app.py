from shiny import App, render, ui
import random

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny on Azure"),
    ui.output_text("random_number")
)

def server(input, output, session):
    @output
    @render.text
    def random_number():
        return f"Random number: {random.randint(1, 100)}"

app = App(app_ui, server)
