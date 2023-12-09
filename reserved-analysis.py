import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("~/Downloads/oci-data-120723.xlsx")

# Fill NaN entries with 0
df.fillna(0, inplace=True)
df = df[:-1]        # Deleting last row since that is not required

# Define the GPU mapping dictionary
gpu_mapping = {
    "BM.GPU.B4.8": {"GPU Type": "A100 40 GB", "# of GPUs": 8},
    "BM.GPU4.8": {"GPU Type": "A100 40 GB", "# of GPUs": 8},
    "BM.GPU.A100-v2.8": {"GPU Type": "A100 80 GB", "# of GPUs": 8},
    "BM.GPU.A10.4": {"GPU Type": "A10", "# of GPUs": 4},
    "x10-2c.112.2048.gpu": {"GPU Type": "H100", "# of GPUs": 8},
}

# Removing any unintended space from the SHAPE column values
df['SHAPE'] = df['SHAPE'].str.strip()

# Create new columns in the DataFrame based on the GPU mapping
df["GPU Type"] = df["SHAPE"].map(lambda x: gpu_mapping[x]["GPU Type"] if x in gpu_mapping else "Unknown")
df["# of GPUs"] = df["SHAPE"].map(lambda x: gpu_mapping[x]["# of GPUs"] if x in gpu_mapping else 0)

# Calculate the Total number of GPUs allocated
df["Total number of GPUs allocated"] = df["Total Count"] * df["# of GPUs"]

# Calculate the Total number of GPUs available
df["Total number of GPUs available"] = df["Available Host Count"] * df["# of GPUs"]

pivot_df = df.pivot_table(index="GPU Type", values=["Total number of GPUs allocated", "Total number of GPUs available"], aggfunc="sum")

print(df)
print(pivot_df)

# Create a Pandas ExcelWriter object
with pd.ExcelWriter("output_file.xlsx") as writer:
    # Write the df DataFrame to the first sheet
    df.to_excel(writer, sheet_name="DataFrame", index=False)
    
    # Write the pivot_df DataFrame to the second sheet
    pivot_df.to_excel(writer, sheet_name="PivotTable", index=True)

    gpu_mapping_df = pd.DataFrame.from_dict(gpu_mapping, orient='index')
    gpu_mapping_df.to_excel(writer, sheet_name="GPU Mapping")