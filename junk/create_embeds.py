import os
import sys
import json
from typing import List

from langchain.embeddings.base import Embeddings
from langchain.embeddings import HuggingFaceHubEmbeddings

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Add src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers.save_embeds import save_embeddings


def create_embeddings(
    load_json_chunks_directory: str = os.getenv("DIRECTORY_FOR_DOCUMENTS_JSON_CHUNKS"),
) -> List[Embeddings]:
    """
    This function creates embeddings for a list of documents stored in JSON format.

    Args:
    - load_json_chunks_directory (str): The directory containing the JSON files to be processed.

    Returns:
    - List[Embeddings]: A list of embeddings for the documents.
    """
    # Load the HuggingFaceHubEmbeddings object
    embeddings = HuggingFaceHubEmbeddings(
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )

    all_embeddings: list[Embeddings] = []

    # Loop through each JSON file in the directory
    for filename in os.listdir(load_json_chunks_directory):
        if filename.endswith(".json"):
            # Load the documents from the JSON file
            with open(os.path.join(load_json_chunks_directory, filename), "r") as f:
                documents = json.load(f)

            texts: list[str] = []
            # Extract the text from each document
            for doc in documents:
                for key, value in doc.items():
                    texts.append(value)
                    break

            # Embed the documents using the HuggingFaceHubEmbeddings object
            embeddings_list = embeddings.embed_documents(texts)

            # Add the embeddings to the list of all embeddings
            all_embeddings.extend(embeddings_list)

    return all_embeddings


"""################# CALLING THE FUNCTION #################"""


print("\n####################### CREATING EMBEDDINGS ########################\n")

# Creating the embeddings
embeddings = create_embeddings()

print("\n####################### EMBEDDINGS CREATED ########################\n")

print("\n####################### SAVING EMBEDDINGS ########################\n")
save_embeddings(embeddings=embeddings)

print("\n####################### EMBEDDINGS SAVED ########################\n")