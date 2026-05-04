try:
  nombre = input("Por favor, ingresa su usuario:\n> ").strip() # texto
  if not nombre: # las condiciones usan datos booleanosm, que serian False o True
     print("Ingrese un usuario valido")
     exit()
  direccion_envio = input("Ingrese la direccion donde el pedido va hacer entregado:\n> ").strip()
  if not direccion_envio:
     print("Ingrese una direccion valida")
     exit()

  print("El precio de la pizza es de $200 MXN")
  cantidad_de_pizzas = int(input("Ingresa la cantidad de pizzas:\n> ")) # numero entero
  if not cantidad_de_pizzas:
     print("Ingresa un numero valido")

  esta_pagado = input("El envio esta pagado? (Si/No)\n> ").strip().lower()
  precio = cantidad_de_pizzas * 200
  if not esta_pagado:
    print("Ingrese una respuesta")
    exit()

  elif esta_pagado == "si":
     print(f"El pedido va hacer unicamente entregado, ya esta pagado con {precio} al {direccion_envio}")

  elif esta_pagado == "no":
     print(f"El pedido debe de ser pagado al entregar con {precio}")
  else:
     print("ingrese un Si o No")
     exit()

except ValueError:
  print("Ingrese un numero valido")