import numpy as np
import pandas as pd
import umap


def reduce_dimensions(vectors: np.array) -> pd.DataFrame:
    reducer = umap.UMAP()
    reduced_vectors = reducer.fit_transform(vectors)

    return reduced_vectors


def add_umap_to_df(df: pd.DataFrame, reduced_vectors: np.array) -> pd.DataFrame:
    df["reduced_encoded"] = reduced_vectors.tolist()
    split = pd.DataFrame(df["reduced_encoded"].to_list(), columns=["x", "y"])
    df = pd.concat([df, split], axis=1)

    return df
