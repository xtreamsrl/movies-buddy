# Your AI-Powered Movies Buddy

## 🚀 Let's get started!

**name** | **open in**
:-----: | :-------:
[Explore Embeddings](./notebooks/01-embeddings.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/01-embeddings.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/xtreamsrl/movies-buddy/blob/main/notebooks/01-embeddings.ipynb) [![SageMaker](https://raw.githubusercontent.com/roboflow-ai/notebooks/main/assets/badges/sage-maker.svg)](https://studiolab.sagemaker.aws/import/github/xtreamsrl/movies-buddy/blob/main/notebooks/01-embeddings.ipynb)
[What are Vector Databases?](./notebooks/02-vector-database.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/02-vector-database.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/xtreamsrl/movies-buddy/blob/main/notebooks/02-vector-database.ipynb) [![SageMaker](https://raw.githubusercontent.com/roboflow-ai/notebooks/main/assets/badges/sage-maker.svg)](https://studiolab.sagemaker.aws/import/github/xtreamsrl/movies-buddy/blob/main/notebooks/02-vector-database.ipynb)
[Explore Embeddings](./notebooks/03-rag-from-scratch.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/03-rag-from-scratch.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/xtreamsrl/movies-buddy/blob/main/notebooks/03-rag-from-scratch.ipynb) [![SageMaker](https://raw.githubusercontent.com/roboflow-ai/notebooks/main/assets/badges/sage-maker.svg)](https://studiolab.sagemaker.aws/import/github/xtreamsrl/movies-buddy/blob/main/notebooks/03-rag-from-scratch.ipynb)

## 🤗 How to contribute

1. Clone the repo:

```bash
git clone git@github.com:xtreamsrl/movies-buddy

gh repo clone xtreamsrl/movies-buddy
```

> [!NOTE]
> The project uses Python 3.11

1. Install PDM

2. Run the following:

```bash
pdm install --group=:dev
```

3. Check if everything works:

```bash
pdm run python -c "from movies_buddy import version; print(version.__version__)"
```

4. Install `pre-commit` and `nbstripout` hooks:

```bash
pdm run pre-commit install --install-hooks
pdm run nbstripout --install
```
