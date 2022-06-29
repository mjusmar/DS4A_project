import random
from signature.DataClean import *
from signature.Fingerprints import *
from measures.Measure import *
from model.Persona import *

def init_dataset(df: pd.DataFrame):

    df = remove_accents(df)
    df = dataset_clean(df)
    df = concat_name(df)
    df = phonetic_ids(df)
    df = lexicographic_ids(df)
    df = vectorial_ids(df)

    return df

def prediction(df_ruv, df_val, persona: BasePersona):
    concat_name2 = persona.name1 + persona.name2 + persona.surname1 + persona.surname2
    matches = cosine_matches(df_ruv, concat_name2)
    return matches

