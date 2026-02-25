# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

### Sample Document
The system analyzes financial documents like Tesla's Q2 2025 financial update.

**To add Tesla's financial document:**
1. Download the Tesla Q2 2025 update from: https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf
2. Save it as `data/sample.pdf` in the project directory
3. Or upload any financial PDF through the API endpoint

1. Agents.py
    1. LLM import function added (added import package)
    2. llm intialisation fixed (added model name and api key)
    3. agent import fixed (misspelled)
    4. agent parameter tools fixed (wrong parameters werre fixed)


2.tools.py
    1. fixed serperdevtool import (added api key)
    2. fixed loading of pdf file (added correct loader for same)
    3. SerperDevTool apikey fixed
    4. fixed the function name  (re-named function to _run )
    5. classes changed to be used with a decorator rather than passing instance of the class
    6. reframed the logic for reading file

3. Task.py
    1. async_execution set to true
    2. fixed passing down of instance to the tools parameter
    3. fixed the description for analyze_financial_document

4. main.py
    1. fixed the function name (earlier using same name as import)