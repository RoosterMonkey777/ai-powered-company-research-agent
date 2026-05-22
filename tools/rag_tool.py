#split the text into chunks
#convert chunks into embeddings
#store them in ChromaDB
#retrieve relevant chunks later

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

embeddings = OpenAIEmbeddings()

def create_vector_store(text):

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    docs = [Document(page_content=chunk) for chunk in chunks]

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="./db"
    )

    return vectordb

def retrieve_context(vectordb, query):

    docs = vectordb.similarity_search(query, k=4)

    return "\n\n".join([d.page_content for d in docs])