from setuptools import find_packages,setup

# This code snippet is a setup configuration for a Python package using `setuptools`. Here's what each parameter in the `setup()` function is doing:
setup(
    name="Demand forecasting SCM RAG",
    vesion="0.0.1",
    author="Karthik",
    author_email="karthiksurya611@gmail.com",
    packages=find_packages(),
    install_requires=["pandas",
"numpy",
"conda",
"black",
"python-dotenv",
"langchain" ,
"langchain-community",
"langchain-core",
"chromadb",
"transformers", 
"transformer-embeddings",
"huggingface_hub",
"setuptools",
"streamlit"]
)