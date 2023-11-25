# importing the required modules
import glob
import pandas as pd
import os

# specifying the path to excel files
cwd = os.getcwd()
path = f'{cwd}/inputs/'
output_dir = f'{cwd}\output'

# csv files in the path
file_list = glob.glob(path + "/*.xlsx")

# list of excel files we want to merge.
# pd.read_excel(file_path) reads the excel
# data into pandas dataframe.
excel_list = []

for file in file_list:
	excel_list.append(pd.read_excel(file))

# create a new dataframe to store the
# merged excel file.
excl_merged = pd.DataFrame()

for excl_file in excel_list:
	
	# appends the data into the excl_merged
	# dataframe.
	excl_merged = excl_merged._append(
	excl_file, ignore_index=True)

# exports the dataframe into excel file with
# specified name.
excl_merged.to_excel('total.xlsx', index=False)
dd = pd.read_excel('total.xlsx').drop_duplicates()
dd = dd.fillna('n/a')

output_dir = f'{cwd}\output'
dd.to_excel(f'{output_dir}\Factiva.xlsx', index=False)

