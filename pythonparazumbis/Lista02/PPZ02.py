""" 2. Determine se um ano é bissexto. Verifique no Google como fazer isso... """

# Da forma If e ELSE
print('Esse ano é BISSEXTO?\n')
ano = int(input('Informe o ano: '))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O ano é bissexto!')

else:
    print('O ano NÃO é bissexto!')

# Carregando a biblioteca CALENDAR e utilizando a função .ISLEAP
import calendar
anoteste = calendar.isleap(ano)
print(anoteste)