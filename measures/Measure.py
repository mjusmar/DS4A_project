import collections
import numpy as np
import pandas as pd
import re
from numpy import dot
from numpy.linalg import norm

from model.Persona import BasePersona

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
    innermask = df_ruv.NAMES_VEC.apply(lambda x:cosine_difference(x, vecpattern))
    return innermask.nlargest(5).sort()

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

def prediction(df_ruv: pd.DataFrame, persona: BasePersona):
    concat_name2 = (persona.name1 + persona.name2 + persona.surname1 + persona.surname2).upper()
    concat_name2 = clean_input(concat_name2)
    matches = cosine_matches(df_ruv, concat_name2)
    return matches