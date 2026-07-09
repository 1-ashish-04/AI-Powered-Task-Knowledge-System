from app.services.faiss_service import search_faiss

results = search_faiss("What is Python?")

for result in results:
    print("=" * 60)
    print(result)