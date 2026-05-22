from tools.search_tool import search_company
from tools.rag_tool import create_vector_store, retrieve_context

# STEP 1: Search web
data = search_company("Stripe")

# STEP 2: Create vector DB
vectordb = create_vector_store(data)

# STEP 3: Retrieve relevant info
context = retrieve_context(
    vectordb,
    "What are Stripe's products?"
)

print(context)