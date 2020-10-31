import pandas as pd
data = pd.read_csv("file.csv")
df = pd.DataFrame(data)
print(df)
#remove all column duplicate by default
#print(df.duplicated())
print(df.drop_duplicates(keep='first'))
column_list = list(df.columns)
#print(column_list)
#we will prepare list of columns to be excluded from process
excluded_columns = []
#we will find what columns to undergo duplicate removal procedure and we will remove excluded items from main list
column_to_process =[x for x in column_list if x not in excluded_columns]
#we can choose which values to keep first or last
what_to_keep = 'first'
#we can remove some columns from the column list if we think they are not to be opted in for duplicates removal
dropped_df = df.drop_duplicates(subset=column_to_process, keep=what_to_keep)
print(dropped_df)