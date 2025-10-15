from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai

#Load the document
loader = TextLoader('state_of_the_union.txt')
documents = loader.load()

#Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)


#convert the text chunks into embeddings & store in faiss vector store
vectorstore = FAISS.from_documents(texts, OpenAIEmbeddings())

#create a retriever 
retriever = vectorstore.as_retriever()

#manually retrieve relevant documents
query = "What did the president say about Ketanji Brown Jackson"
retrieved_docs = retriever.get_relevant_documents(query)

#combine retrieved documents into a single string
retrieve_text = "\n".join([doc.page_content for doc in retrieved_docs])

#initialize the LLM
llm = openai.OpenAI(model_name="gpt-3.5-turbo",temperature=0.7)

prompt=f"based on the context: {retrieve_text}, answer the question: {query}"

answer = llm.predict(prompt)
print(answer)