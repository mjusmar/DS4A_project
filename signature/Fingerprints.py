import pandas as pd
import phonetics as phn

def concat_name(df:pd.DataFrame):
    df["FULLNAME"] = df["NOM1"]+df["NOM2"]+df["APE1"]+df["APE2"]
    return df

def phonetic_ids(df):
    df["NAMES_PHN"] = df["FULLNAME"].apply(lambda x : phn.metaphone(x))
    return df

def lexicographic_ids(df):
    letter_replacer= {r"V":"B", r"Y":"J", r"Z":"S", r"X":"S", r"LL":"J"}
    df["NAMES_LEX"] = df["FULLNAME"].replace(letter_replacer, regex=True)
    return df
