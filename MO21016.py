# Jason Alexander Molina Ortiz ~ MO21016 ~ IIS GT08
# Calculadora de comisiones de vendedores
# Hotfix
print("=========================================")
print("BIENVENIDO A LA CALCULADORA DE COMISIONES")
print("=========================================")

nombre_trabajador = input("Ingresa tu nombre: ")
ventas_totales = float(input("Ingresa las ventas totales: $"))
comision = round(ventas_totales * 0.13, 2)

print("\n============================================================================")
print(f"¡Felicidades {nombre_trabajador}! Tu comision por las ventas que realizaste es de ${comision}")
print("============================================================================")
