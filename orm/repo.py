import orm.modelos as modelos
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_ 

# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()
#para consultar todos los usuarios
def usuarios(sesion:Session):
    print("select * from app.usuarios ")
    return sesion.query(modelos.Usuario).all()

def compra_por_id(sesion:Session,id_compra:int):
    print("select * from app.compras where id = ", id_compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()
#para consultar todos las compras
def compras(sesion:Session):
    print("select * from app.compras ")
    return sesion.query(modelos.Compra).all()

# select * from app.fotos where id = id_fotos
def foto_por_id(sesion:Session,id_foto:int):
    print("select * from app.fotos where id = ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()
#para consultar todos las compras
def fotos(sesion:Session):
    print("select * from app.fotos ")
    return sesion.query(modelos.Foto).all()
