from pathlib import Path
import pandas as pd

base_p = Path(__file__)
base_path = Path(__file__).parent
db_folder_path = Path(__file__).parent.parent.joinpath('DataBase',"asd.csv")

print("original",base_p)
print("parent",base_path)
print(db_folder_path)

def return_df(path):
    return pd.read_csv(path)

def fun1():
    return return_df(db_folder_path)