import pandas as pd

from model.Persona import BasePersona
from measures.Measure import clean_input, cosine_matches, phonetic_matches

def populate(df_res: pd.DataFrame):
    results = []
    for index, row in df_res.iterrows():
        person = {
                    'cedula':row['DOC_RUV'],
                    'nombre1':row['NOM1'],
                    'nombre2':row['NOM2'],
                    'apellido1':row['APE1'],
                    'apellido2':row['APE2'],
                    'puntaje': round(row['COS'],2),
                    'fonetica':round(row['PHN'],2),
                    'puntaje_total':round(row['COS']*row['PHN'],2)
                    }
        results.append(person)
    return results

def order_by_phonetic(results):
    results = sorted(results, key=lambda k: k['puntaje_total'], reverse=True)
    return results

def prediction(df_ruv: pd.DataFrame, persona: BasePersona):
    persona = clean_input(persona)
    concat_name2 = (persona.name1 + persona.name2 + persona.surname1 + persona.surname2)
    matches = cosine_matches(df_ruv, concat_name2)
    matches = phonetic_matches(matches, persona)
    results = populate(matches)
    results_order = order_by_phonetic(results)
    return results_order