# Physiological Data
Takes the labels from an .xlsx file in the current directory and applies it to all .csv and .xlsx files in the current directory with a matching number of rows. Files are then combined, transposed, and organized by index. This program should run properly as long as there are the correct number of columns in the data files.

## Setup
Running this software requires python, pip, pandas, and xlrd. It should be compatible with all operating systems, however python is a little more complicated on MacOS. You might have to look up how to install everything properly. There might be some missing dependencies depending on your OS, but you should be able to install most of them with pip (or pip3), the same way you will in the following directions.

### Python
If you don't have python installed, you can download it from https://www.python.org/

### pip
Pip is a program that installs python extensions and libraries, that we'll use to install the rest of the software. It should come included with a new install of python but if not, open a command prompt and type:
> sudo apt-get pip

### pandas
Pandas is a data science library used to handle excel documents in python. To install this, open a command prompt and type:
> pip install pandas

### xlrd
xlrd is needed by pandas to load excel files. I don't know if it comes included, but I had to install it on my own. To install this, open a command prompt and type:
> pip install xlrd

### openpyxl
openpyxl is another dependency that I only needed to install on my MacOS machine. You can install it the same way:
> pip install openpyxl

Written by Anjo Gabriel Cordero
