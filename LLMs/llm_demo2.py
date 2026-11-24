from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7
)

result = llm.invoke("Who is Harry Potter?")

print(result.content)