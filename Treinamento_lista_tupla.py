# Ex1: Verificando itens na despensa

# Lista = ['Arroz','Feijao','Cafe','Leite']
# Lista_comparar = [item2.upper() for item2 in Lista]

# item = input('Qual item voce quer verificar: ')
# item_comparar = item.upper()

# if item_comparar in Lista_comparar:
#     print('Tem em casa')
# else:
#     print('Nao tem em casa, va comprar')

# Ex2: Organizando notas de um concurso de redação

# notas = [85, 70, 90, 60, 75]
# notas.sort()

# print(notas)

# Ex3: Registrando voluntários para uma campanha

# lista_participantes = []

# nome_participantes = input('Digite o nome do voluntário (ou sair para encerrar): ')

# while nome_participantes != 'sair':
#     lista_participantes.append(nome_participantes)
#     if nome_participantes.lower() == 'sair':
#         break
#     nome_participantes = input('Digite o nome do voluntário (ou sair para encerrar): ')

# print(lista_participantes)

# Ex4: Unindo o relatório de estoques

# Produtos_do_estoque_1 = ('Arroz', 'Feijão', 'Macarrão')
# Produtos_do_estoque_2 = ('Óleo', 'Sal', 'Açúcar')

# Produtos_do_estoque_total = Produtos_do_estoque_1 + Produtos_do_estoque_2
# print(Produtos_do_estoque_total)

# Ex5: Reorganizando uma lista de convidados

# lista_convidados = ['Ana', 'Pedro', 'Carlos']
# adicionar_pessoa = input('Digite o nome do novo convidado: ')
# adicionar_pessoa_posicao = int(input('Digite a posição na qual deseja inserir o convidado:  '))
# lista_convidados.insert(adicionar_pessoa_posicao, adicionar_pessoa)

# print(lista_convidados)

# Ex6: Ordenando os eventos

# eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
# eventos_registrados.reverse()

# print(eventos_registrados)

# Ex7:Corrigindo posições na lista de uma corrida de atletismo

# Lista = ['Ana', 'Carlos', 'Pedro']

# nome_incorreto = input('Digite o nome incorreto: ')
# nome_correto = input('Digite o nome correto: ')

# if nome_incorreto in Lista:
#     Lista.remove(nome_incorreto)
#     Lista.append(nome_correto)
#     print(Lista)
# else:
#     print('O nome nao esta na lista')

# Ex8: Removendo o último item de um 

# pedidos = input("Digite os pedidos feitos (separados por vírgula): ").split(", ")
# pedidos.pop()
# print(f'Lista de pedidos final: {pedidos}')

# Ex9: Calculando a média de notas

# notas = input('Digite as notas (separadas por virgula): ').split(',')
# notas_int = []

# for nota in notas:
#     notas_int.append(int(nota)) 

# def calcular_media(lista_de_notas):
#     notas_somadas = sum(lista_de_notas)
#     media = notas_somadas/ len(lista_de_notas)
#     print(f'Media final e de: {media:.2f}')

# calcular_media(notas_int)

# Ex10: Registrando dados de alunos

# alunos = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(',')

# for i in range(0, len(alunos), 3):
#     print(f'Aluno: {alunos[i]}')
#     print(f'Idade: {alunos[i+1]}')
#     print(f'Nota: {alunos[i+2]}')