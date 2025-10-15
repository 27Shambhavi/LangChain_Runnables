import random
# class psuedoLLM:

#     def __init__(self):
#         print('LLm  created')
#     def predict(self, prompt):
#         response_list= [
#             'Delhi is the capital of India.',
#             'Virat kohli is the captain of Indian cricket team.',
#             'Python is a programming language.',   
#         ]

#         return {'response': random.choice(response_list)}
    
# llm=psuedoLLM()
# llm.predict('who is the captain of Indian cricket team?')    


# class pusedoPromptTemplate:
#     def __init__(self, input_variables, template):
#         self.input_variables = input_variables
#         self.template = template
#         print('Prompt template created')
    
#     def format(self, input_dict):
#         return self.template.format(**input_dict)
    
# template= pusedoPromptTemplate(
#         input_variables=["context", "question"],    
#         template="based on the context: {context}, answer the question: {question}",
#     )
# template.format({'context': 'Delhi is the capital of India', 'question': 'What is the capital of India?'})


# prompt=template.format({'context': 'Delhi is the capital of India', 'question': 'What is the capital of India?'})
class NakliLLM:

  def __init__(self):
    print('LLM created')

  def predict(self, prompt):

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}
class NakliPromptTemplate:

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    return self.template.format(**input_dict)
    template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)
    prompt = template.format({'length':'short','topic':'india'})
    llm = NakliLLM()
    llm.predict(prompt)

class NakliLLMChain:

  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt

  def run(self, input_dict):

    final_prompt = self.prompt.format(input_dict)
    result = self.llm.predict(final_prompt)

    return result['response']
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)
llm = NakliLLM()
chain = NakliLLMChain(llm, template)
chain.run({'length':'short', 'topic': 'india'})