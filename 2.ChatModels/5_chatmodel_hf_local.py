from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ

llm = HuggingFacePipeline.from_model_id(
  model_id='meta-llama/Llama-3.1-8B-Instruct',
  task='text-generation',
  pipeline_kwargs=dict(
    temperature = 0.5,
    max_new_tokens = 100
  )
)
model = ChatHuggingFace(llm = llm)

result = model.invoke("brief explaination about virat kohli")

print(result.content)