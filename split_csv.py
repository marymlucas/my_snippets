'''
For splitting large CSV files into smaller more manageable files.
Using tkinter for the file dialog GUI.

Requirements: Python 3.x, Pandas and tkinter librarys
e.g. Excel can only load 1 million rows at a time
Ideally place this script in the same folder as the file to be split but can be elsewhere

USAGE: 
Modify chunk_size parameter to the number of rows you want each individual file to be
In the command line/shell navigate to the folder and run the command *python split_csv.py*
This should open a file dialog interface to select the file to be split.
'''

import pandas as pd 
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

chunk_size = 10000000  # modify this to the number of rows you want in each file
batch_no = 1

file_name = filedialog.askopenfilename()
namepart = os.path.splitext(file_name)[0]


for chunk in pd.read_csv(file_name, chunksize = chunk_size, low_memory=False):
	print("Now writing file no." + str(batch_no) + "...")
	chunk.to_csv(namepart + "_" + str(batch_no) + ".csv", index = False)
	batch_no +=1

