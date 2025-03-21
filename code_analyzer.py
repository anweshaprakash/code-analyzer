import os
from pathlib import Path

from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import openai
load_dotenv()

def analyze_code():
    """This tool reads the contents of a code file for analysis."""
    
    file_path = input("PASTE YOUR CODE FILE PATH HERE: ")
    file_extension = Path(file_path).suffix[1:].lower()
    
    if file_extension not in ["py", "js", "cpp", "java", "tex"]:
        raise ValueError(f"Unsupported file type: {file_extension}")
    
    with open(file_path, "r") as file:
        code_contents = file.read()

    groq_client = openai.OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("groq_api_key"),
    )

    # Analyze the code contents
    chat_completion = groq_client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": f"Analyze the following code:\n{code_contents}"
                }],
                model="qwen-2.5-coder-32b",
            )
    results = chat_completion.choices[0].message.content
    return results


llm = ChatGroq(model='qwen-2.5-coder-32b',
               temperature=0.1,
               api_key=os.getenv('groq_api_key')
)

data = analyze_code()
system_prompt = """
                           This is the code for you to analyze: {data}
        """

prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("human", "{input}")]
        )

chain = prompt | llm
answer = chain.invoke({"input": "State the errors in the code", "data": data})
print(answer.content)
