pesos_argentinos = 1320
pesos_colombianos = 4021
euros = 0.86
dolares = 0

print("Bienvenido a la calculadora de divisas")
print("Ingrese la cantidad a convertir en dolares")

while True:
    try:
        dolares = float(input(">> "))
    except ValueError:
        print("Solo puedes ingresar numeros")
    if dolares:
        break

cantidad_en_argentinos = dolares * pesos_argentinos
cantidad_en_colombianos = dolares * pesos_colombianos
cantidad_en_euros = dolares * euros

print(f"Tienes una cantidad de ${cantidad_en_argentinos:.2f} pesos argentinos\n"
      f"Una cantidad de ${cantidad_en_colombianos:.2f} pesos colombianos\n"
      f"Y €{cantidad_en_euros:.2f} de euros")
