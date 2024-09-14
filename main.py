from rag.db import (
    add_to_collection,
    get_db_collection,
    query_collection,
    generate_context,
)
from rag.llm import llm_invoke, prepare_chat_prompt
from rag.document_loader import generate_document_payload


COLLECTION_NAME = "my_project"
collection = get_db_collection(COLLECTION_NAME)

# check if collection has documents already, if not load
if collection.count() > 0:
    print("Documents already loaded to DB")
else:
    print("Loading documents to DB")

    contents, ids, metadata = generate_document_payload(
        file_path="docs/project-report.pdf"
    )
    add_to_collection(collection, contents, ids, metadata)


while True:

    query_text = input(
        "\n\nAsk anything about Automatic Medicine Vending Machine project. (Enter q to quit) :\n"
    )
    if query_text == "q":
        print("Quitting...\n\n")
        break

    query_result = query_collection(collection, query_text)

    context = generate_context(query_result)

    prompt = prepare_chat_prompt(context, query_text)

    result = llm_invoke(prompt)

    print(result, "\n\n")
