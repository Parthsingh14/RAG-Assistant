from langchain_community.document_loaders.text import TextLoader

def load_txt(file_path: str):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents