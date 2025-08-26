import chromadb
from langchain_ollama import OllamaEmbeddings, OllamaLLM
import os
from atproto import Client as blueskyClient

bluesky = blueskyClient()
bluesky.login("USERNAME","APP PASSWORD" ) 
print("log in successful!")
data = bluesky.app.bsky.feed.get_feed({
    'feed': 'at://did:plc:7fzt44e2vn3tfzftahicqyyc/app.bsky.feed.generator/aaael56jxike4',
    'limit': 100,
}, headers={'Accept-Language': "english"})

feed = data.feed
next_page = data.cursor

print("\n"f"{feed[0].post.record.text}")

llm = OllamaLLM(model="llama3.2")
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")



client = chromadb.Client()
collection = client.get_or_create_collection(name="my_collection")

for idx, doc in enumerate(feed):
    text = doc.post.record.text
    embedded_text = embedding_model.embed_documents([text])
    id= collection.count()
    collection.add(documents=[text], embeddings=embedded_text, ids=[str(id)])
    print(f"text={text}...id={id}")

query = input("Please input your query: ")
query_embedding = embedding_model.embed_documents([query])

context = collection.query(query_embeddings=query_embedding,n_results=5)
context = context["documents"][0]
print(f"The context is...{context}")

prompt = f"You are an NFL insider, you are being fed breaking news about NFL information. Here is your context {context} using this information give a response to this question: {query}"

response = llm.invoke(prompt)

print(f"The LLM response is {response}")


