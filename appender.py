import os
import pandas as pd
cwd = os.getcwd()

print("Before running, make sure appender.py is in the same folder as the file containing the data and the labels to be added on to the data. If not, press CTRL + C to abort.")
label_name = input("Enter filename of the .xlsx file which contains labels: ")

included_extensions = ['.csv', '.xlsx']
files = [fn for fn in os.listdir(cwd) if any(fn.endswith(ext) for ext in included_extensions)] # Adds any files with .csv or .xlsx extensions to list

if files.count(label_name) == 0: # Check if file exists
    print(label_name + " is not found in the curent directory.")
    exit()

labels = pd.read_excel(label_name)

files.remove(label_name)
index = labels.index

combined_file = labels


if len(files) != 0:
    #if data.shape[0] == combined_file.shape[0]:
        data = pd.read_csv(files[0])
        data.index = index
        data = data.T
        """ data = data.reset_index()
        data.index = [files[0]] * len(data) """
        arrays = list(data.index), [files[0]] * len(data)
        tuples = list(zip(*arrays))
        multi_index = pd.MultiIndex.from_tuples(tuples, names=['Index', 'File'])
        combined_file = data
        combined_file.index = multi_index
        files.remove(files[0])


for file in files:
    data = pd.read_csv(file)

    #if data.shape[0] + 1 == combined_file.shape[1]:
    data.index = index
    data = data.T
    """ data = data.reset_index()
    data.index = [file] * len(data) """
    arrays = list(data.index), [file] * len(data)
    tuples = list(zip(*arrays))
    multi_index = pd.MultiIndex.from_tuples(tuples, names=['Index', 'File'])
    data.index = multi_index
    combined_file = pd.concat([combined_file, data], axis=0, join='outer', sort=False)

    #else:
    #    print("Mismatched size in file " + file)

combined_file.sort_index(inplace=True)
combined_file.to_excel("combined_" + label_name)

for index in combined_file.index:
    index_name = index[0].replace('/', '_')
    index_name = index_name.replace('\\', '_')
    combined_file.loc[slice(index[0], index[0]), :].to_excel(index_name + '_' + label_name)

print("Completed!")