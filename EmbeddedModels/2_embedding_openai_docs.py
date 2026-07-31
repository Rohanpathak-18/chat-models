from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = '', dimensions=32)

documents = [
  "delhi is the capital of india"
  "kolkata is the capital of west bengal"
  "paris is the capital of france"
]

result =  embedding.embed_documents(documents)

print(str(result))
