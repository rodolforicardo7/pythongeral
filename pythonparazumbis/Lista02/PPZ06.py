''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo: '''
''' a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$ '''

valordahora = float(input('Informe o valor da sua hora trabalhada: R$ '))
horasnomes = int(input('Informe o número de horas trabalhadas no mês: '))
salariobruto = valordahora*horasnomes
impostoderenda = salariobruto*0.11
inss = salariobruto*0.08
sindicado = salariobruto*0.05

print('Salário Bruto: R$', round(salariobruto, 2))
print('Desconto INSS: R$', round(inss, 2))
print('Imposto de Renda: R$', round(impostoderenda, 2))
print('Sindicato: R$', round(sindicado, 2))
print('Salário Líquido: R$', round(salariobruto - (inss+impostoderenda+sindicado), 2),'\n')

