import os
import pandas as pd

# Define base directory (chapter6) dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_PATH = os.path.join(BASE_DIR, "input", "customers.csv")
CURATED_DIR = os.path.join(BASE_DIR, "curated")
CURATED_FILE_PATH = os.path.join(CURATED_DIR, "etl_customers.csv")

def run_etl():
    print("--- Running ETL Pipeline ---")
    
    # 1. Extract
    df = pd.read_csv(INPUT_PATH)
    print(f"[EXTRACT] Read {len(df)} records from source.")
    
    # 2. Transform
    df = df.drop_duplicates()
    df["Age"] = df["Age"].fillna(-1)
    df["City"] = df["City"].fillna("Unknown")
    print("[TRANSFORM] Cleaned duplicates and missing values.")
    
    # 3. Load
    os.makedirs(CURATED_DIR, exist_ok=True)
    df.to_csv(CURATED_FILE_PATH, index=False)
    print(f"[LOAD] Saved cleaned data to: {CURATED_FILE_PATH}\n")

if __name__ == "__main__":
    run_etl()