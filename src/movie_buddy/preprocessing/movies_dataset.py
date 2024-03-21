import pandas as pd
from ast import literal_eval


def get_movies_dataset() -> pd.DataFrame:
    original_movies_data_df = pd.read_csv(
        "../data/movies_metadata.csv", low_memory=False
    )

    columns = ["id", "title", "overview", "release_date", "runtime", "genres"]
    movies_df = original_movies_data_df[columns].dropna()

    movies_df["genres"] = movies_df["genres"].apply(literal_eval)
    movies_df = movies_df[movies_df["genres"].str.len() > 0]
    movies_df["genre"] = movies_df["genres"].apply(lambda i: i[0]["name"])

    movies_df = movies_df.drop(columns=["genres"], axis=0)

    return movies_df
