
import os
import sys
import json
import weaviate
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.utils import connect_to_weaviate, load_schema_from_file


try:
    client = connect_to_weaviate()
    schema = load_schema_from_file()
    client.schema.delete_all()
    client.schema.create(schema)

except Exception as e:
    print(f'ExceptionL {e}')





