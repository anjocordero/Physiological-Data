# Physiological Data
Takes the labels from an .xlsx file in the current directory and applies it to all .csv and .xlsx files in the current directory with a matching number of rows. Combined files are then transposed.

## Setup
Running this software requires python, pip, pandas, and xlrd. It should be compatible with all operating systems.

### Python
If you don't have python installed, you can download it from https://www.python.org/

### pip
Pip is a program that installs python extensions and libraries. It should come included with a new install of python but if not, open a command prompt and type:
> sudo apt-get pip

### pandas
Pandas is a data science library used to handle excel documents in python. To install this, open a command prompt and type:
> pip install pandas

### xlrd
xlrd is needed by pandas to load excel files. I don't know if it comes included, but I had to install it on my own. To install this, open a command prompt and type:
> pip install xlrd

Written by Anjo Gabriel Cordero
