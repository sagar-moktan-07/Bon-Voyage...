from fastapi import FastAPI as F

app = F()

@app.post("/hello")
def hello():
    return "Jackass forgetting everything......"