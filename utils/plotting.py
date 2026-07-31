import plotly.graph_objects as go

from utils.geometry import einstein_rosen_bridge


def create_bridge(mass):

    X, Y, Z = einstein_rosen_bridge(mass)

    fig = go.Figure()

    # Upper universe
    fig.add_surface(
        x=X,
        y=Y,
        z=Z,
        colorscale="Viridis",
        showscale=False
    )

    # Lower universe
    fig.add_surface(
        x=X,
        y=Y,
        z=-Z,
        colorscale="Viridis",
        showscale=False
    )

    fig.update_layout(

        title="Einstein-Rosen Bridge",

        scene=dict(

            xaxis_title="X",

            yaxis_title="Y",

            zaxis_title="Z",

            aspectmode="data",

            camera=dict(

                eye=dict(
                    x=2,
                    y=2,
                    z=1.4
                )

            )
        ),

        margin=dict(
            l=0,
            r=0,
            t=40,
            b=0
        )

    )

    return fig
