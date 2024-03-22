import pandas as pd
import numpy as np

from pathlib import Path
import numpy.typing as npt


def add_extra_movies() -> None:
    movies = get_movies_dataset()

    extra_movies = [
        (
            "1000",
            "Poor Things",
            "Poor Things is a 2023 film directed by Yorgos Lanthimos and written by "
            "Tony McNamara, based on the 1992 novel by Alasdair Gray. "
            "A co-production between Ireland, the United Kingdom, and the United States, "
            "the film stars Emma Stone, Mark Ruffalo, Willem Dafoe, Ramy Youssef, "
            "Christopher Abbott, and Jerrod Carmichael.[5] It focuses on Bella Baxter, "
            "a woman in Victorian London who is brought back to life via brain "
            "transplant and embarks on an odyssey of self-discovery. "
            "Principal photography took place in Hungary from August to December 2021. "
            "Poor Things premiered at the 80th Venice International Film Festival on "
            "September 1, 2023, and won the Golden Lion there. The film was released "
            "theatrically in the United States on December 8, 2023, and in the United "
            "Kingdom and Ireland on January 12, 2024, by Searchlight Pictures. "
            "It received critical acclaim and has grossed over $112 million worldwide on "
            "a budget of $35 million. "
            "Poor Things was named one of the top ten films of 2023 by the National "
            "Board of Review and the American Film Institute, and received various "
            "accolades, including four wins at the 96th Academy Awards, two wins at "
            "the 81st Golden Globe Awards, and five wins at the 77th British Academy Film "
            "Awards, with Stone winning Best Actress at each of these ceremonies.",
            "2023-12-08",
            142,
            "Drama",
        ),
        (
            "1001",
            "Oppenheimer",
            "Oppenheimer is a 2023 epic biographical thriller film[a] written, directed,"
            " and co-produced by Christopher Nolan.[8] It follows the life of J. Robert "
            "Oppenheimer, the American theoretical physicist who helped develop the "
            "first nuclear weapons during World War II. Based on the 2005 biography "
            "American Prometheus by Kai Bird and Martin J. Sherwin, the film chronicles "
            "Oppenheimer's studies, his direction of the Los Alamos Laboratory, and his "
            "fall from grace due to his 1954 security hearing. Cillian Murphy stars as "
            "Oppenheimer, alongside Robert Downey Jr. as the United States Atomic Energy "
            "Commission member Lewis Strauss. The ensemble supporting cast includes "
            "Emily Blunt, Matt Damon, Florence Pugh, Josh Hartnett, Casey Affleck, Rami "
            "Malek, and Kenneth Branagh. Oppenheimer was announced in September 2021. "
            "It is Nolan's first film not distributed by Warner Bros. Pictures since "
            "Memento (2000), due to his conflicts regarding the studio's simultaneous "
            "theatrical and HBO Max release schedule.[9] Murphy was the first cast member "
            "to sign on the following month, with the rest joining between November 2021 "
            "and April 2022. Pre-production began by January 2022, and filming took place "
            "from February to May. The cinematographer, Hoyte van Hoytema, used a "
            "combination of IMAX 65 mm and 65 mm large-format film, including, "
            "for the first time, scenes in IMAX black-and-white film photography. "
            "As with many of his previous films, Nolan used extensive practical effects,"
            " with minimal compositing. "
            "Oppenheimer premiered at Le Grand Rex in Paris on July 11, 2023, and was "
            "theatrically released in the US and the UK ten days later by Universal. "
            "Its concurrent release with Warner Bros.'s Barbie was the catalyst of the "
            '"Barbenheimer" phenomenon, encouraging audiences to see both films as a '
            "double feature. Oppenheimer grossed over $964 million worldwide, "
            "becoming the third-highest-grossing film of 2023, the highest-grossing "
            "World War II-related film, the highest-grossing biographical film, and "
            "the second-highest-grossing R-rated film. Among its many accolades, "
            "Oppenheimer won seven Academy Awards, including Best Picture, "
            "Best Director, Best Actor for Murphy, and Best Supporting Actor for Downey. "
            "The film also won five Golden Globe Awards (including Best Motion Picture – "
            "Drama) and seven British Academy Film Awards (including Best Film), and was "
            "named one of the top ten films of 2023 by the National Board of "
            "Review and the American Film Institute.",
            "2023-07-21",
            180,
            "Biography",
        ),
        (
            "1002",
            "Dune 2",
            "Dune: Part Two is a 2024 American epic science fiction film directed and produced by Denis "
            "Villeneuve, who co-wrote the screenplay with Jon Spaihts. The sequel to Dune (2021), it "
            "is the second of a two-part adaptation of the 1965 novel Dune by Frank Herbert. "
            "It follows Paul Atreides as he unites with the Fremen people of the desert planet Arrakis "
            "to wage war against House Harkonnen. Timothée Chalamet, Rebecca Ferguson, Josh Brolin, "
            "Stellan Skarsgård, Dave Bautista, Zendaya, Charlotte Rampling, and Javier Bardem reprise "
            "their roles from the first film, with Austin Butler, Florence Pugh, Christopher Walken, "
            "Léa Seydoux, and Souheila Yacoub joining the ensemble cast. Development began after Legendary "
            "Entertainment acquired film and television rights for the Dune franchise in 2016. Villeneuve "
            "signed on as director in 2017, intending to make a two-part adaptation of the novel due to "
            "its complexity. Production contracts were only secured for the first film, with the second "
            "film having to be green-lit based on the first's success. Villeneuve was concerned about "
            "the sequel's certainty after the first film had a simultaneous theatrical and HBO Max "
            "release but Warner Bros. Pictures assured him the sequel would happen if it performed "
            "well on HBO Max. After the critical and commercial success of the first film, Warner Bros. "
            "and Legendary green-lit Dune: Part Two in October 2021. Principal photography took place "
            "in Budapest, Italy, Jordan and Abu Dhabi between July and December 2022. Dune: Part Two "
            "was scheduled for a November 2023 release, but was delayed by the 2023 Hollywood labor "
            "disputes. The film had its world premiere at the Odeon Luxe Leicester Square, London, "
            "on February 15, 2024, and opened in the United States on March 1. It received praise from "
            "critics and has grossed $514 million worldwide, making it the highest-grossing film of "
            "2024.",
            "2024-03-01",
            155,
            "Science Fiction",
        ),
    ]

    movie_to_add = pd.DataFrame(
        extra_movies,
        columns=["id", "title", "overview", "release_date", "runtime", "genre"],
    )

    movies = pd.concat([movies, movie_to_add], ignore_index=True)

    here = Path(__file__)
    source = here.parent.parent.parent / "data/movies.parquet"
    movies.to_parquet(source, index=False)


def get_movies_dataset(sample: int = 0, *, local: bool = False) -> pd.DataFrame:
    if local:
        here = Path(__file__)
        source = here.parent.parent.parent / "data/movies.parquet"
    else:
        source = "https://raw.githubusercontent.com/xtreamsrl/movies-buddy/main/data/movies.parquet"

    if sample:
        return pd.read_parquet(source).sample(sample)
    return pd.read_parquet(source)


def get_embeddings(*, local: bool = False) -> npt.NDArray:
    if local:
        here = Path(__file__)
        source = here.parent.parent.parent / "data/movies_embeddings.npy"
    else:
        source = "https://raw.githubusercontent.com/xtreamsrl/movies-buddy/main/data/movies_embeddings.npy"

    return np.load(source)


def get_sentences_dataset() -> pd.DataFrame:
    sentences = [
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

    return pd.DataFrame(sentences, columns=["sentences", "field"])
