import numpy as np
import pandas as pd
import umap
import plotly.express as px


def add_sentences(data: pd.DataFrame, sentences: list[str], encoder) -> pd.DataFrame:
    sentences_ = pd.DataFrame(sentences, columns=["sentences"]).assign(
        short_sentences=lambda df: df["sentences"].str.slice(0, 20) + "...",
        field="MINE",
    )

    all_sentences = pd.concat([data, sentences_], ignore_index=True)

    encodings = encoder.encode(all_sentences["sentences"])

    reduced_encodings = reduce_dimensions(encodings)

    return add_umap_to_dataset(all_sentences, reduced_encodings)


def plot_sentences(sentences: pd.DataFrame) -> None:
    sentences["short_sentences"] = sentences["sentences"].str.slice(0, 20) + "..."

    fig = px.scatter(
        sentences,
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
    fig.update_layout(title_text="Which vectors are close?", template="plotly_white")
    fig.update_traces(textposition="top center", marker=dict(size=15))
    fig.show()


def reduce_dimensions(vectors: np.array) -> np.array:
    reducer = umap.UMAP()
    reduced_vectors = reducer.fit_transform(vectors)

    return reduced_vectors


def add_umap_to_dataset(data: pd.DataFrame, reduced_vectors: np.array) -> pd.DataFrame:
    return data.assign(
        reduced=reduced_vectors.tolist(),
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
    )
