import pandas as pd
import os
from datasets import load_dataset

def load_file():
    print(f"----- ⌛ Loading csv file -----")
    return load_dataset('data/')

def save(data : pd.DataFrame,
         file_name : str):
    with open(f"{os.environ['CSV_FILE_PATH']}/{file_name}", 'a') as f:
        data.to_csv(f, mode='a', header=f.tell()==0)
