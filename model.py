# Load required python libraries 
from langchain.llms import CTransformers
import torch
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA,LLMChain

# Check if GPU is available, otherwise use CPU
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu" 

device = torch.device(device)

# Path to load FAISS index
DB_FAISS_PATH = 'vectorstore/db_faiss'  

# Custom prompt template with context and question variables
custom_prompt = '''
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}  
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
'''

# Load embedding model  
embeddings=HuggingFaceEmbeddings(model_name='microsoft/unixcoder-base',model_kwargs={'device': device})


# Create prompt template
prompt=PromptTemplate(template=custom_prompt,input_variables=['context','question'])

# Load stablecode model
codestable=CTransformers(
        model="Stablecode-alpha-3b/stablecode-instruct-alpha-3b.ggmlv1.q8_0.bin",
        model_type="gpt_neox",
        max_new_tokens=512,
        temperature = 0)

# Load FAISS index
db_faiss=FAISS.load_local(DB_FAISS_PATH,embeddings)

# Function to create retrieval chain
def chains(llm,prompt,db):
  chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", 
    retriever=db.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True,
    chain_type_kwargs={'prompt': prompt}
  )
  return chain

# Function to run QA
def qa_bot(query):
  db = db_faiss
  llm = codestable
  qa_prompt = prompt
  qa = chains(llm, qa_prompt, db)
  response = qa({'query': query})
  return response

