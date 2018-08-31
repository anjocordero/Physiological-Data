def append_labels(labels, file):
    "Appends the column of labels in 'labels' to the right side of 'file'"

import os
cwd = os.getcwd()
import os
import pandas as pd
cwd = os.getcwd()

print("Before running, make sure the current folder contains only the file containing labels, and the physiological data files corresponding to the labels. If not, press CTRL + C to abort.")
labels = input("Enter filename of file which contains labels: ")
files = os.listdir(cwd)

found = files.count(labels)     
if found == 0:
    print(labels + " is not found in the curent directory.")
    exit()

files.remove(labels)
files.remove('appender.py')
files.remove('.git')            # Remove if not cloned from git repo!
files.remove('README.md')       # Remove if not cloned from git repo!

for file in files:
    append_labels(labels, file)