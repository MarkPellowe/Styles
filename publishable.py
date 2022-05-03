"""A template to allow plotly to be used instead of matplotlib DIRECTLY in 
    the thesis. 

    This file needs to be within the path, and you import it at the beginning of 
    the document and then set the default template to the one desired as:

    `import publishable
    pio.templates.default = "scientific"`

    """

import plotly.graph_objects as go
import plotly.io as pio

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)

pio.templates["scientific"] = go.layout.Template(
    layout=dict(
        scene={
            "xaxis": {
                "backgroundcolor": "white",
                "gridcolor": "rgb(232,232,232)",
                "gridwidth": 2,
                "linecolor": "rgb(36,36,36)",
                "showbackground": True,
                "showgrid": True,
                "showline": True,
                "mirror": True,
                "ticks": "inside",
                "nticks": 6,
                "tickwidth": 1.25,
                "zeroline": False,
                "zerolinecolor": "rgb(36,36,36)",
            },
            "yaxis": {
                "backgroundcolor": "white",
                "gridcolor": "rgb(232,232,232)",
                "gridwidth": 2,
                "linecolor": "rgb(36,36,36)",
                "showbackground": True,
                "showgrid": True,
                "showline": True,
                "mirror": True,
                "ticks": "inside",
                "nticks": 6,
                "tickwidth": 1.25,
                "zeroline": False,
                "zerolinecolor": "rgb(36,36,36)",
            },
            "zaxis": {
                "backgroundcolor": "white",
                "gridcolor": "rgb(232,232,232)",
                "gridwidth": 2,
                "linecolor": "rgb(36,36,36)",
                "showbackground": True,
                "showgrid": True,
                "showline": True,
                "mirror": True,
                "ticks": "inside",
                "nticks": 6,
                "tickwidth": 1.25,
                "zeroline": False,
                "zerolinecolor": "rgb(36,36,36)",
            },
        },
        xaxis={
            "automargin": True,
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "rgb(36,36,36)",
            "linewidth": 2,
            "showgrid": True,
            "showline": True,
            "mirror": True,
            "ticks": "inside",
            "nticks": 6,
            "tickwidth": 1.25,
            "title": {"standoff": 10},
            "zeroline": False,
        },
        yaxis={
            "automargin": True,
            "gridcolor": "rgb(232,232,232)",
            "linecolor": "rgb(36,36,36)",
            "linewidth": 2,
            "showgrid": True,
            "showline": True,
            "mirror": True,
            "ticks": "inside",
            "nticks": 6,
            "tickwidth": 1.25,
            "title": {"standoff": 10},
            "zeroline": False,
        },
        font={"family": "serif", "size": 12, "color": "black"},
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
