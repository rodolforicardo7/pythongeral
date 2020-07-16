#Testando o For com strings
frase = 'tesTando as lEtraS maísculas no for. Tudo para dar cErto.'
mensagem = ''
for letra in frase:
    if letra.isupper():
        print(letra) # para imprimir um embaixo do outro

print('') #Divisor

for letra in frase:
    if letra.isupper():
        print(letra, end='') # para imprimir um do lado do outro