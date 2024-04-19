#Bienvenida al usuario
name=(input("Ingresa tu nombre: "))
print("Bienvenido ",name)
chek=float(input("Ingresa el saldo de tu tajeta "))

#lista donde se guardan las cosas del ususario
Productos=[
    ["XBOX 360"],
    ["XBOX ONE"],
    ["PLAY 5"],
]

PreciosProducto=[
    ["200"],
    ["300"],
    ["400"],
]

ProDucComprados=[]

#boleano que nos ayudara a que se repita el proceso para el usuario desde el menu
boolean=True

#menu del usuario
while boolean==True:
    print("=============================================")
    print("                   MENU                      ")
    print("=============================================")
    print("""
    "1. agregar productos al carrito " 
    "2. ver lista de compras "
    "3. finalizar programa "
      """)
    OP=int(input(f"seleccione una opcion usando solo (1,2,3):\n "))
    

    #productos que se le mostraran al usuario
    if OP==1:
        print(Productos)
        ver=input("que producto deseas agregar? ")
        PreciosProducto=ver-chek
        print(ver)

    elif ver==Productos:
        #por si el produco no esta en la lista o no hay suficientes en el inventario
        print(Productos.get(ver,"no tenemos este producto"))
        
    #Productos que comprara o compro el ususario
    if OP==2:
        ProDucComprados=ver
        print(ProDucComprados)
     
    #Se cierra la tienda o el menu usando el boolean
    if OP==3:
        print("vuelve pronto :D")
        boolean=False

#Creado por Miguel Guerrero C.C 1090381839