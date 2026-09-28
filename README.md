# Data Pipeline: Kaggle & Hugging Face to MongoDB Atlas

A Python ETL (Extract, Transform, Load) pipeline that pulls datasets from Kaggle and Hugging Face, cleans them with pandas, and loads them into a MongoDB Atlas cloud database.

## What it does

- **Extract**: Downloads the Titanic dataset from Kaggle and the IMDB movie reviews dataset from Hugging Face
- **Transform**: Cleans both datasets with pandas (removes junk columns, duplicates and missing values, renames fields)
- **Load**: Loads the cleaned data into MongoDB Atlas using upserts, so re-running the pipeline never creates duplicates

## Tech stack

- Python
- pandas
- Kaggle API
- Hugging Face `datasets`
- MongoDB Atlas and PyMongo
- python-dotenv

## Project structure

```
data-pipeline-project/
├── main.py                     # Runs the whole pipeline
├── download_kaggle.py          # Extract: Kaggle Titanic dataset
├── transform.py                # Transform: clean Titanic data
├── load_mongo.py               # Load: Titanic into MongoDB
├── extract_huggingface.py      # Extract: Hugging Face IMDB dataset
├── transform_huggingface.py    # Transform: clean IMDB data
├── load_imdb_mongo.py          # Load: IMDB reviews into MongoDB
├── explore_data.py             # Exploring the raw data
└── .gitignore                  # Keeps secrets and raw data out of Git
```

## How to run it

1. Install the dependencies:
```
   pip install kaggle datasets pandas pymongo python-dotenv
```
2. Create a `.env` file (not included, for security) containing:
```
   MONGO_URI=your_mongodb_connection_string
```
3. Set your Kaggle API token as the `KAGGLE_API_TOKEN` environment variable.
4. Run the full pipeline:
```
   python main.py
```

## What I learned

This was my first end-to-end data engineering project. I learned to work with external APIs, keep credentials secure with environment variables, clean messy real-world data with pandas, and load data into a cloud NoSQL database with duplicate protection.