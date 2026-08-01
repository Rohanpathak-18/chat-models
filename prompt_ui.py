from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)


   
# Load PromptTemplate
template = load_prompt("prompt_template.json")



st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    (
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    )
)

# Explanation Style Dropdown
style_input = st.selectbox(
    "Select Explanation Style",
    (
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    )
)

# Explanation Length Dropdown
length_input = st.selectbox(
    "Select Explanation Length",
    (
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed Explanation)"
    )
)



# Show selected options
if st.button("Generate"):
    chain = template | model

    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)
        
 