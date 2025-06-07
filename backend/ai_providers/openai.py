from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os

def build_conversation_chain():
    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    memory = ConversationBufferMemory(
        return_messages=True,
        max_token_limit=5000  
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "{history}"),
        ("human", "{input}")
    ])

    chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)
    return chain, memory
