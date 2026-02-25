import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader

search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))


@tool
def Finance_doc_tool(path: str) -> str:
    """Reads and returns cleaned content of a PDF financial document"""
    docs = PyPDFLoader(path).load()
    full_report = ""
    for page in docs:
        full_report += page.page_content.replace("\n\n", "\n") + "\n"
    return full_report


@tool
def Investment_tool(financial_document_data: str) -> str:
    """Analyzes investment aspects of a financial document"""
    processed_data = financial_document_data
        
        # Clean up the data format
    i = 0
    while i < len(processed_data):
        if processed_data[i:i+2] == "  ":  # Remove double spaces
            processed_data = processed_data[:i] + processed_data[i+1:]
        else:
            i += 1
                
        # TODO: Implement investment analysis logic here
    return "Investment analysis functionality to be implemented"



@tool
def Risk_tool(financial_document_data: str) -> str:
    """Performs a risk assessment on the document"""
    return f"Risk assessment placeholder. Length: {len(financial_document_data)}"