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

def plot_Items(Total_Weights_E, Total_Weight_G):
    E = list(Total_Weights_E)
    G = list(Total_Weight_G)


    Number_of_items = list(range(3, 16))
    p = figure(width=600, height=400, title="Average Weights")
    p.add_layout(Title(text="Number of Items", align="center"), "below")
    p.add_layout(Title(text="Total Weight", align="center"), "left")

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
    export_png(p, filename="Total_Weights.png")

def plot_ValueRatio(Values_R):
    R = list(Values_R)

    Number_of_items = list(range(3, 16))

    p = figure(width=600, height=400, title="Value Ratio: Exhaustive/Greedy")
    p.add_layout(Title(text="Number of Items", align="center"), "below")
    p.add_layout(Title(text="Ratio", align="center"), "left")

    # add data to scatter plot
    p.circle(Number_of_items, R, color="Red")


    # remove toolbar on graph
    p.toolbar.logo = None
    p.toolbar_location = None

    # save as Plot.png
    export_png(p, filename="ValueRatio.png")
    






