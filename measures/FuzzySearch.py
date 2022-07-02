import re
import pandas as pd

from model.Persona import BasePersona
from measures.Measure import cosine_matches

def clean_input(input_name: str):
    val_accents = {r'Á' : 'A',
                   r'É' : 'E', 
                   r'Í' : 'I',
                   r'Ó' : 'O', 
                   r'Ú' : 'U', 
                   r'Ü' : 'U', 
                   r'Ñ' : 'N'}
    for key, val in val_accents.items():
        if re.search(key, input_name):
            input_name = re.sub(key, val, input_name)
    input_name = re.sub(r'[^A-Z]', '', input_name)
    return input_name

def populate(df_res: pd.DataFrame):
    results = []
    for index, row in df_res.iterrows():
        person = {
                    'nombre1':row['NOM1'],
                    'nombre2':row['NOM2'],
                    'apellido1':row['APE1'],
                    'apellido2':row['APE2'],
                    'certidumbre':row['COS']}
        results.append(person)
    return results


def prediction(df_ruv: pd.DataFrame, persona: BasePersona):
    concat_name2 = (persona.name1 + persona.name2 + persona.surname1 + persona.surname2).upper()
    concat_name2 = clean_input(concat_name2)
    matches = cosine_matches(df_ruv, concat_name2)
    matches = populate(matches.to_frame().join(df_ruv))
    return matches