distancia = 0
precio_gasolina = 0

print("Bienvenido al calculador de viajes")

while True:
    try:
        distancia = float(input("Ingrese la distancia en Kilometros\n"">> "))
        precio_gasolina = float(input("Ingrese el precio de la gasolina\n"">> "))
    except ValueError:
        print("Solo puedes ingresar numeros")
    if distancia and precio_gasolina:
        print("Datos ingresados correctos")
        break

litros_necesarios = (distancia * 8) / 100
costo_del_viaje = litros_necesarios * precio_gasolina
tipo_estimado = distancia / 90

print(f"Se necesitaran {litros_necesarios:.2f} litros de gasolina para el viaje\n"
      f"El viaje costará {costo_del_viaje:.2f} en gasolina\n"
      f"Y el tiempo estimado con una media de 90 km/h es de {tipo_estimado:.2f} horas")
