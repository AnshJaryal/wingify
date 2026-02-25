from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str="data/sample.pdf"):
    """To run the whole crew"""
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )
    
    result = financial_crew.kickoff({'query': query ,'path': file_path})
    return result

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_document_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_path = None  
    try:
        response = run_crew(query=query.strip(), file_path=file_path)
        print("CREW RAW RESPONSE:", response)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

    try:
        os.makedirs("data", exist_ok=True)

        file_id = str(uuid.uuid4())
        file_path = f"data/financial_document_{file_id}.pdf"  

        with open(file_path, "wb") as f:
            f.write(await file.read())

        if not query:
            query = "Analyze this financial document for investment insights"

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)