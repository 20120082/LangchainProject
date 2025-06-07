from langchain_google_genai import GoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os

def build_conversation_chain():
    llm = GoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
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
