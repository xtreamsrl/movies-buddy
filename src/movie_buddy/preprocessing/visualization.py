import pandas as pd
import plotly.express as px


def plot_sentences(sentences_df: pd.DataFrame) -> None:
    fig = px.scatter(
        sentences_df,
        x="x",
        y="y",
        text="short_sentences",
        color="field",
        height=512,
        hover_name="field",
        hover_data={
            "sentences": True,
            "x": False,
            "y": False,
            "field": False,
            "short_sentences": False,
        },
    )
    fig.update_layout(title_text="Which Vector are close?", template="plotly_white")
    fig.update_traces(textposition="top center", marker=dict(size=15))
    fig.show()
