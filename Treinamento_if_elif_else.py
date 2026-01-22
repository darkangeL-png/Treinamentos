# Ex1: Função que compara duas vendas e informa qual é maior

# def Comparador_de_vendas(a,b):
#     if a > b:
#         print("Venda A é maior")
#     elif b > a:
#         print("Venda B é maior")
#     else:
#         print("As vendas são iguais")

# input_a = input('Digite o valor da Venda Maca: ')
# input_b = input('Digite o valor da Venda Banana: ')
# Comparador_de_vendas(int(input_a), int(input_b))

# Ex2: Função que soma a quantidade de dias para completar 3 tarefas
    
# soma_de_dias = 0
# tarefa_1 = int(input('Digite a quantidade de dias para a tarefa 1: '))
# tarefa_2 = int(input('Digite a quantidade de dias para a tarefa 2: '))
# tarefa_3 = int(input('Digite a quantidade de dias para a tarefa 3: '))

# if tarefa_1 > 0 and tarefa_2 > 0 and tarefa_3 > 0:
#     soma_de_dias = tarefa_1 + tarefa_2 + tarefa_3
#     print(f'A soma total de dias para completar as 3 tarefas é: {soma_de_dias} dias')
# else:
#     print('Nao é possivel inserir valores negativos')

# Ex3: Função que verifica se a temperatura está adequada para uma sala

# Temperatura = float(int(input('Digite a temperatura atual: ')))

# if Temperatura < 25:
#     print('Temperatura certa para a sala')
# else:
#     print('Temperatura alta para a sala')

# Ex4: Função que calcula o IMC (Índice de Massa Corporal)

# peso = float(input('Digite seu peso em kg: '))
# altura = float(input('Digite sua altura em metros: '))
# imc = peso / (altura ** 2)

# if imc < 18.5:
#     print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso.')
# elif 18.5 <= imc < 25:
#     print(f'Seu IMC é {imc:.2f}. Você está com o peso normal.')
# else: 
#     print(f'Seu IMC é {imc:.2f}. Você está acima do peso.')

# Ex5: Calculadora de orcamento mensal

# Despesas_fixas = float(input('Digite o valor das despesas fixas mensais: R$ '))
# Despesas_variaveis = float(input('Digite o valor das despesas variaveis mensais: R$ '))
# Limite = 3000

# if Limite > (Despesas_fixas + Despesas_variaveis):
#     print('Orçamento mensal está positivo.')
# else:
#     print('Orçamento mensal está negativo.')

# Ex6: verificação por horário comercial

# Hora_atual = getattr(__import__('time'), 'localtime')().tm_hour 
# print(f'Hora atual: {Hora_atual}h')

# if Hora_atual >= 8 and Hora_atual < 18:
#     print('horário comercial')
# else:
#     print('fora do horário comercial')

# Ex7: Media de notas escolares

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))

# Media = float( nota1 + nota2 + nota3 ) / 3

# if Media >= 7:
#     print(f'Aprovado de ano. Sua média foi: {Media:.2f}')
# elif Media < 7 and Media >= 5:
#     print(f'Recuperação. Sua média foi: {Media:.2f}')
# else:
#     print(f'Reprovado. Sua média foi: {Media:.2f}')

# Ex8: preco pedagio 

# distancia = float(input('Digite a distância percorrida em km: '))

# if distancia <= 100:
#     print(f'O preço do pedágio é R$ 10,00 para {distancia} km percorridos.')
# elif distancia > 100 and distancia <= 200:
#     print(f'O preço do pedágio é R$ 20,00 para {distancia} km percorridos.')
# else:
#     print(f'O preço do pedágio é R$ 30,00 para {distancia} km percorridos.')

# Ex9: Par ou Ímpar

# numero = int(input('Digite um número inteiro: '))
# if numero % 2 == 0:
#     print(f'O número {numero} é Par.')
# else:
#     print(f'O número {numero} é Ímpar.')

# Ex10: Verificação de emprestimo

# salario = float(input('Digite o valor do seu salário mensal: R$ '))
# valor_possivel = salario*0.3
# valor_emprestimo = float(input('Digite o valor do empréstimo desejado: R$ '))

# if valor_possivel > valor_emprestimo and salario > 1999:
#     print('Empréstimo aprovado!')
# elif salario < 2000:
#     print('Empréstimo negado: renda insuficiente.')
# else:
#     print('Empréstimo negado: parcela acima de 30% da renda.')