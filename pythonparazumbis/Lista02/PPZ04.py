''' Faça um Programa que leia três números e mostre o maior deles '''

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

if (numero1 >= numero2) and (numero1>=numero3):
    print('O maior número é:', numero1)
#se ele passar par o próximo elif, já sabemos que o A não é primeiro não é o maior
elif (numero2>=numero3):
    print('O maior número é:', numero2)
else:
    print('O maior número é:', numero3)