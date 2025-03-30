import marimo

__generated_with = "0.11.31-dev3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go

    # Create UI elements
    amplitude = mo.ui.slider(1, 10, value=5, label="Amplitude")
    frequency = mo.ui.slider(1, 10, value=2, label="Frequency")

    color = mo.ui.dropdown(
        {
            "Blue": "blue",
            "Red": "red",
            "Green": "green",
            "Orange": "orange",
            "Black": "black"
        },
        value="Blue",
        label="Line Color"
    )
    return amplitude, color, frequency, go, mo, np


@app.cell
def _(amplitude, color, frequency, go, mo, np):
    # Left-side controls with a horizontal divider
    controls = mo.vstack([
        amplitude,
        frequency,
        mo.Html("<hr style='width:100%; border: none; border-top: 1px solid #ccc; margin: 1em 0;' />"),
        color
    ])

    # Generate sine wave data
    x = np.linspace(0, 10, 300)
    y = amplitude.value * np.sin(frequency.value * x)

    # Create Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", line=dict(color=color.value)))
    fig.update_layout(
        title="Interactive Sine Wave (Plotly)",
        margin=dict(t=40, b=40, l=40, r=40),
        height=400
    )

    # Layout with controls on the left and plot on the right
    mo.hstack([controls, fig])
    return controls, fig, x, y


if __name__ == "__main__":
    app.run()
