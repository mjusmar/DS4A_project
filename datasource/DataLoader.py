import os
import numpy as np
import pandas as pd

df_ruv = pd.read_csv(os.path.normpath(os.path.realpath("datasource/data/registros_ruv.csv")), encoding="latin")
df_val = pd.read_csv(os.path.normpath(os.path.realpath("datasource/data/registros_val.csv")), encoding="latin")

# print(df_ruv.head())