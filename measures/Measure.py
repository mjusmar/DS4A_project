import collections
import numpy as np
import pandas as pd

from numpy import dot
from numpy.linalg import norm



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
    return innermask.nlargest(5).sort_values(ascending=False)