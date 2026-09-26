import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files(
    "heptapod/titanic",
    path="data/raw",
    unzip=True
)

print("Download complete!")
