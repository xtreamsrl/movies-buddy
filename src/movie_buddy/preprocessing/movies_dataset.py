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


def get_sentences_dataset() -> pd.DataFrame:
    my_sentences_list = [
        ("The sun rises in the east and sets in the west.", "Nature and Environment"),
        (
            "Forests play a crucial role in maintaining the earth's ecosystem.",
            "Nature and Environment",
        ),
        (
            "Pollution is one of the biggest threats to marine life.",
            "Nature and Environment",
        ),
        ("Climate change affects weather patterns globally.", "Nature and Environment"),
        ("Cats are known for their independence and agility.", "Animals"),
        ("Dogs are loyal companions that can understand human emotions.", "Animals"),
        ("Elephants have complex social structures and remarkable memory.", "Animals"),
        ("Technology has revolutionized the way we communicate.", "Technology"),
        (
            "Artificial intelligence is transforming industries by automating tasks.",
            "Technology",
        ),
        (
            "Cybersecurity is essential in protecting online data from threats.",
            "Technology",
        ),
        (
            "Cooking at home allows for healthier dietary choices.",
            "Health and Lifestyle",
        ),
        (
            "Regular exercise contributes to both physical and mental well-being.",
            "Health and Lifestyle",
        ),
        ("Meditation can reduce stress and improve focus.", "Health and Lifestyle"),
        (
            "Mathematics is fundamental to the understanding of the universe.",
            "Science and Education",
        ),
        (
            "Physics explores the fundamental principles governing the natural world.",
            "Science and Education",
        ),
        (
            "History teaches us about the successes and failures of past civilizations.",
            "Science and Education",
        ),
        (
            "Reading fiction can improve empathy and emotional intelligence.",
            "Literature and Psychology",
        ),
        (
            "Writing poetry is a way to express emotions and explore creativity.",
            "Literature and Psychology",
        ),
        (
            "Studying psychology helps us understand human behavior and mental processes.",
            "Literature and Psychology",
        ),
        ("The Olympic Games bring together athletes from around the world.", "Sports"),
        (
            "Football is one of the most popular sports globally, with a vast fan base.",
            "Sports",
        ),
        (
            "Marathon running challenges individuals to push their physical limits.",
            "Sports",
        ),
        (
            "Renewable energy sources are key to sustainable development.",
            "Energy and Sustainability",
        ),
        (
            "Recycling reduces waste and conserves natural resources.",
            "Energy and Sustainability",
        ),
        (
            "Urban planning that includes green spaces contributes to environmental health.",
            "Energy and Sustainability",
        ),
    ]

    return pd.DataFrame(my_sentences_list, columns=["sentences", "field"])
