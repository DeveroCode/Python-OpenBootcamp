peso = float(input('Ingrese su peso en kg: '))
esatura = float(input('Ingrese su estatura en m: '))

imc = peso / (esatura ** 2)
imc_redondeado = round(imc, 2)

print('Su IMC es: ', imc)
