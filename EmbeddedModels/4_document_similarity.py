from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimension=307)

documents = [
    "virat kohli is an indian cricketer",
    "he is the captain of the indian cricket team",
    "he is one of the best batsman in the world",
    "he has scored more than 7000 runs in odi cricket",
    "he has scored more than 2000 runs in t20 cricket",
    "he has scored more than 7000 runs in test cricket",
    "he has scored more than 100 centuries in international cricket",
    "he has won many awards for his performance in cricket",
    "he is a role model for many young cricketers",
    "he is a philanthropist and has contributed to many social causes"
]

query = "tell me about virat kohli runs in odi cricket "

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

print(cosine_similarity([query_embedding], doc_embeddings)[0])