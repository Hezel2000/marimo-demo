import marimo

__generated_with = "0.11.31-dev3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    # Create UI controls
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
    return amplitude, color, frequency, mo, np, plt


@app.cell
def _(amplitude, color, frequency, mo, np, plt):
    # Left side controls
    controls = mo.vstack([amplitude, frequency, mo.Html("<hr style='width:100%; border: none; border-top: 1px solid #ccc; margin: 1em 0;' />"), color])

    # Generate sine wave
    x = np.linspace(0, 10, 300)
    y = amplitude.value * np.sin(frequency.value * x)

    # Create figure
    fig, ax = plt.subplots()
    ax.plot(x, y, color=color.value)
    ax.set_title("Interactive Sine Wave")
    ax.grid(True)

    # Show controls + plot side by side
    mo.hstack([controls, fig])
    return ax, controls, fig, x, y


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


if __name__ == "__main__":
    app.run()
