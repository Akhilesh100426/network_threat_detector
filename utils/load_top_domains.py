import pandas as pd

def load_top_domains(csv_path="tranco_8L2QV.csv"):
    """
    Loads domain names from a CSV file where domains are in Column B (index 1).
    Returns a set of lowercase domain strings for quick lookup.
    """
    try:
        df = pd.read_csv(csv_path, header=None, usecols=[1])  
        return set(df[1].str.strip().str.lower())
    except Exception as e:
        print(f"❌ Error loading top domains: {e}")
        return set()
