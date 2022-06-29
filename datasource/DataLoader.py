import os
import numpy as np
import pandas as pd

from signature.DataClean import *
from signature.Fingerprints import *
from measures.Measure import *
from model.Persona import *

class DataLoader():
    df_ruv = pd.read_csv(os.path.normpath(os.path.realpath("datasource/data/registros_ruv.csv")), encoding="latin")
    df_val = pd.read_csv(os.path.normpath(os.path.realpath("datasource/data/registros_val.csv")), encoding="latin")

def init_dataset(df: pd.DataFrame):

    df = remove_accents(df)
    df = dataset_clean(df)
    df = concat_name(df)
    df = phonetic_ids(df)
    df = lexicographic_ids(df)
    df = vectorial_ids(df)

    return df