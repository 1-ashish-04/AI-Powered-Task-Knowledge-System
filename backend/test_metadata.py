import pickle

with open("app/vector_store/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

print(f"Total Chunks: {len(metadata)}")

print("\nFirst Chunk:")
print(metadata[0])

print("\nLast Chunk:")
print(metadata[-1])