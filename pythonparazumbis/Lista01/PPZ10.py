''' 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias '''

print('PARE DE FUMAR!\n')

cigarros = int(input('Informe o número de cigarros fumados por dia: '))
anosfumando = int(input('Informe quantos anos de fumante: '))

dias = ((cigarros*10)/1440)*(anosfumando*365)

print('O total de dias perdidos:', dias)

