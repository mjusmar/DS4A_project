import pandas as pd

def remove_accents(df_clean:pd.DataFrame):
    val_accents = {r'Á' : 'A',
                   r'É' : 'E', 
                   r'Í' : 'I',
                   r'Ó' : 'O', 
                   r'Ú' : 'U', 
                   r'Ü' : 'U', 
                   r'Ñ' : 'N',
                   r'' : 'A',
                   r'' : 'E', 
                   r'' : 'I',
                   r'¡' : 'I', 
                   r'Ç': 'I', 
                   r'¢' : 'O', 
                   r'£' : 'U', 
                   r'¤' : 'N'}
    df_clean.replace(r"[\t\n\r]", '', regex=True, inplace=True)
    df_clean = df_clean.apply(lambda x :x.str.upper())
    df_clean.replace(val_accents, regex=True, inplace=True)
    df_clean.replace(r'[^A-Z:]', '', regex=True, inplace=True)
    return df_clean

def dataset_clean(df_clean:pd.DataFrame):
    df_clean.replace('Ç\?|\?|¥', 'N', regex=True, inplace=True)
    df_clean.replace(r"[ .·'-\(\)]|&amp;apos;|&apos;|ERR/QUERY", '', regex=True, inplace=True)
    df_clean.fillna(value='', inplace=True)
    return df_clean