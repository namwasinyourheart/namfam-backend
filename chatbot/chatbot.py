import os

from dotenv import load_dotenv
load_dotenv() 

from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain.memory import ConversationBufferMemory 
from langchain.chains import ConversationalRetrievalChain

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

import re

# from langdetect import langdetect


# import os
# from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService
# def load_env(): 
#     _ = load_dotenv(find_dotenv())

# def get_openai_api_key():
#     load_env()
#     openai_api_key = os.getenv("OPENAI_API_KEY")
#     return openai_api_key


openai_api_key = os.getenv("OPENAI_API_KEY")
# print(openai_api_key)  

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

def get_llm(model_name, 
            max_tokens=1000, 
            temperature=0):
    pass

llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")

def get_embeddings_model():
    return OpenAIEmbeddings(model="text-embedding-3-small")

# def generate_response():
#     # llm = 
#     gen_response_prompt_template = """
    
#     """
#     chain = 
#     return 



def get_pdf_text(pdf_files):
    
    text = ""
    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_chunk_text(text):
    
    text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len
    )

    chunks = text_splitter.split_text(text)

    return chunks

def get_vector_store(text_chunks):
    embeddings = get_embeddings_model()
    vector_store = FAISS.from_texts(texts = text_chunks,
                                    embedding = embeddings)
    
    return vector_store

def get_conversation_chain(vector_store):
    memory = ConversationBufferMemory(memory_key="chat_history",
                                      return_message=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vector_store.as_retriever(),
        memory = memory
    )

    return conversation_chain

def get_response(user_query, documents):

    template = """
    You are a Vietnamese helpful assistant to provide information about a candidate named Nam.

    You dedicated to assisting Nam in his job search by providing recruiters with relevant and concise information from relevant documents. 

    If the question isn't relevant to topic, say "Sorry, I can't assist you with this question."
   
    Note that, respond with similar language from the question, except technical terms.
    Documents: {documents}

    User question: {user_question}

    Again, if the question isn't relevant to topic, say "Sorry, I can't assist you with this question."
    """

    prompt = ChatPromptTemplate.from_template(template)

    # llm = ChatOpenAI()
        
    chain = prompt | llm | StrOutputParser()
    
    
    # return chain.stream({
    #     "documents": documents,
    #     "user_question": user_query,
        # })

    answer = chain.invoke(
        {"documents": documents,
        "user_question": user_query})

    return answer
    



def get_answer(user_input):
    
    pdf_files = [
            # "../CV_Updated_1905.pdf",
            "./CV_Updated_1905.pdf"
        ]

    # Get PDF Text
    raw_text = get_pdf_text(pdf_files)

    # Get Text Chunks
    text_chunks = get_chunk_text(raw_text)

    # print("TEXT CHUNKS:", text_chunks)
    
    # Create Vector Store
    vector_store = get_vector_store(text_chunks)
    # st.write("DONE")

    query = user_input
    docs = vector_store.similarity_search(query=query, k=5)

    # print("DOCS:", docs)

    # chain = load_qa_chain(llm=llm, chain_type="stuff")
    answer = get_response(query, docs)

    return answer
