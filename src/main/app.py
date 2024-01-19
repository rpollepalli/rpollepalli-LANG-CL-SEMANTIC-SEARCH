port os
import csv
import pprint
import chromadb

from typing import List, Tuple
from csv import reader

# ------------------------------------------------------------------------------
# TODO Functions - Implement the logic as per instructions
# ------------------------------------------------------------------------------


def get_embeddings_from_csv(
    csv_file_data: List[List[str]],
) -> Tuple[List[str], List[dict], List[str]]:
    """
    TODO: Implement this method to extract document texts, metadata, and generate unique IDs from the given CSV file data.
    Each row in the CSV file represents a document. The first column is considered metadata (e.g., title or ID from the CSV),
    and the second column is the document text.

    Parameters:
    file_data (list of lists): The content of the CSV file, where each inner list represents a line.

    Returns:
    tuple: A tuple containing three lists - documents (list of strings), metadatas (list of dictionaries), and ids (list of strings).

    Instructions:
    - Iterate over each line in file_data.
    - Skip the first line if it contains headers.
    - For each line, extract the first column as metadata (e.g., {"title": value}) and the second column as document text.
    - Generate a unique ID for each document (e.g., using the line number).
    """
    # Implement your code here
    line = 0
    documents = []
    metadatas = []
    ids = []
    for row in csv_file_data:
        if line == 0:
            line += 1
            continue
        documents.append(row[1])
        metadatas.append({"title": row[0]})
        ids.append(str(line))
        line += 1
    return (documents, metadatas, ids)


def get_chromadb_collection(
    documents: List, metadatas: List, ids: List
) -> chromadb.Collection:
    """
    TODO: Implement this method to initialize a ChromaDB collection named 'semantic-lab' and add the provided documents, metadata, and ids to it.
    If a collection with the same name already exists, it should be deleted and a new one should be created.

    Parameters:
    documents (list): A list of document texts to add to the collection.
    metadatas (list): A list of metadata dictionaries corresponding to the documents.
    ids (list): A list of unique identifiers for the documents.

    Returns:
    chromadb.Collection: The initialized ChromaDB collection object.

    Instructions:
    - Create a new ChromaDB client.
    - Check if a collection named 'semantic-lab' already exists. If it does, delete it.
    - Create a new collection named 'semantic-lab'.
    - Add the documents, metadatas, and ids to the collection using the collection.add method.
    """
    # Implement your code here
    client = chromadb.PersistentClient("./chroma")
    for collection in client.list_collections():
        if collection.name == "semantic-lab":
            client.delete_collection(name="semantic-lab")
            break
    collection = client.create_collection(name="semantic-lab")
    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    return collection


def get_collection_query(user_input: str) -> chromadb.QueryResult:
    """
    TODO: Implement this method to query the 'semantic-lab' ChromaDB collection for documents that are semantically related to the given user input.

    Parameters:
    user_input (str): The user input to query the collection for.

    Returns:
    chromadb.QueryResult: The query result object containing the top 5 results.

    Instructions:
    - Retrieve the 'semantic-lab' collection from the ChromaDB client.
    - Perform a query using the collection.query method with the provided user_input.
    - Limit the number of results to 5 (n_results=5).
    - Return the query result.
    """
    # Implement your code here
    collection = chromadb.PersistentClient("./chroma").get_collection(name="semantic-lab")
    return collection.query(query_texts=[user_input], n_results=5)


# ------------------------------------------------------------------------------
# Starter Code - Do not modify
# ------------------------------------------------------------------------------


def read_file_from_folder(csv_file: str) -> List[List[str]]:
    """
    Reads a .csv file from a directory and returns its content.

    Parameters:
    csv_file (str): The path to the .csv file relative to the root directory

    Returns:
    list: A list of rows from the CSV file, where each row is represented as a list.
    """
    with open(csv_file) as file:
        return list(csv.reader(file))


def main():

    print("getting csv", end="\n")

    # Read the files from the resources folder (don't move this csv file)
    file_data = read_file_from_folder("./resources/menu_items.csv")
    
    print("separating csv into docs, metadata, and ids", end="\n")
    
    # Get the embeddings from the csv files
    documents, metadatas, ids = get_embeddings_from_csv(file_data)
    
    print("initializing collection", end="\n")

    # Initializing the collection
    collection = get_chromadb_collection(documents, metadatas, ids)

    while True:
        # Get user input
        user_input = input("What are your taste buds craving today? (x to cancel): ")

        # Check if the user wants to exit
        if user_input == "x":
            break

        # Query the collection
        results = get_collection_query(user_input)

        # Print the results
        # Note: Remove the 'documents' key if you don't want to print only documents
        pprint.pprint(results["documents"])

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()