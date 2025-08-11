#!/usr/bin/env python3
"""
curate_metadata.py
Run:
    python scripts/curate_metadata.py --input data/sample_metadata.csv --output data/curated_sample.csv
"""

import argparse
import pandas as pd

def curate(df: pd.DataFrame) -> pd.DataFrame:
    # Standardize 'sex' column
    if 'sex' in df.columns:
        df['sex_original'] = df['sex']
        df['sex'] = df['sex'].astype(str).str.lower().map({
            'male': 'male', 'm': 'male',
            'female': 'female', 'f': 'female'
        }).fillna('unknown')
    
    # Standardize 'species' column
    if 'species' in df.columns:
        df['species_original'] = df['species']
        df['species'] = df['species'].astype(str).str.strip().str.title()
    
    # Standardize 'age' column
    if 'age' in df.columns:
        df['age_original'] = df['age']
        df['age'] = df['age'].astype(str).str.extract(r'(\d+)').fillna('unknown')
    
    # Example: normalize disease field
    if 'disease_summary' in df.columns:
        df['disease_summary_original'] = df['disease_summary']
        df['disease_summary'] = df['disease_summary'].astype(str).str.strip().str.title()
    
    return df

def main():
    parser = argparse.ArgumentParser(description="Curate metadata CSV file")
    parser.add_argument('--input', required=True, help="Path to input CSV file")
    parser.add_argument('--output', required=True, help="Path to save curated CSV")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    curated_df = curate(df)
    curated_df.to_csv(args.output, index=False)
    print(f"✅ Curated metadata saved to: {args.output}")

if __name__ == "__main__":
    main()
