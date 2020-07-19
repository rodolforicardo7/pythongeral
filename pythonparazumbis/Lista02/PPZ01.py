""" 1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. """

lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))

if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
    print('Triângulo Equilátero')
elif (lado1 != lado2 and lado1!=lado3 and lado2!=lado3):
    print('Triângulo Escaleno')
else:
    print('Triângulo Isóceles')

