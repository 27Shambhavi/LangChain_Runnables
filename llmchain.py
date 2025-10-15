from langchain.llms import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

#load the LLM
llm = openai.OpenAI(model_name="gpt-3.5-turbo",temperature=0.7)

#Create a prompt template
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="based on the context: {context}, answer the question: {question}",
)

#Create the LLM chain
llm_chain = LLMChain(llm=llm, prompt=prompt)      

#run the chain with context and question
context = "The president discussed various topics including the economy, healthcare, and judicial appointments."
question = "What did the president say about Ketanji Brown Jackson?" 

print(llm_chain.run({"context": context, "question": question}))