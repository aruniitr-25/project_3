import sys
import pandas as pd

def main():
    print("Reading data into Pandas DataFrame...", file=sys.stderr)
    
    try:
        # 1. Read the entire stream into a DataFrame
        #    We assume standard BED columns: 0=Chr, 1=Start, 2=End
        #    usecols=[1, 2] reads only Start and End to save memory
        df = pd.read_csv(sys.stdin, sep="\t", header=None, usecols=[1, 2], names=["start", "end"])
        
        # 2. Vectorized Calculations (Very Fast)
        #    Calculate Length (Y)
        df["length"] = df["end"] - df["start"]
        
        #    Calculate Midpoint (X)
        df["offset"] = (df["start"] + df["end"]) // 2
        
        # 3. Filter
        #    Keep fragments between 0 and 1000bp
        df = df[(df["length"] > 0) & (df["length"] <= 1000)]
        
        # 4. The "Group By" Magic
        #    Group by (offset, length) and count the size of each group
        matrix = df.groupby(["offset", "length"]).size().reset_index(name="count")
        
        # 5. Output
        #    Pandas handles the tab-separation automatically
        matrix.to_csv(sys.stdout, sep="\t", index=False)
        
    except pd.errors.EmptyDataError:
        print("Error: No data found.", file=sys.stderr)

if __name__ == "__main__":
    main()