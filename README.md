 Genomic Fragment Density Calculator

This script is a high-performance Python utility that reads genomic interval data (like a BED file) from standard input (stdin) and calculates the density of fragments based on their midpoint offset and length.

It uses vectorized operations from the pandas library to quickly process large streaming datasets, making it ideal for integration into bioinformatics pipelines. The output is a matrix of offset, length, and the count of fragments that share those exact properties.

 Features

High Performance: Leverages Pandas vectorized arithmetic (df["end"] - df["start"]) and the highly optimized groupby().size().

Standard I/O: Reads from stdin and writes the resulting matrix to stdout.

Focused Data Processing: Only reads columns 1 and 2 (Start and End) from the input to optimize memory usage.

Filtering: Automatically filters out fragments with a length greater than 1000 bp.

Matrix Output: Generates a ready-to-plot TSV matrix used for downstream visualization (e.g., heatmaps).

 Requirements

This script requires the pandas library.

pip install pandas


 Usage

Pipe your unsorted or sorted genomic interval data (assuming standard 0-based, half-open format where columns 1 and 2 are Start and End) into the script.

Example

# Assuming your input data is in 'fragments.bed'
cat fragments.bed | python your_script_name.py > density_matrix.tsv


Input Data Format (Expected)

The script expects tab-separated input where:

Column Index

0

1

2

3...

Content

Chromosome

Start

End

Other Data

Output Data Format (Generated)

The script writes a tab-separated matrix to stdout with the following columns:

Column Name

Calculation

Description

offset

(start + end) // 2

The integer midpoint of the genomic fragment (X-axis for a density plot).

length

end - start

The calculated length of the fragment (Y-axis for a density plot).

count

Count

The total number of fragments that share this specific offset and length combination.
 Core Logic

The script performs three core vectorized calculations:

Length: df["length"] = df["end"] - df["start"]

Offset: df["offset"] = (df["start"] + df["end"]) // 2 (Integer division for midpoint)

Aggregation: df.groupby(["offset", "length"]).size() counts the number of fragments at each unique (midpoint, length) coordinate.

