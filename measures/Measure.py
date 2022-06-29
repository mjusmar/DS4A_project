import collections
import numpy as np

def word2vec(word):
    prefix = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

    # Count the number of characters in each word.
    count_characters = collections.Counter(prefix+word)
    base_characters = collections.Counter(prefix)
    
    count_characters.subtract(base_characters)
    

    # Gets the set of characters and calculates the "length" of the vector.
    set_characters = set(count_characters)

    length = np.sqrt(sum(c*c for c in count_characters.values()))

    return count_characters, set_characters, length, word

def cosine_similarity(vector1, vector2, ndigits):
    
    # Get the common characters between the two character sets
    common_characters = vector1[1].intersection(vector2[1])

    # Sum of the product of each intersection character.
    product_summation = sum(vector1[0][character] * vector2[0][character] for character in common_characters)

    # Gets the length of each vector from the word2vec output.
    length = vector1[2] * vector2[2]

    # Calculates cosine similarity and rounds the value to ndigits decimal places.
    if length == 0:
        # Set value to 0 if word is empty.
        similarity = 0
    else:
        similarity = round(product_summation/length, ndigits)

    return similarity