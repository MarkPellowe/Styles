"""A template to allow plotly to be used instead of matplotlib DIRECTLY in 
    the thesis. 
    This file needs to be within the path, and you import it at the beginning of 
    the document and then set the default template to the one desired as:
    `import publishable
    pio.templates.default = "scientific"`
    """

import plotly.graph_objects as go
import plotly.io as pio


pio.templates["scientific"] = go.layout.Template(
    layout=dict(
        scene={
            "xaxis": {
                "backgroundcolor": "white",
                "gridcolor": "rgb(45,45,45)",
                "gridwidth": 2,
                "linecolor": "rgb(0,0,0)",
                "showbackground": True,
                "showgrid": True,
                "showline": True,
                "mirror": "allticks",
                "ticks": "inside",
                "nticks": 6,
                "tickwidth": 1.2,
                "zeroline": False,
                "zerolinecolor": "rgb(0,0,0)",
            },
            "yaxis": {
                "backgroundcolor": "white",
                "gridcolor": "rgb(45,45,45)",
                "gridwidth": 2,
                "linecolor": "rgb(0,0,0)",
                "showbackground": True,
                "showgrid": True,
                "showline": True,
                "mirror": "allticks",
                "ticks": "inside",
                "nticks": 6,
                "tickwidth": 1.25,
                "zeroline": False,
                "zerolinecolor": "rgb(0,0,0)",
            },
            "zaxis": {
                "backgroundcolor": "white",
                "gridcolor": "rgb(45,45,45)",
                "gridwidth": 2,
                "linecolor": "rgb(0,0,0)",
                "showbackground": True,
                "showgrid": True,
                "showline": True,
                "mirror": "allticks",
                "ticks": "inside",
                "nticks": 6,
                "tickwidth": 1.2,
                "zeroline": False,
                "zerolinecolor": "rgb(0,0,0)",
            },
        },
        xaxis={
            "automargin": True,
            "gridcolor": "rgb(45,45,45)",
            "linecolor": "rgb(0,0,0)",
            "linewidth": 2,
            "showgrid": True,
            "showline": True,
            "mirror": "allticks",
            "ticks": "inside",
            "nticks": 6,
            "tickwidth": 1.2,
            "title": {"standoff": 10},
            "zeroline": False,
            "griddash": "dash",
        },
        yaxis={
            "automargin": True,
            "gridcolor": "rgb(45,45,45)",
            "linecolor": "rgb(0,0,0)",
            "linewidth": 2,
            "showgrid": True,
            "showline": True,
            "mirror": "allticks",
            "ticks": "inside",
            "nticks": 6,
            "tickwidth": 1.2,
            "title": {"standoff": 10},
            "griddash": "dash",
            "zeroline": False,
        },
        font={"family": "CMU Serif", "size": 12, "color": "black"},
        width=500,
        height=350,
        margin={
            "l": 5,
            "r": 5,
            "t": 10,
            "b": 5,
            "pad": 4,
        },
        # title={"pad": 10},
    )
)
