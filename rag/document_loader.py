from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.keyword_generator import extract_keywords


def generate_document_payload(file_path:str):
    """
    Load a PDF document, split it into chunks of text, extract keywords from each chunk, and
    return the chunks, IDs, and metadata (which includes keywords) for each chunk.

    :param file_path: Path to the PDF file to load
    :type file_path: str

    :return: 3-tuple of lists of (1) chunk contents, (2) chunk IDs, and (3) metadata dictionaries
    :rtype: tuple[list[str], list[str], list[dict]]
    """

    loader = PyPDFLoader(file_path)
    document = loader.load()
    print("No. of pages in the document:", len(document))

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunked_documents = text_splitter.split_documents(document)

    contents = []
    ids = []
    keywords = []

    page_no = 0
    c_index = -1
    for _, doc in enumerate(chunked_documents):
        metadata = doc.metadata
        source = metadata['source'].replace('/','-').replace('.','-')

        if metadata['page'] > page_no:
            c_index = 0
        else:
            c_index += 1

        page_no = metadata['page']
        
        chunk_id = f"{source}-p{page_no}-c{c_index}"

        contents.append(doc.page_content)
        ids.append(chunk_id)
        keywords.append(extract_keywords(doc.page_content))
        print("Processed chunk:", chunk_id)

    metadata = [{"tags": ", ".join(i) } for i in keywords]

    return contents, ids, metadata
    