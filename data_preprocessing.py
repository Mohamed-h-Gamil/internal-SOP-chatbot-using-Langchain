from langchain_docling.loader import ExportType
from langchain_docling import DoclingLoader
from docling.chunking import HybridChunker
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata
from dotenv import load_dotenv

FILE_PATH = ["./data/SOP.pdf"]
EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
EXPORT_TYPE = ExportType.DOC_CHUNKS

def create_vector_db():
    loader = DoclingLoader(
        file_path=FILE_PATH,
        export_type=EXPORT_TYPE,
        chunker=HybridChunker(
                    tokenizer=EMBED_MODEL_ID,
                ),
    )

    docs = loader.load()


    embedding = HuggingFaceEmbeddings(model_name=EMBED_MODEL_ID)

    # Filter out complex metadata that ChromaDB cannot handle
    filtered_docs = filter_complex_metadata(docs)

    vectordb = Chroma.from_documents(
        documents=filtered_docs, 
        embedding=embedding,
        persist_directory='vectordb/',
        collection_name="SOPs_collection"
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    return retriever


def get_vector_db():
    embedding = HuggingFaceEmbeddings(model_name=EMBED_MODEL_ID)
    vectordb = Chroma(
        persist_directory='vectordb/',
        embedding_function=embedding,
        collection_name="SOPs_collection"
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    return retriever


if __name__ == "__main__":
    load_dotenv()
    create_vector_db()
