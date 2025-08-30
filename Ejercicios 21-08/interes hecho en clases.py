monto_inicial = int(input("Dime la cantidad de dinero deseado para el prestamo \n >> "))
interes = int(input("Dime el porcentaje de interes mensual \n >> ")) / 100
meses_del_prestamo = int(input("Dime la cantidad de meses a pagar el prestamo \n >> "))
monto_final = monto_inicial * (1 + interes) ** meses_del_prestamo
print(f"El monto a pagar en total es de {round(monto_final, 2)} y el monto por mes es de {round(monto_final / 12, 2)}")

