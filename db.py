from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader,JSONLoader,TextLoader
import torch

# Check if GPU is available, otherwise set device to CPU
if torch.cuda.is_available():
    device = "cuda" 
else:
    device = "cpu"

device = torch.device(device) 


DATA_PATH="DATA/"
DB_PATH="vectorstore/db_faiss"

def db_creator():
    
    loader=DirectoryLoader(
        DATA_PATH,
        glob='*.txt',
        loader_cls=TextLoader,
        recursive=True,
        use_multithreading=True,
        max_concurrency=8
    )
    
    doc=loader.load()
    
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,chunk_overlap=50
    )
    
    chunks=splitter.split_documents(doc)
    
    embeddings=HuggingFaceEmbeddings(
        model_name='microsoft/unixcoder-base',
        model_kwargs={'device': device}
    )
    
    db=FAISS.from_documents(chunks,embeddings)
    db.save_local(DB_PATH)
    

if __name__ == "__main__":
    db_creator()