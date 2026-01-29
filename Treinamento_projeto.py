# Ex1: gorjeta

# valor = float(input("Qual o valor da conta? R$ "))
# porcentagem = float(input("Qual a porcentagem da gorjeta você gostaria de dar? "))

# gorjeta = valor * (porcentagem / 100)
# total = valor + gorjeta

# print(f"A gorjeta é R$ {gorjeta:.2f}")
# print(f"O total a ser pago é R$ {total:.2f}")

# Ex2: CPF válido

# try:
#     cpf = int(input("Digite o CPF (somente números): "))

#     if len(str(cpf)) != 11:
#         print('Erro: O CPF deve ter exatamente 11 dígitos.')
#     else:
#         print('CPF válido.')
# except ValueError:
#     print('Erro: O CPF deve conter apenas números.')

# Ex3: Contagem de vogais em um texto

# texto = input('Digite um texto: ')
# vogais = 'aeiouAEIOU'
# contador = 0

# for char in texto:
#     if char in vogais:
#         contador += 1

# print(f"O texto contém {contador} vogais.")

# Ex4: Palavras grandes

# texto = input('Digite um texto: ')
# lista = texto.split()
# lista_grande = []

# for item in lista:
#     if len(item) > 10:
#         lista_grande.append(item)
#     else:
#         continue
# print(f'palavra grande: {lista_grande}')

# Ex5: Gerador de senha segura

# import random

# def gerar_senha():
    
#     Maisculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     Minusculas = 'abcdefghijklmnopqrstuvwxyz'
#     Numeros = '0123456789'
#     Simbolos = '!@#$%^&*()-_=+[]{}|;:,.<>?/'
    
#     Senha = [
#         random.choice(Maisculas),
#         random.choice(Minusculas),
#         random.choice(Numeros),
#         random.choice(Simbolos)
#     ]
    
#     todos_caracteres = Maisculas + Minusculas + Numeros + Simbolos
#     Senha.extend(random.choices(todos_caracteres, k=8))
#     random.shuffle(Senha)
#     return ''.join(Senha)

# print(f"Senha gerada: {gerar_senha()}")

# Ex6: Pedra, papel e tesoura

# def Pedra_papel_tesoura():
#     import random

#     try:
#         Escolhas = ['pedra', 'tesoura', 'papel']

#         escolha_computador = random.choice(Escolhas)
#         escolha_jogador = (input('Escolha entre pedra, tesoura e papel: ')).lower()
#         print(escolha_computador)
        
#         if escolha_jogador == escolha_computador: 
#             print("Empate!") 
#         elif ( 
#             (escolha_jogador == "pedra" and escolha_computador == "tesoura") or 
#             (escolha_jogador == "papel" and escolha_computador == "pedra") or 
#             (escolha_jogador == "tesoura" and escolha_computador == "papel") 
#         ): 
#             print("Você venceu!") 
#         else: 
#             print("Você perdeu!")
            
#     except ValueError:
#         print('Erro: Escolha inválida.')
#         return 
    
# Pedra_papel_tesoura()

# Ex7: Jogo de adivinhar o número

# import random

# numero_aletorio = random.randint(1, 500)

# numero_escolhido = int(input("Escolha um número entre 1 e 500: "))

# while numero_aletorio != numero_escolhido:
#     if numero_aletorio > numero_escolhido:
#         numero_escolhido = int(input('Chute muito baixo tente de novo: '))
#     elif numero_aletorio < numero_escolhido:
#         numero_escolhido = int(input('Chute muito alto tente de novo: '))
    
# print('parabens acertou o numero')

# Ex8: Calculadora com tratamento de erros

# try:
#     n1 = int(input('Digite o primeiro número: '))
#     n2 = int(input('Digite o segundo número: '))
#     oper = input('Escolha a operação (| + | - | * | / |): ')

#     def Calculadora(operacao, num1, num2):
#         if operacao == '+':
#             resultado = num1 + num2
#             return resultado
#         elif operacao == '-':
#             resultado = num1 - num2
#             return resultado
#         elif operacao == '*':
#             resultado = num1 * num2
#             return resultado
#         elif operacao == '/' and num2 != 0:
#             resultado = num1 / num2
#             return resultado
#         else:
#             return 'Nao existe divisao por 0'
            
#     print(Calculadora(oper, n1, n2))
# except:
#     print('Apenas numeros')

# Ex9: Gerenciador de tarefas

# import os

# lista_tarefas = ["Estudar Python", "Fazer exercícios", "Ler documentação"]

# def finalizar_app():
#     print('Finalizando app')

# def exibir_menu():
    
#     print("1. Adicionar tarefa")
#     print("2. Visualizar tarefas ")
#     print("3. Remover tarefa ")
#     print("4. Sair\n")
    
#     escolher_opcao()
    
# def escolher_opcao():
#     try:
#         opcao_escolhida = int(input('Escolha uma opção: '))
        
#         if opcao_escolhida == 1:
#             adicionar_tarefas()
#             voltar_menu()
#         elif opcao_escolhida == 2:
#             visualizar_tarefas()
#             voltar_menu()
#         elif opcao_escolhida == 3:
#             remover_tarefas()
#             voltar_menu()
#         elif opcao_escolhida == 4:
#             finalizar_app()
#         else:
#             print('Opção inválida. Tente novamente.')
#             voltar_menu()
#     except ValueError:
#         print('Erro: Por favor, insira um número válido.')
#         voltar_menu()

# def adicionar_tarefas():
#     tarefa = input('qual tarefa gostaria de adicionar?: ')
#     lista_tarefas.append(tarefa)
#     print(f'Tarefa {tarefa} adicionada com sucesso!')
    
# def visualizar_tarefas():
#     for tarefa in lista_tarefas:
#         print(f'- {tarefa}')

# def remover_tarefas():
#     tarefa = input('qual tarefa gostaria de remover?: ')
#     if tarefa in lista_tarefas:
#         lista_tarefas.remove(tarefa)
#         print(f'Tarefa {tarefa} removida com sucesso!')
#     else:
#         print(f'Tarefa {tarefa} não encontrada.')
#         exibir_menu()
#         escolher_opcao()

# def voltar_menu():
#     input('\nPressione Enter para voltar ao menu principal...')
#     os.system('cls')
#     exibir_menu()
#     escolher_opcao()

# exibir_menu()

# Ex10: Contador de cédulas únicas

# def ATM():

#     try:
#         valor = int(input('qual valor quer sacar?: '))
#         lista_cedulas = [100, 50, 20, 10, 5, 2]
        
#         if valor % 2 == 1:
#             print('O valor deve ser multiplo de 2')
#         elif valor == 0:
#             print('Nao se poder sacar nada')
#         else:
#             print("Cédulas entregues:")
#             for cedula in lista_cedulas:
#                 quantidade = valor // cedula
#                 if quantidade > 0:
#                     print(f'A quantidada da {cedula} e {quantidade}: Valor total R$ {cedula * quantidade}')
        
#     except ValueError:
#         print('Valor deve ser valido')
    
# ATM()