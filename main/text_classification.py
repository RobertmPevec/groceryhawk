import pandas as pd
import faiss
import numpy as np
import pickle
import openai

openai.api_key = "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"

file_path = "datasets/globaldataset.csv"

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    response = openai.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def create_faiss_index(csv_path, text_column):
    df = load_csv(csv_path)
    texts = df[text_column].astype(str).tolist()
    
    # Generate embeddings
    embeddings = np.array([get_embedding(text) for text in texts], dtype=np.float32)
    
    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # Save index
    faiss.write_index(index, "faiss_index.bin")
    
    # Save ID mapping
    with open("id_mapping.pkl", "wb") as f:
        pickle.dump(df.to_dict(orient="records"), f)
    
    print("FAISS index and ID mapping saved.")