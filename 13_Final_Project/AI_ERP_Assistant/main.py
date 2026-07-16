from fastapi import FastAPI

app = FastAPI(title="AI ERP Assistant")

@app.get("/")
def root():
    return {"message": "AI ERP Assistant is running!"}
