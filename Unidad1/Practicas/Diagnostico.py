productos = ["Universal Championship", "Undisputed WWE Championship", "Intercontinental Championship"]
precios = [250, 470, 70]

def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

print("MENU WWE Shop - BIENVENIDO")
print("=" * 35)

cantidades = [] 

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_input = int(input("Ingresa la cantidad de este producto: "))
    cantidades.append(cantidad_input) 

total = calcular_total(cantidades, precios)

print("\n--- TICKET DE COMPRA ---")
print("WWE Shop")
print("-" * 50)
print(f"{'Producto':30} {'Cant.':<6} {'Precio':<8} {'Subtotal':<8}")
print("-" * 50)

for i in range(len(productos)):
    subtotal = cantidades[i] * precios[i]
    print(f"{productos[i]:30} {cantidades[i]:<6} ${precios[i]:<7} ${subtotal:<7}")

print("-" * 50)
print(f"{'TOTAL:':30} ${total}")
print("-" * 50)
print("\n¡Gracias por su compra!")