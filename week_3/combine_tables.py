#import the modules
import os
import pandas as pd
# #read the path
# cwd = os.path.abspath('./data')
# #list all the files from the directory
# file_list = os.listdir(cwd)
# print(file_list)



# df_append = pd.DataFrame()
# #append all files together
# for file in file_list:
#             df_temp = pd.read_csv('./data/'+file, compression='gzip')
#             df_append = df_append.append(df_temp, ignore_index=True)
# df_append

# df_append.to_csv('./data/fhv_2019.csv.gz', compression='gzip') 


import os
import pandas as pd

# 1. defines path to csv files
path = "./data/"

# 2. creates list with files to merge based on name convention
file_list = [path + f for f in os.listdir(path)]

# 3. creates empty list to include the content of each file converted to pandas DF
csv_list = []
 
# 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file, compression='gzip').assign(File_Name = os.path.basename(file)))

# 5. merges single pandas DFs into a single DF, index is refreshed 
csv_merged = pd.concat(csv_list, ignore_index=True)

# 6. Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv(path + 'fhv_2019.csv.gz', index=False, compression='gzip')
