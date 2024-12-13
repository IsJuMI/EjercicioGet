from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

# creación del servidor
app = FastAPI()


# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta


#se hizo en clases para usuarios
@app.get("/usuarios/{id}")
def usuario_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando usuario por Id")
    return repo.usuario_por_id(sesion, id)

#se hizo en clases para consultar todos los usuarios
@app.get("/usuarios")
def usuarios(sesion:Session=Depends(generador_sesion)):
    print("Api consultando usuarios")
    return repo.usuarios(sesion)

#Para compras
@app.get("/compras/{id}")
def compra_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando compras por ID ")
    return repo.compra_por_id(sesion, id)

#para consultar todas las compras
@app.get("/compras")
def compras(sesion:Session=Depends(generador_sesion)):
    print("Api consultando todas las compras")
    return repo.compras(sesion)

#para fotos
@app.get("/fotos/{id}")
def foto_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por ID ")
    return repo.foto_por_id(sesion, id)
#se hizo en clases para consultar todas las fotos
@app.get("/fotos")
def fotos(sesion:Session=Depends(generador_sesion)):
    print("Api consultando todas las fotos")
    return repo.fotos(sesion)
