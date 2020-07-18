''' # 9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. '''

kmpercorridos = float(input('Informe a quantidade de KM percorridos: '))
dias = int(input('Informe a quantidade de dias de aluguel: '))

diaria = 60
kmrodado = 0.15

print('O valor total a pagar é de: R$', kmpercorridos*kmrodado + dias*diaria)