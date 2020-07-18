""" #5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar. """

valordamercadoria = float(input('Informe o valor da mercadoria: '))
percentualdedesconto = float(input('Informe o percentual de desconto (%): '))

valordodesconto = valordamercadoria*percentualdedesconto/100
precoapagar = valordamercadoria - (valordamercadoria*percentualdedesconto/100)

print('O valor do desconto é de: R$', valordodesconto, '\nO preço a pagar é: R$', precoapagar)
