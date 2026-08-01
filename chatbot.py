from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history = []


while True:
  user_input = input("User: ")
  
  chat_history.append( user_input)
  
  if user_input.lower() == "exit":
    break 
  
  result = model.invoke(chat_history)
  chat_history.append( result.content)
  print("AI:", result.content)
  
  print(chat_history)