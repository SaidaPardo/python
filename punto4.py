listaRegistro=[]

def ingresar_usuario():
    documento=input("Ingrese su numero de documento ")
    nombre=input("Ingrese el nombre del paciente ")
    apellido=input("ingrese sus apellidos ")
    edad=input("Ingrese su edad ")
    peso=input("ingrese su peso ")
    estatura=input("ingrese su estatura ")
    diccionario=dict(id=documento,nombre=nombre,apellido=apellido,edad=edad,peso=peso,estatura=estatura)
    return diccionario

print("Se encuentra en la opcion Ingresar Usuario")
listaRegistro.append(ingresar_usuario())
print(listaRegistro)
print("Su registro ha sido exitoso¡¡")

def buscar_usuario(listaRegistro,id):
    for i in range(len(listaRegistro)):
        datosUsuario=listaRegistro[i]
        if id == datosUsuario.get('id'):
            return i
    return -1

def ver_registro(listaRegistro,id):
    indice=buscar_usuario(listaRegistro,id)
    if indice != -1:
        print("se encontro el usuario")
        return listaRegistro[indice]

def ver_consulta(listaRegistro,id):
  indice=buscar_usuario(listaRegistro,id)
  if indice != -1:
        print("se encontro el usuario")
        return listaRegistro[indice]

pregunta=int(input("¿Desea consultar su registro?\n\n Ingrese:\n1. Consultar.\n 2. Agregar nuevo usuario.\n 3. Salir\n"))

if pregunta==1:
        print("Se encuentra en la opcion consultar registro")
        usuarioBuscar=input("Ingrese el id del usuario a buscar")
        mostrarregistro=ver_registro(listaRegistro,usuarioBuscar)
        print(mostrarregistro)
 
elif pregunta==2:
    print("Se encuentra en la opcion Ingresar Usuario")
    listaRegistro.append(ingresar_usuario())
    print(listaRegistro)

elif pregunta==3:
    print("Programa terminado, tenga buen dia")


       