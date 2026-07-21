import os
import shutil
import pandas as pd

# Define base directory (chapter6) dynamically using script location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_PATH = os.path.join(BASE_DIR, "input", "customers.csv")
RAW_DIR = os.path.join(BASE_DIR, "raw")
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw_customers.csv")
CURATED_DIR = os.path.join(BASE_DIR, "curated")
CURATED_FILE_PATH = os.path.join(CURATED_DIR, "elt_customers.csv")

def run_elt():
    print("--- Running ELT Pipeline ---")
    
    # Step 1: Extract & Load Raw (Save unchanged copy to Raw Zone)
    os.makedirs(RAW_DIR, exist_ok=True)
    shutil.copyfile(INPUT_PATH, RAW_FILE_PATH)
    print(f"[LOAD RAW] Stored untouched raw file at: {RAW_FILE_PATH}")
    
    # Step 2: Extract from Raw Zone
    raw_df = pd.read_csv(RAW_FILE_PATH)
    print(f"[READ RAW] Read {len(raw_df)} records from Raw Zone.")
    
    # Step 3: Transform (Clean the raw data)
    clean_df = raw_df.drop_duplicates()
    clean_df["Age"] = clean_df["Age"].fillna(-1)
    clean_df["City"] = clean_df["City"].fillna("Unknown")
    print("[TRANSFORM] Removed duplicates and imputed missing values.")
    
    # Step 4: Load Curated (Save transformed version)
    os.makedirs(CURATED_DIR, exist_ok=True)
    clean_df.to_csv(CURATED_FILE_PATH, index=False)
    print(f"[LOAD CURATED] Saved cleaned data to: {CURATED_FILE_PATH}\n")

if __name__ == "__main__":
    run_elt()