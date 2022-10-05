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
        colorway=[
            "rgb(0,119,187)",
            "rgb(51,187,238)",
            "rgb(0,153,136)",
            "rgb(238,119,51)",
            "rgb(204,51,17)",
            "rgb(238,51,119)",
            "rgb(187,187,187)",
        ],
        # line={"dash":["solid","dot","dash","longdash","dashdot"],},
        # newshape_line_dash="dash",
        # ["solid","dot","dash","longdash","dashdot"],
        scene={
            "xaxis": {
                "backgroundcolor": "white",
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
            "zaxis": {
                "backgroundcolor": "white",
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
            "griddash": "dot",
            "gridwidth": 0.5,
            "gridcolor": "rgba(0,0,0,0.5)",
        },
        yaxis={
            "automargin": True,
            "linecolor": "rgb(0,0,0)",
            "linewidth": 2,
            "showgrid": True,
            "showline": True,
            "mirror": "allticks",
            "ticks": "inside",
            "nticks": 6,
            "tickwidth": 1.2,
            "title": {"standoff": 10},
            "griddash": "dot",
            "gridwidth": 0.5,
            "gridcolor": "rgba(0,0,0,0.5)",
            "zeroline": False,
        },
        font={"family": "CMU Serif", "size": 11, "color": "black"},
        width=612.40416,  # Matches text width of latex document exactly.
        height=459.30312,  # Sets it to a 4/3 aspect ratio.
        margin={
            "l": 5,
            "r": 5,
            "t": 10,
            "b": 5,
            "pad": 4,
        },
        # title={"pad": 10},
        legend={
            "orientation": "h",
            "y": -0.3,
            "x": 0.5,
            "yanchor": "bottom",
            "xanchor": "center",
            "bordercolor": "black",
            "borderwidth": 1.4,
        },
    )
)
