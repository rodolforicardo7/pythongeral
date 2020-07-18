#Escreva um programa que leia a quantidade de dias, 
#horas, minutos e segundos do usuário. Calcule o total em segundos.

horas = int(input('Informe a hora: '))
minutos = int(input('Informe os minutos: '))
segundos = int(input('Informe os segundos: '))

horasemsegundos = horas * 3600
minutosemsegundos = minutos * 60

print('O valor total em segundos é:', horasemsegundos+minutosemsegundos+segundos, 'segundos.')
