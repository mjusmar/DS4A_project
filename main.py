import uvicorn
from fastapi import FastAPI, UploadFile

from datasource import DataLoader
from model import Persona
from test import init_datasets, prediction

# proxy=""
# service_prefix = os.getenv('JUPYTERHUB_SERVICE_PREFIX')
# if service_prefix:
#     proxy = f'{service_prefix}proxy/8050/'

   
app = FastAPI(title='Test', description='API test', version= '1.0.1')

@app.on_event("startup")
async def startup_event():
    DataLoader.df_ruv, DataLoader.df_val = init_datasets(DataLoader.df_ruv, DataLoader.df_val)
    print('init')

@app.get('/')
async def index():
    return 'Server is working'

@app.post('/search')
async def structured_search(persona: Persona.BasePersona):
    """
    POST method that requests the information from a single person.
    
    @params person: structured data of a person
    @returns: Search results of the fuzzy search over a threshold
    """
    rate = prediction(DataLoader.df_ruv, DataLoader.df_val, persona)
    return {"prediction" : rate}

# @app.get('/batch/')
# async def batch_search(csv: UploadFile):
#     """
#     GET method that sends a batch request of several people to search.
    
#     @params csv: comma separated values of the  UploadFile
#     @returns: JSON of the fuzzy search 
#     """
#     return {"status":"In Construction"}
# #    prepared_data = prepare_csv_data(csv)
# #    return prepare_response(prediction)


if __name__ == "__main__":
    uvicorn.run(app, port=8050,host='0.0.0.0')