import orm.modelos as modelos
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

#DLETE '/usuarios/{id}'
# delete from app.usuarios where id=id_usuario
def borra_usuario_por_id(sesion:Session, id_usuario:int):
    print("delete from app.usuarios where id=id_usuario", id_usuario)
    #1.-select para ver si existe el usuario a borrar
    usr=usuario_por_id(sesion, id_usuario)
    #-Borramos 
    if usr is not None:
        #Borramos usuario
        sesion.delete(usr)
        #confirmar cambios
        sesion.commit()
    respuesta ={
        "mensaje": "usuario eliminado"
    }
    return respuesta
#select * fromm app.compras where edad =x and edad <x
def devuelve_usuarios_edad (sesion:Session,eda:int, eda2:int):
    print("Select *from usuario where edad >x and edad <x")
    return sesion.query(modelos.Usuario).filter(and_(modelos.Usuario.edad>eda, modelos.Usuario.edad<eda2)).first()
#Select *from app.compras where id=2 and precio >=500
# select * from app.compras where id = id_compra
#para consultar todas las compras Get'/compras?id_usuario ={id_usu}&precio={p}
#select * fromm app.compras where id_usuario =id_usur and precio >=p
def devuelve_compras_por_usuario_precio (sesion:Session,id_usr:int, p:float):
    print("Select")
    return sesion.query(modelos.Compra).filter(and_(modelos.Compra.id_usuario==id_usr, modelos.Compra.precio>=p)).first()

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

#buscar fotos por id_usuario
#Get '/usuarios/{id}/fotos'
#select *from app.fotos where id_usuario=id
def fotos_por_id_usuario(sesion:Session, id_usuario:int):
    print("select *from app.fotos where id_usuario",id_usuario)
    sesion.query(modelos.Foto).filter(modelos.Foto.id_usuario==id_usuario).all()

#borra fotos por id usuarii
#Delete '/usuarios/{id}/fotos'
#delete from app.fotos where id_usuario=id
def borrar_fotos_por_id_usuario(sesion:Session,id_usuario:int):
    print("delete from app.fotos where id_usuario=id", id_usuario)
    fotos_usr=fotos_por_id_usuario(sesion,id_usuario)
    if fotos_usr is not None: 
        for foto_usuario in fotos_usr:
         sesion.delete(foto_usuario)
        sesion.commit()
