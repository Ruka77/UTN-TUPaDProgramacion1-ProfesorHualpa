
while True:
    try:
        patentes_a_mover = int(input("Ingrese la cantidad de veces que quieres moverte de la patente inicial\n"">> "))
    except ValueError:
        print("Solo se pueden ingresar numeros enteros")
        continue

    patente = input("Ingrese la patente sin espacios ni guiones\n"">> ").lower()

    if len(patente) == 6:
        print("patente correctamente ingresada")
        break
    else:
        print("Patente ingresada incorrectamente")

numeros = int(patente[3:])
letras = patente[:3]
valores_letras = [ord(letra) - ord('a') for letra in letras]

letras_num = valores_letras[0] * 26 * 26 + valores_letras[1] * 26 + valores_letras[2]
posicion_inicial = letras_num * 1000 + numeros

posicion_final = posicion_inicial + patentes_a_mover

nuevas_letras_num = posicion_final // 1000
nuevos_numeros = posicion_final % 1000

l1 = nuevas_letras_num // (26 * 26)
l2 = (nuevas_letras_num // 26) % 26
l3 = nuevas_letras_num % 26

nuevas_letras = chr(l1 + ord('a')) + chr(l2 + ord('a')) + chr(l3 + ord('a'))
nueva_patente = f"{nuevas_letras}{nuevos_numeros:03d}"

print(f"La nueva patente es: {nueva_patente.upper()}")