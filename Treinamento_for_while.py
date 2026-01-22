# Ex1: Lista de clientes

# clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

# for cliente in clientes:
#     print(f'Cliente: {cliente}')

# Ex2: Loop infinito com condição de parada

# contador = 0

# while contador < 10:
#     print("Processando dados...")
#     contador += 1

# Ex3: Repetição de mensagem de boas-vindas

# for i in range(5):
#     print("Bem-vindo ao Buscante!")

# Ex4: Soma total de vendas

# valores = [10, 20, 30, 40, 50]

# soma_total = 0

# for valor in valores:
#     soma_total += valor
# print(f"A soma total das receitas é: {soma}")

# Ex5: ignorar item da lista

# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for projeto in projetos:
#     if projeto == None:
#         print('Projeto ausente')
#     else:
#         print(f'{projeto}')

# Ex6: Break point em loop

# livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

# for livro in livros:
#     if livro == "O Hobbit":
#         print(f'O livro {livro} foi encontrado')
#         break

# Ex7: controle de vendas

# Livros_em_estoque = 5

# while Livros_em_estoque >= 0:
#     Livros_em_estoque -= 1
    
#     if Livros_em_estoque >= 0:
#         print(f'Livro vendido! Livros restantes em estoque: {Livros_em_estoque}')
#     else:
#         print('Estoque esgotado!')

# Ex8: Contagem regressiva para lançamento

# for N in range(10,0,-1):
#     if N %2 == 0:
#         print(f'Faltam apenas {N} segundos - Não perca essa oportunidade!')
#     else:
#         print(f'A contagem continua: {N} segundos restantes.')
# print('Aproveite a promoção agora!')

# Ex9: Lista de livros disponiveis

# livros = [
#     {"nome": "1984", "estoque": 5},
#     {"nome": "Dom Casmurro", "estoque": 0},
#     {"nome": "O Pequeno Príncipe", "estoque": 3},
#     {"nome": "O Hobbit", "estoque": 0},
#     {"nome": "Orgulho e Preconceito", "estoque": 2}
# ]

# for livro in livros:
#     if livro['estoque'] == 0:
#         continue
#     else:
#         print(f'Livro disponível:{livro ["nome"]}')

# Ex10: Validar usuario e senha

# senha = input('Digite a senha: ')
# usuario = input('Digite o usuario: ')

# cadastro_aceito = False

# while cadastro_aceito == False:
    
#     if len(usuario) < 5:
#         print('Usuario deve ter mais de 5 caracteres')
#         usuario = input('Digite o usuario: ')
#     elif len(senha) < 8:
#         print('Senha deve ter mais de 8 caracteres')
#         senha = input('Digite a senha: ')
#     else:
#         cadastro_aceito = True

# print('Usuario e senha aceitos!')