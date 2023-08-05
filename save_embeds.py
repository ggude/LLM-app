import pickle
import os

from langchain.embeddings.base import Embeddings

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def save_embeddings(
    embeddings: Embeddings,
    saving_embeddings_file_name: str = os.getenv("SAVING_EMBEDDINGS_FILE_NAME"),
    saving_embeddings_directory: str = os.getenv("SAVING_EMBEDDINGS_DIRECTORY"),
) -> None:
    """
    Save embeddings to a binary file with the specified file name and directory path.

    Args:
        - embeddings (Embeddings): The embeddings to be saved.
        - saving_embeddings_file_name (str): The name of the file to save the embeddings to.
        - saving_embeddings_directory (str): The path to the directory where the file will be saved.

    Returns:
        - None
    """

    directory = os.path.join(os.getcwd(), saving_embeddings_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, saving_embeddings_file_name + ".pkl")

    # Save embeddings to binary file
    with open(file_path, "wb") as f:
        pickle.dump(embeddings, f)