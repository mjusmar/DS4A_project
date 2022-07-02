import re
import collections
import numpy as np
import pandas as pd
import phonetics as phn

from numpy import dot
from numpy.linalg import norm
from model.Persona import BasePersona

def clean_input(persona:BasePersona):
    persona.name1 = clean_field(persona.name1)
    persona.name2 = clean_field(persona.name2)
    persona.surname1 = clean_field(persona.surname1)
    persona.surname2 = clean_field(persona.surname2)
    return persona

def clean_field(input_name: str):
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
    input_name = input_name.upper()
    input_name = re.sub(r'[^A-Z]', '', input_name)
    return input_name

def word2vec(word):
    prefix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Count the number of characters in each word.
    count_characters = collections.Counter(prefix+word)    
    count_characters.subtract(collections.Counter(prefix))
    
    # Gets the set of characters and calculates the "length" of the vector.
    set_characters = set(count_characters)

    # Frobenius vectorial norm using numpy library
    length = np.linalg.norm(tuple(count_characters.values()))  

    return np.array(list(count_characters.values()))#.reshape(1, -1) #, set_characters, length, word

def cosine_difference(vector1, vector2):
    if (vector1.any() and vector2.any()):        
        return dot(vector1, vector2)/(norm(vector1)*norm(vector2)).sum()
    return 0

def cosine_matches(df_ruv: pd.DataFrame, pattern: str):
    vecpattern = word2vec(pattern)
    innermask = df_ruv.NAMES_VEC.apply(lambda x:cosine_difference(x, vecpattern)*100).rename("COS")
    results = innermask.nlargest(5).sort_values(ascending=False).to_frame()
    return results.join(df_ruv)

def phonetic_difference(per:BasePersona, pattern:str):
    phname1 = phn.metaphone(per.name1)
    phname2 = phn.metaphone(per.name2)
    phsurname1 = phn.metaphone(per.surname1)
    phsurname2 = phn.metaphone(per.surname2)
    return (bool(re.search(phname1, pattern)) + bool(re.search(phname2, pattern)) + bool(re.search(phsurname1, pattern)) + bool(re.search(phsurname2, pattern)))/4
    
def phonetic_matches(df_ruv: pd.DataFrame, persona:BasePersona):
    innermask = df_ruv.NAMES_PHN.apply(lambda x:phonetic_difference(persona, x)).rename("PHN").to_frame()
    return innermask.join(df_ruv)