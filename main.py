# Bienvenida al usuario
name = input("Ingresa tu nombre: ")
print("Bienvenido", name)
saldo_tarjeta = float(input("Ingresa el saldo de tu tarjeta: "))

# Lista donde se guardan los productos disponibles
productos = [
    "XBOX 360",
    "XBOX ONE",
    "PLAY 5",
]

precios_productos = {
    "XBOX 360": 200,
    "XBOX ONE": 300,
    "PLAY 5": 400,
}

stock_productos = {
    "XBOX 360": 15,
    "XBOX ONE": 10,
    "PLAY 5": 5,
}

productos_comprados = []

# Bucle principal del menú
while True:
    print("=============================================")
    print("                   MENU                      ")
    print("=============================================")
    print("1. Agregar producto al carrito")
    print("2. Ver lista de compras")
    print("3. Finalizar programa")

    opcion = int(input("Selecciona una opción (1, 2, 3): "))

    if opcion == 1:
        print("Productos disponibles:")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. {producto} - Precio: {precios_productos[producto]} - Stock: {stock_productos[producto]}")
        
        seleccion = int(input("Elige el número del producto que deseas agregar al carrito: "))
        if seleccion < 1 or seleccion > len(productos):
            print("Opción inválida, Intenta nuevamente")
            continue
        
        producto_elegido = productos[seleccion - 1]
        cantidad_deseada = int(input(f"Ingrese la cantidad de '{producto_elegido}' que deseas agregar al carrito: "))
        
        if cantidad_deseada > stock_productos[producto_elegido]:
            print("Lo sentimos, no hay suficiente stock disponible")
        else:
            if precios_productos[producto_elegido] * cantidad_deseada > saldo_tarjeta:
                print("Saldo insuficiente para realizar esta compra")
            else:
                stock_productos[producto_elegido] -= cantidad_deseada
                productos_comprados.append((producto_elegido, cantidad_deseada))
                saldo_tarjeta -= precios_productos[producto_elegido] * cantidad_deseada
                print(f"Se agregaron {cantidad_deseada} '{producto_elegido}' al carrito de compras")

    elif opcion == 2:
        if not productos_comprados:
            print("Aún no has comprado nada.")
        else:
            print("Lista de compras:")
            for producto, cantidad in productos_comprados:
                print(f"{cantidad} x {producto}")
            print(f"Saldo restante en la tarjeta: {saldo_tarjeta} USD")

    elif opcion == 3:
        print("¡Gracias por tu visita!, Vuelve pronto :D ")
        break

# Creado por Miguel Guerrero C.C 1090381839
