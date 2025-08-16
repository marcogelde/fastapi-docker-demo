from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá turma, este é meu primeiro container com FastAPI!"}

@app.get("/marco")
def read_marco():
    return {"message": "Olá turma, este é o do Marco"}
