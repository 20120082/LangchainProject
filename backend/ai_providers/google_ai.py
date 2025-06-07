from langchain_google_genai import GoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

def build_conversation_chain():
    llm = GoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
    )
    memory = ConversationBufferMemory()
    return ConversationChain(llm=llm, memory=memory, verbose=True)
