import os
import pandas as pd
cwd = os.getcwd()

def append_labels(labels, file):
    "Appends the column of labels in 'label_name' to the index of 'file' and transposes file"
    
    data = pd.read_csv(file)
    index = labels.index
    data.index = index

    if data.shape[0] == labels.shape[0]:
        data = data.T
        data.to_csv("combined_" + file)

    else:
        print("Mismatched size in file " + file)

print("Before running, make sure appender.py is in the same folder as the file containing the data and the labels to be added on to the data. If not, press CTRL + C to abort.")
label_name = input("Enter filename of the .xlsx file which contains labels: ")

included_extensions = ['.csv', '.xlsx']
files = [fn for fn in os.listdir(cwd) if any(fn.endswith(ext) for ext in included_extensions)] # Adds any files with .csv or .xlsx extensions to list

if files.count(label_name) == 0: # Check if file exists
    print(label_name + " is not found in the curent directory.")
    exit()

labels = pd.read_excel(label_name)
files.remove(label_name)

for file in files:
    append_labels(labels, file)

print("Completed!")