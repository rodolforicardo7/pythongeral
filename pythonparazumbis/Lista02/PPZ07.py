''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. 

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 

Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas. '''

tamanho = float(input('Qual o tamanho em metros quadrados da área? '))
#o valor total em metros por lata é de 54.
#para saber o total de latas é preciso informar que o número deve ser inteiro
#para que o número de latas seja inteiro e não float.
latas = int(tamanho/54)
valor = latas*80

print('O valor total da pintura é de:', valor)
print('O total de latas é:', latas)

