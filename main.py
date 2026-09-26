import subprocess
import sys

def run_step(script_name, description):
    print(f"\n{'='*50}")
    print(f"STEP: {description}")
    print(f"{'='*50}")
    result = subprocess.run([sys.executable, script_name])
    if result.returncode != 0:
        print(f"❌ {script_name} failed! Stopping pipeline.")
        exit(1)
    print(f"✅ {description} complete")

if __name__ == "__main__":
    print("Starting full data pipeline...\n")

    # Kaggle pipeline
    run_step("download_kaggle.py", "Extract Titanic data from Kaggle")
    run_step("transform.py", "Clean Titanic data")
    run_step("load_mongo.py", "Load Titanic data into MongoDB")

    # HuggingFace pipeline
    run_step("extract_huggingface.py", "Extract IMDB reviews from Hugging Face")
    run_step("transform_huggingface.py", "Clean IMDB data")
    run_step("load_imdb_mongo.py", "Load IMDB data into MongoDB")

    print("\n🎉 Full pipeline completed successfully!")