from langchain_community.document_loaders.word_document import Docx2txtLoader

def load_docx(file_path: str):
    loader = Docx2txtLoader(file_path)
    documents = loader.load()
    return documents