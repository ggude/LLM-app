# -*- coding: utf-8 -*-
"""LLM_TUTORIAL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SxxasJzoSx__47kGGXnIb48qJkYg25LX
"""

cd /content/drive/MyDrive/llm_dev

#!pip install -r requirements.txt

#!pip install python-dotenv

#pwd

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os
import argparse
import time

os.environ["PERSIST_DIRECTORY"]= "/content/drive/MyDrive/llm_dev/gnapi_db"

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

os.environ["MODEL_TYPE"]= "LlamaCpp"
os.environ["MODEL_N_CTX"]= "4096"

#cd models
#!wget "https://gpt4all.io/models/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin"
#!wget "https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"

#pwd

from constants import CHROMA_SETTINGS

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

#from langchain.embeddings import HuggingFaceHubEmbeddings

#!pip install sentence_transformers

#embeddings = HuggingFaceHubEmbeddings(
 #         huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
  #    )

embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)

retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

query = "Article 13"
results = retriever.get_relevant_documents(query)
#for chunk in results:
#  print(chunk.page_content)  # or whatever attribute holds the content
print(results)

print(dir(retriever))

#llm = GPT4All(model=model_path, max_tokens=model_n_ctx, backend='gptj', n_batch=model_n_batch, verbose=False)
 llm = LlamaCpp(model_path=model_path, max_tokens=model_n_ctx, n_batch=model_n_batch, verbose=False)

#!pip install pygpt4all

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

query = "summarise fundamental rights in bullet points"

res = qa(query)

res

"""#ingest.py"""


