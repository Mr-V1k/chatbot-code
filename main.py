# from langchain.chat_models import ChatOpenAI -> deprecated
from langchain_openai import ChatOpenAI # new import for ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# from langchain.embeddings.openai import OpenAIEmbeddings -> deprecated
from langchain_openai import OpenAIEmbeddings # new import for OpenAIEmbeddings
from langchain.vectorstores import Chroma
from api_keys import openai_api_key

def conversational_chat_parent(query, chat_history):
    # Create instance of OpenAI LLM
    openai_llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

    # Database Directory
    persist_directory = "vectordb/"

    # get embedding functions
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)

    # load from the disk
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
    
    with open("PromptTemplate/Parent/KPI-Mobile.txt", "r") as f:
        template = f.read()

    prompt = PromptTemplate(input_variables=["context", "question", "chat_history"], template=template)
    chain = LLMChain(llm=openai_llm, prompt=prompt)

    context = vectorstore.similarity_search(query)
    result = chain.run({
        "question": query,
        "context": context,
        "chat_history": chat_history,
    })

    return result
