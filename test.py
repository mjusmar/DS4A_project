import random
from signature import DataClean, Fingerprints
from measures import Measure
from model import Persona

def init_datasets(df_ruv, df_val):

    df_ruv = DataClean.remove_accents(df_ruv)
    df_ruv = DataClean.dataset_clean(df_ruv)
    df_ruv = Fingerprints.concat_name(df_ruv)
    df_ruv = Fingerprints.phonetic_ids(df_ruv)
    df_ruv = Fingerprints.lexicographic_ids(df_ruv)

    df_val = DataClean.remove_accents(df_val)
    df_val = DataClean.dataset_clean(df_val)
    df_val = Fingerprints.concat_name(df_val)
    df_val = Fingerprints.phonetic_ids(df_val)
    df_val = Fingerprints.lexicographic_ids(df_val)

    # print(df_ruv.head())
    # print(df_val.head())
    return df_ruv, df_val

def prediction(df_ruv, df_val, persona: Persona.BasePersona):
    print(persona.name)
    num_r1 = random.randint(0, df_ruv['NOM1'].size - 1)
    num_r2 = random.randint(0, df_val['NOM1'].size - 1)

    name_ruv = df_ruv['NOM1'][num_r1]
    name_val = df_val['NOM1'][num_r2]

    print('RUV name:', name_ruv)
    print('Validation name:', name_val)

    vector1 = Measure.word2vec(name_ruv)
    vector2 = Measure.word2vec(name_val)

    cosine_similarity_rate = Measure.cosine_similarity(vector1, vector2, 3)

    print('Cosine similarity rate:', cosine_similarity_rate)

    return cosine_similarity_rate

