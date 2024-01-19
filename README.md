# Vector Database Lab Activity: Semantic Search with ChromaDB

## Objectives
- Implement and understand key functions in ChromaDB that facilitate semantic search.
- Gain practical experience in handling semantic queries and understanding their results.

## Prerequisites
- Python environment.
- Basic knowledge of Python programming.
- Understanding of basic database operations.

## Setup Instructions
1. Ensure Python and necessary tools are installed on your system.
2. Install dependencies using pip or pip3:

```bash
pip install -r requirements.txt
```

or

```bash
pip3 install -r requirements.txt
```

## Lab Overview
In this lab, you will embark on an interactive journey with ChromaDB, focusing on building collections, embedding data from a CSV file, and harnessing the power of semantic search. Beginning with a fundamental setup of ChromaDB, you will learn to embed data from a CSV file containing a restaurant menu. The key part of this lab involves using semantic search to effectively query this embedded data, gaining insights into how advanced database queries operate.

**What is Semantic Search?**

Semantic search is the advanced method of understanding the deeper intent and contextual meaning behind a search query, moving away from mere keyword matching. It leverages natural language processing (NLP) techniques to understand the subtleties and relationships within language, aiming to deliver search results that are not only relevant but also contextually accurate.

**How Does It Differ From Traditional Search?**

Keyword Search: Traditional search methods are based on keyword matching, where the search query's keywords are matched with those in database documents. This approach, while straightforward, can often lead to irrelevant results if the keywords, though present, are used in a different context or meaning.

Semantic Search: Semantic search, in contrast, delves into the context and semantics of the query's words. It utilizes NLP techniques to grasp the intent behind the query, enabling it to find results that are related in context, even when the exact query terms are not present in the database.

**Relevance in This Lab**

In this lab, you will engage with ChromaDB to implement and explore semantic search functionality. The lab's highlight is embedding a restaurant menu from a CSV file into a ChromaDB collection and then querying this data semantically. This process will involve generating embeddings from NLP models, enabling you to create a system that understands the semantic content of both the search queries and the menu items in your database. This approach aims to yield more meaningful and contextually relevant search results, showcasing the effectiveness of semantic search in practical applications.

## Lab Instructions
- Complete the 'TODO' methods as outlined in the lab documents.
- To successfully finish the lab, pass all tests in the tests/test_lab.py file.
- Run the application or tests using your editor, or use the provided run scripts.

### Running Scripts
To run a shell script in Unix/Linux/Mac environments, use the command:

```
./run_script.sh
````

Make sure the script has execute permissions. If not, run chmod +x run_script.sh first.

To run a batch script in Windows, simply execute:

```
run_script.bat
```

## Support
- For technical issues or detailed understanding, consult the [ChromaDB documentation](https://docs.trychroma.com/).
- For additional guidance or inquiries, reach out to the lab coordinator or use the dedicated help forum.

## License
This lab activity and its materials are provided under the MIT License. They are intended for educational and training purposes.
