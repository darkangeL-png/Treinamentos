# Ex1: organizando uma lista de convidados

# conjunto_de_convidados = set()

# while True:
#     convidado = input('Digite o nome do convidado: ')
#     if convidado.lower() == 'sair':
#         break
    
#     conjunto_de_convidados.add(convidado)

# print(f"Convidados confirmados: {', '.join(conjunto_de_convidados)}")

# Ex2: descobrindo palavras comuns entre dois textos

# texto1 = set(input("Texto 1: ").lower().split()) 
# texto2 = set(input("Texto 2: ").lower().split()) 

# texto3 = texto1 & texto2

# Ex3: comparando listas de compra

# lista1 = set(input("Lista 1: ").lower().split(',')) 
# lista2 = set(input("Lista 2: ").lower().split(','))

# lista3 = lista1|lista2
# lista4 = lista1&lista2
# lista5 = lista1-lista2
# lista6 = lista2-lista1

# print(f"Lista de itens: {', '.join(lista3)}")  

# print(f"Itens em ambas as listas: {', '.join(lista4)}")  

# print(f"Itens exclusivos de Laura: {', '.join(lista5)}")  

# print(f"Itens exclusivos de Ana: {', '.join(lista6)}")

# Ex4: verificando permissões

# conjunto1 = set(input('Permissões principais: ').strip().lower().split(','))
# conjunto2 = set(input('Permissões solicitadas: ').strip().lower().split(','))

# sub_conjunto = conjunto2<=(conjunto1)

# if sub_conjunto:  
#     print("As permissões solicitadas fazem parte das permissões principais.")  
# else:  
#     print("As permissões solicitadas não fazem parte das permissões principais.") 

# Ex5: comparando conjunto de números

# equipe1 = set(input('Lista da equipe 1: ').strip().lower().split(','))
# equipe2 = set(input('Lista da equipe 2: ').strip().lower().split(','))
# equipe3 = equipe1 | equipe2
# tarefa_a_ser_removida = input('Tarefa a ser removida: ').lower()

# if tarefa_a_ser_removida in equipe3:
#     equipe3.remove(tarefa_a_ser_removida)

# print(equipe3)

# Ex6: cadastro de produtos

# lista_produtos = []

# def cadastrar_produto():
#     produto = input('Produto: ')
    
#     while produto.lower() != 'sair':
#         produto_quantidade = int(input('Quantidade: '))
#         novo_dicionario = dict(nome=produto, quantidade=produto_quantidade)
#         lista_produtos.append(novo_dicionario)
#         produto = input('Produto: ')
    
#     print(f"Dicionário de produtos: {lista_produtos}")
    
# cadastrar_produto()

# Ex7: atualizando informações no estoque

# lista_produtos = []

# def cadastrar_produto():
#     produto = input('Produto: ')
    
#     while produto.lower() != 'sair':
#         produto_quantidade = int(input('Quantidade: '))
#         novo_dicionario = dict(nome=produto, quantidade=produto_quantidade)
#         lista_produtos.append(novo_dicionario)
#         produto = input('Produto: ')
    
#     print(f"Dicionário de produtos: {lista_produtos}")
    
# def alterar_quantidade_produto():
#     produto_para_alterar = input('Nome do produto a ser atualizado: ')
    
#     produto_encontrado = False
#     for produto in lista_produtos:
#         if produto['nome'].lower() == produto_para_alterar.lower():
#             produto_para_alterar_quantidade = int(input('Nova quantidade: '))
#             produto['quantidade'] = produto_para_alterar_quantidade
#             produto_encontrado = True
#             break
    
#     if not produto_encontrado:
#         print('O produto nao existe.')
        
#     print(f"Dicionário de produtos atualizado: {lista_produtos}")
        
# cadastrar_produto()
# alterar_quantidade_produto()

# Ex8: analisando os participantes de uma maratona

# participantes = {"Mariana": 25, "Carlos": 32, "Beatriz": 28, "Rafael": 35} 

# print(f'Nomes dos participantes: {', '.join(participantes.keys())}\n') 

# for idade in participantes.values():
#     print(f'Idade dos participantes: {idade}')
    
# print()
# for nome, idade in participantes.items():
#     print(f'{nome} : {idade}')
    
# Ex9: gerenciando inscrições de um 

# participantes = {"Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},"Workshop 2": {"Fernanda", "Gustavo", "Helena"}} 

# participante_removido = input('Digite o nome da pessoa a ser removida: ')

# for workship,nomes in participantes.items():
    
#     nomes.discard(participante_removido)
    
# print('Lista atualizada')

# for workship,nomes in participantes.items():
    
#     print(f'{workship} : {nomes}')

# Ex10:analisando vendas por categoria
    
# vendas = { 
#     "Eletrônicos": [ 

#         {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

#         {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

#     ], 

#     "Eletrodomésticos": [ 

#         {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

#         {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

#     ], 

#     "Livros": [ 

#         {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

#         {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
# ]} 

# categorias = vendas.items()

# for categoria, tipos in categorias:
    
#     montante = 0
    
#     for tipo in tipos:
        
#         montante += tipo["quantidade"] * tipo["valor_unitario"] 
    
#     print(f"{categoria}: R$ {montante:.2f}") 
