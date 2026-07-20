import os

# Locate the data directory relative to this script
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")

print("--- Data Format Classifier Pipeline ---")
print(f"Scanning directory: {data_dir}\n")

# Dictionary mapping extensions to their structural data types
DATA_TYPE_MAPPING = {
    '.csv': 'Structured',
    '.json': 'Semi-Structured',
    '.xml': 'Semi-Structured',
    '.pdf': 'Unstructured',
    '.jpg': 'Unstructured',
    '.png': 'Unstructured',
    '.txt': 'Unstructured'
}

try:
    # List all files inside the target data folder
    files = os.listdir(data_dir)
    
    if not files:
        print("[Warning] No files found inside the data directory.")
        
    for filename in sorted(files):
        # Ignore hidden system files like .DS_Store on macOS
        if filename.startswith('.'):
            continue
            
        # Extract the file extension (e.g., '.csv', '.json')
        _, extension = os.path.splitext(filename)
        extension = extension.lower()
        
        # Classify based on mapping dictionary
        classification = DATA_TYPE_MAPPING.get(extension, 'Unknown Data Type')
        
        # Print matching output in a clean, aligned layout
        print(f"{filename:<16} -> {classification}")

except FileNotFoundError:
    print(f"[Error] Directory not found at: {data_dir}. Please check your folders.")