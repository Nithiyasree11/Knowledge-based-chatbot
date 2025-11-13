import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import FastEmbedEmbeddings


load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

st.set_page_config(page_title="Knowledge-based-Chatbot",layout="centered")
st.title("Knowledge-based-Chatbot")
st.write("Knowledge base is on history of gold")

model="gemini-2.5-flash"

@st.cache_resource(show_spinner=False)
def vectorstore():
    loader=PyPDFLoader(r"data/HistoryofGoldElsevier2ndedition.pdf")
    doc=loader.load()


    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=350)
    docs=text_splitter.split_documents(doc)


    embeddings=FastEmbedEmbeddings()

    vectordb=Chroma.from_documents(documents=docs,embedding=embeddings,persist_directory="./chroma_db")

    return vectordb,embeddings

vectordb,embeddings=vectorstore()
retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k":5})

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

system_prompt=(
    "you are a chatbot on histdockerory of gold. "
    "use the retrieved context to answer the question accurately. "
    "if the answer is not in the"
    " context say you dont know. "
    "be concise and informative."
    "\n\n"
    "{context}"
    )

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human","{input}")
    ]
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

if st.button("clear history"):
    st.session_state.chat_history=[]
    st.rerun()

for message in st.session_state.chat_history:
    if isinstance(message,tuple):
        role,content=message
    else:
        role,content=message["role"],message["content"]
    with st.chat_message(role):
        st.markdown(content)

query=st.chat_input("Ask a question about history of gold")


if query:
    st.chat_message("user").markdown(query)
    st.session_state.chat_history.append({"role":"user","content":query})

    chain=create_stuff_documents_chain(llm, prompt)
    rag_chain=create_retrieval_chain(retriever,chain)

    response=rag_chain.invoke({"input":query})
    answer=response["answer"]

    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.chat_history.append({"role":"assistant","content":answer})
