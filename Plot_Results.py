from bokeh.plotting import figure, show
from bokeh.io import export_png
from bokeh.models import Title


def plot_runtimes(E, G):
    # for some reason the list aren't read as lists so just re-listifying them
    E = list(E)
    G = list(G)
    Number_of_items = list(range(3, 16))

    # create scatter plot layout
    p = figure(width=600, height=400, title="Average Runtime")
    p.add_layout(Title(text="Number of Items", align="center"), "below")
    p.add_layout(Title(text="Runtime (Seconds)", align="center"), "left")

    # add data to scatter plot
    p.circle(Number_of_items, E, color="Blue", legend_label="Exhaustive")
    p.square(Number_of_items, G, color="Green", legend_label="Greedy")

    # add legend
    p.legend.location = "top_right"
    p.legend.title = "Search Algorithm"
    p.add_layout(p.legend[0], 'right')

    # remove toolbar on graph
    p.toolbar.logo = None
    p.toolbar_location = None

    # save as Plot.png
    export_png(p, filename="Runtimes.png")

def plot_Items(Objects):
    Weights = []
    Values = []
    for weight, values in Objects.values():
        Weights.append(weight)
        Values.append(values)
    
    # create scatter plot layout
    p = figure(width=600, height=400, title="Item spread")
    p.add_layout(Title(text="Weights", align="center"), "below")
    p.add_layout(Title(text="Values", align="center"), "left")

    # add data to scatter plot
    p.circle(Weights, Values, color="Blue")

    # remove toolbar on graph
    p.toolbar.logo = None
    p.toolbar_location = None

    export_png(p, filename="Items.png")

    






