from ast import List
from typing import Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Curso(BaseModel):
    id= str
    nombre = str
    decripcion = Optional[str]=None
    nivel = str
    duracion:int

db = []

#Crud

@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return db

@app.post("/cursos/" , response_model=Curso)
def crear(curso:Curso):
    curso.id = str(uuid.uuid())
    db.append(curso)

@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id:str):
    curso = None
    for c in db:
        if c.id == curso_id:
         curso = c
         break
    if curso is None:
        raise HTTPException(status_code=404,detail="No encontrado")
    return db

@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id:str, nuevo:Curso):
    curso = None
    for c in db:
        if c.id == curso_id:
         curso = c
         break
    if curso is None:
        raise HTTPException(status_code=404,detail="No encontrado")
    else:
       nuevo.id = curso_id
       index = db.index(curso)
       db[index] = nuevo
       return nuevo
    
@app.delete("/cursos/{curso_id}", response_model=Curso)
def borrar_curso(curso_id:str):
    curso = None
    for c in db:
        if c.id == curso_id:
         curso = c
         break
    if curso is None:
        raise HTTPException(status_code=404,detail="No encontrado")
    else:
       db.remove(curso)
    return curso