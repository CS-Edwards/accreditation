import os
import json
import weaviate
from dotenv import load_dotenv
from typing import Any, Dict



def connect_to_weaviate() -> weaviate.Client:
    """
    Connects to Weaviate Cloud Service

    Returns:
        weaviate.Client: The Weaviate client instance.
    
    Raises:
        ValueError: If the Weaviate client is not live.
    """
    load_dotenv()
    URL: str = os.getenv("WCSURL")
    APIKEY: str = os.getenv("WCSAPI")
    OPENAI: str = os.getenv("OPENAIKEY")

    client: weaviate.Client = weaviate.Client(
        url=URL,
        auth_client_secret=weaviate.auth.AuthApiKey(APIKEY),
        additional_headers={
            "X-OPENAI-Api-Key": OPENAI
        }
    )

    if not client.is_live():
        error_message = (f"Weaviate Client is not live in {os.path.basename(__file__)} "
                         f"-> {connect_to_weaviate.__name__}. "
                         "Please check the configuration settings and ensure that "
                         "the Weaviate Cloud Service URL (WCSURL) and API key (WCSAPI) "
                         "are correct and that the service is reachable.")
        raise ValueError(error_message)
    else:
        print('Successfully connected to WCS')

    return client


def load_schema_from_file() -> Dict[str, Any]:
    """
    Loads the schema for vector DB from a JSON file.

    Returns:
        Dict[str, Any]: The loaded schema.

    Raises:
        FileNotFoundError: If the schema file is not found.
    """
    SCHEMA_FILE_PATH: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..", "config", "schema_v0.json"))

    try:
        with open(SCHEMA_FILE_PATH, 'r') as schema_file:
            schema: Dict[str, Any] = json.load(schema_file)
            print(schema)
            return schema
        
    except FileNotFoundError:
            error_message = (f"Error in {__file__} -> {load_schema_from_file.__name__}: "
                         f"Schema file '{SCHEMA_FILE_PATH}' not found. "
                         "Please ensure that the file exists and the path is correct.")
        
            print(error_message)
            raise FileNotFoundError(error_message)