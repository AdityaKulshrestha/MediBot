from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback


def response_from_gpt(title):
    with open('prompt.txt', 'r') as f:
        template = f.read()
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template,
    )
    chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
    return chain.run(title)
