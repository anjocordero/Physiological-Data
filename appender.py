import os
import pandas as pd
cwd = os.getcwd()

def append_labels(label_name, file):
    "Appends the column of labels in 'label_name' to the index of 'file' and transposes file"
    labels = pd.read_excel(label_name)
    data = pd.read_csv(file)

    index = labels.index
    data.index = index
    data = data.T
    data.to_csv("combined_" + file)

print("Before running, make sure the current folder contains only the file containing labels, and the physiological data files corresponding to the labels. If not, press CTRL + C to abort.")
label_name = input("Enter filename of the .xlsx file which contains labels: ")
files = os.listdir(cwd)

found = files.count(label_name)     
if found == 0:
    print(labels + " is not found in the curent directory.")
    exit()

files.remove(label_name)
files.remove('appender.py')
files.remove('.git')            # Remove if not cloned from git repo!
files.remove('README.md')       # Remove if not cloned from git repo!

for file in files:
    append_labels(label_name, file)