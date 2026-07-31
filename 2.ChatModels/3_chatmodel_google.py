from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model = '')

result = model.invoke('what is the capital of india')

print(result.content)

