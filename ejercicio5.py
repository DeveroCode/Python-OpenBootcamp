# Crear una funcion que determine si un año es bisiesto o no. Utiliza lo siguiente como hack
# Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
# Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
# El año es un año bisiesto (tiene 366 días).
# El año no es un año bisiesto (tiene 365 días).

def año_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'El {year} es bisiesto')
    else:
        print(f'El {year} no es bisiesto')


año_bisiesto(2023)
