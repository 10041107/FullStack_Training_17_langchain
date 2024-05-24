from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

#response=llm.invoke("how can langsmith help with testing?")
#print(response)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm
result = chain.invoke({"input": "how can langsmith help with testing?"})
print(result)