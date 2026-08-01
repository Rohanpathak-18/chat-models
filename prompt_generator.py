from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """
Please summarize the research paper titled "{paper_input}" with the following specifications.

Explanation Style:
{style_input}

Explanation Length:
{length_input}

Additionally:
- Include relevant mathematical equations if present.
- Explain mathematical concepts using simple intuition and code snippets where applicable.
- Use relatable analogies to simplify difficult concepts.
- If any information is unavailable in the paper, respond with "Insufficient information available" instead of guessing.
- Ensure the summary is clear, accurate, and follows the requested style and length.
    """,
   input_variables=["paper_input", "style_input", "length_input"],
validate_template=True
)
template.save("prompt_template.json")

