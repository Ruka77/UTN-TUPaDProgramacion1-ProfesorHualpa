print("Bienvenido a la calculadora de nota final")
print("Porfavor ingresa todas las notas totales y no en porcentaje")

nota1 = float(input("Ingresa la primera nota parcial \n"">> "))
nota2 = float(input("Ingresa la segunda nota parcial \n"">> "))
nota3 = float(input("Ingresa la tercera nota parcial \n"">> "))
nota_exa_final = float(input("Ingresa la nota del examen final \n"">> "))
nota_trab_final = float(input("Ingrese la nota del trabajo final \n"">> "))

promedio_notas1_a_3 = (nota1 + nota2 + nota3) / 3
porcentaje_de_la_nota_1_2_3 = (promedio_notas1_a_3 * 55) / 100
porcentaje_nota_exa_final = (nota_exa_final * 30) / 100
porcentaje_nota_trab_final = (nota_trab_final * 30) / 100

nota_final = porcentaje_nota_exa_final + porcentaje_de_la_nota_1_2_3 + porcentaje_nota_trab_final

print(f"La nota final es un {nota_final:.2f}")