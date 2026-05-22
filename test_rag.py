from tools.search_tool import search_company
from tools.rag_tool import create_vector_store, retrieve_context

# search web
data = search_company("Stripe")

# create vector DB
vectordb = create_vector_store(data)

# retrieve relevant info
context = retrieve_context(
    vectordb,
    "What are Stripe's products?"
)

print(context)
