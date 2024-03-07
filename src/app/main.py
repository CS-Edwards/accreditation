
import os
import json
import weaviate
from dotenv import load_dotenv


load_dotenv()

#Weaviate Cloud Service URL (WCS)
URL = os.getenv("WCSURL") 

#WCS API Key
APIKEY = os.getenv("WCSAPI")

#OPENAI API Key
OPENAI = os.getenv("OPENAIKEY")

client = weaviate.Client(
    url= URL,
    auth_client_secret = weaviate.auth.AuthApiKey(APIKEY),
    additional_headers ={
        "X-OPENAI-Api-Key": OPENAI
    }
)

if not client.is_live():
    raise ValueError('Weaviate Client is not live')
else:
    print('Successfully connected to WCS')


#
# Database Schema
#
    
SCHEMA_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "config", "schema_v0.json"))

try:
    # Load chema from file
    with open(SCHEMA_FILE_PATH,'r') as schema_file:
        schema = json.load(schema_file)
        print(schema)

except FileNotFoundError:
    print(f'Error: Schema file {SCHEMA_FILE_PATH} not found')

client.schema.delete_all()
client.schema.create(schema)


