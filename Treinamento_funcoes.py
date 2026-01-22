# Ex1: Calcular idade

# def calcular_idade(ano_nascimento, ano_atual):
#     return ano_atual - ano_nascimento

# ano_nascimento = int(input('Digite seu ano de nascimento: '))
# ano_atual = int(input('Digite o ano atual: '))
# print(f'Sua idade é: {calcular_idade(ano_nascimento, ano_atual)} anos')

# Ex2: Tamanho da palavra

# def Calcular_tamanho_palavra(palavra):
#     return len(palavra)

# palavra = input('Digite a palavra para calcularmos o tamanho: ')
# print(f'O tamanho da palavra {palavra} e: {Calcular_tamanho_palavra(palavra)} caracteres')

# Ex3: Saudação personalizada

# def saudacao_personalizada(horario, nome):
#     if 5 <= horario < 12:
#         return f'Bom dia, {nome}!'
#     elif 12 <= horario < 18:
#         return f'Boa tarde, {nome}!'
#     else:
#         return f'Boa noite, {nome}!'
    
# nome = input('Qual seu nome: ')
# hora = int(input('Que horas sao: '))

# print(saudacao_personalizada(hora, nome))

# Ex4: Converter string para inteiro

# def converter_telefones(lista):  

#    return [int(telefone) for telefone in lista] 

# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

# def verificar_conversao(numero):
#     try:
#         for telefone in numero:
#             int(telefone)
#             return True
#     except ValueError:
#         return False

# print(verificar_conversao(converter_telefones(telefones)))

# Ex5: calculando o total de vendas

# entrada = input('Digite seus gastos: ').split()

# valor = sum(map(float, entrada))

# print(valor)

# Ex6: Listar pares

# numeros = input('Digite seus numeros: ').split()

# lista = map(int, numeros)

# filtrada = filter(lambda x: x % 2 == 0, lista)

# print(list(filtrada))

# Ex7: fusao de listas

# produtos = input('Digite os produtos separados por vírgula: ').split(',')
# precos = input('Digite os preços separados por vírgula: ').split(',')

# def fusao_de_listas(lista1, lista2):
#     for produto, preco in zip(lista1, lista2):
#         print(f"{produto.strip()}: {preco.strip()}")

# fusao_de_listas(produtos, precos)

# Ex8: calculadora

# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# oper = input('Escolha a operação (| + | - | * | / |): ')

# def Calculadora(operacao, num1, num2):
#     if operacao == '+':
#         resultado = num1 + num2
#         return resultado
#     elif operacao == '-':
#         resultado = num1 - num2
#         return resultado
#     elif operacao == '*':
#         resultado = num1 * num2
#         return resultado
#     elif operacao == '/' and num2 != 0:
#         resultado = num1 / num2
#         return resultado
#     else:
#         return 'Nao existe divisao por 0'
        
# print(Calculadora(oper, n1, n2))

# Ex9: gerador de funções personalizadas

# def gerar_desconto(n):
#     def Calcular(x):
#         return x * n
#     return Calcular

# preco_original = gerar_desconto(200)
# preco_a_pagar = preco_original(0.9)

# print(f'Preço final com desconto: {preco_a_pagar}')

# Ex10: somando números recursivamente

# def fatorial(n):
#     if n == 0:
#         return 1
#     return n * fatorial(n - 1)

# valor = int(input('Digite um numero para ver seu fatorial: '))
# print(fatorial(valor))