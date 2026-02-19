import os
import subprocess
import zipfile
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DATASET = "rishianand/devanagari-character-set"
ZIP_NAME = "devanagari-character-set.zip"
DATA_DIR = Path("data")

def download():
    print("⬇ Downloading dataset...")
    subprocess.check_call([
        "kaggle", "datasets", "download",
        "-d", DATASET
    ])

def extract():
    print("📦 Extracting dataset...")
    DATA_DIR.mkdir(exist_ok=True)
    with zipfile.ZipFile(ZIP_NAME, "r") as zip_ref:
        zip_ref.extractall(DATA_DIR)
    print("✅ Dataset extracted to ./data/")

if __name__ == "__main__":
    if not os.getenv("KAGGLE_USERNAME") or not os.getenv("KAGGLE_KEY"):
        raise EnvironmentError("KAGGLE_USERNAME or KAGGLE_KEY not set in .env")

    download()
    extract()
