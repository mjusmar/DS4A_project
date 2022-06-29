import uvicorn
from io import BytesIO
from fastapi import FastAPI, UploadFile

from datasource import DataLoader
from model.Persona import *
from test import *

# proxy=""
# service_prefix = os.getenv('JUPYTERHUB_SERVICE_PREFIX')
# if service_prefix:
#     proxy = f'{service_prefix}proxy/8050/'

   
app = FastAPI(title='Test', description='API test', version= '1.0.1')

@app.on_event("startup")
async def startup_event():
    DataLoader.df_ruv = init_dataset(DataLoader.df_ruv)
    DataLoader.df_val = init_dataset(DataLoader.df_val)
    print('init')
    # print(DataLoader.df_ruv.head())


@app.get('/')
async def index():
    return 'Server is working'

@app.post('/search')
async def structured_search(persona: BasePersona):
    """
    POST method that requests the information from a single person.
    
    @params person: structured data of a person
    @returns: Search results of the fuzzy search over a threshold
    """
    matches = prediction(DataLoader.df_ruv, DataLoader.df_val, persona)
    return {"matches" : matches}

@app.post('/batch')
async def batch_search(csv: UploadFile):
    """
    POST method that sends a batch request of several people to search.
    
    @params csv: comma separated values of the  UploadFile
    @returns: JSON of the fuzzy search 
    """
    # data = csv.reader(codecs.iterdecode(file.file,'utf-8'))

    bytes_data = csv.file.read()
    df = pd.read_csv(BytesIO(bytes_data), encoding="latin")

    return  {"status":"In Construction"}
# #    prepared_data = prepare_csv_data(csv)
# #    return prepare_response(prediction)


if __name__ == "__main__":
    uvicorn.run(app, port=8050,host='0.0.0.0')