print("Bienvenido la calculadora de prestamos")
print("Indica que quieres hacer. \n""[1] Calculador de intereses [2] Solicitar un prestamo")

while True:
    calculadora = int(input("Selecciona una opcion (1 o 2): "))
    if calculadora == 1:
        print("Has seleccionado la calculadora de intereses.")
        break
    elif calculadora == 2:
        print("Has seleccionado solicitar un prestamo.")
        break
    else:
        print("Opcion no valida")

if calculadora == 2:
    while True:
        monto_solicitado = float(input("Ingresa el monto inicial: "))
        tasa_interes_anual = float(input("Ingresa la tasa de interes anual (en %): "))
        plazo_meses = int(input("Ingresa el plazo en meses: "))
        es_veraz = input("¿Tu te encuentras dentro del veraz? (si/no): ").lower()
        ingresos_mensuales = float(input("Ingresa tus ingresos mensuales: "))
        if monto_solicitado > 0 and tasa_interes_anual > 0 and plazo_meses > 0 and es_veraz in ['si', 'no']:
            break
        else:
            print("Por favor ingresa valores validos.")
       
    if es_veraz == 'no' and ((ingresos_mensuales * 30) / 100) >= (monto_solicitado / plazo_meses):
        tasa_interes_mensual = tasa_interes_anual / 12 / 100
        interes_total = monto_solicitado * tasa_interes_mensual * plazo_meses
        monto_total = monto_solicitado + interes_total
        pago_mensual = monto_total / plazo_meses

        print(f"El monto total a pagar es: {monto_total:.2f}")
        print(f"El interes total a pagar es: {interes_total:.2f}")
        print(f"El pago mensual es: {pago_mensual:.2f}")
    else:
        print("Lo sentimos, no puedes solicitar un prestamo si estas en el veraz.")

if calculadora == 1:
    while True:
        monto_solicitado = float(input("Ingresa el monto inicial: "))
        tasa_interes_anual = float(input("Ingresa la tasa de interes anual (en %): "))
        plazo_meses = int(input("Ingresa el plazo en meses: "))
        if monto_solicitado > 0 and tasa_interes_anual > 0 and plazo_meses > 0:
            break
        else:
            print("Por favor ingresa valores positivos.")

    tasa_interes_mensual = tasa_interes_anual / 12 / 100
    interes_total = monto_solicitado * tasa_interes_mensual * plazo_meses
    monto_final = monto_solicitado + interes_total

    print(f"El monto final despues de {plazo_meses} meses es: {monto_final:.2f}")
    print(f"El interes total a pagar es: {interes_total:.2f}")
