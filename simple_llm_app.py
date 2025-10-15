from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Initialize Chat model (correct one for GPT-3.5+)
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key="your_openai_api_key_here",  
)

# Create the prompt
prompt = PromptTemplate(
    input_variables=["Topic"],
    template="Suggest a catchy blog title about {Topic}?",
)

# Take user input
Topic = input("Enter a topic: ")

# Format the prompt
formatted_prompt = prompt.format(Topic=Topic)

# Get the response
response = llm.invoke(formatted_prompt)

# Display output
print("Generated blog title:", response.content)