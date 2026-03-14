import re

# Ex01: Ajustando nomes de produtos

# def ajustar_nome(produto):
    
#     produto_ajustado = produto.strip().lower()
#     return produto_ajustado

# item = input('Digite o nome do produto: ')
# print(ajustar_nome(item))

# Ex02: Formatando uma saudação

# def imprimir_nome():
#     nome = input('Digite o nome do cliente: ')
#     cidade = input('Digite a cidade do cliente: ')
    
#     print(f'Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}.')

# imprimir_nome()

# Ex03: Decifrando pistas com palavras-chave

# def imprimir_letras():
    
#     palavra_chave = input('Digite a palavra chave: ')
    
#     print(f'As primeiras sao: {palavra_chave[:3]}')
#     print(f'As ultimas sao: {palavra_chave[-3:]}')
    
# imprimir_letras()

# Ex04: Verificando o início e o fim de uma String

# def inicio_e_fim():
    
#     url = input('Digite sua URL: ')
    
#     if url.startswith('https://') & url.endswith('.com'):
#         print('URL válida!')
#     else:
#         print('URL inválida!')
    
# inicio_e_fim()

# Ex05: Encontrando números em um texto

# def numeros_no_texto():
    
#     mensagem = input('Digite a descrição da receita: ')
    
#     numero_na_mensagem = re.findall(r"\d+", mensagem)
    
#     print(f'O número da receita é: {numero_na_mensagem}')

# numeros_no_texto()

# Ex06: Substituindo palavras específicas

# def substituir_palavras():
    
#     texto = input('Digite o texto a ser revisado: ')
#     palavra_substituir = input('Qual palavra deseja substituir?: ')
#     palavra_nova = input('Qual palavra nova?: ')
    
#     return re.sub(rf"{palavra_substituir}", f"{palavra_nova}", f'{texto}')
    
# print(substituir_palavras())

# # Ex07: Validando nomes com Regex

# def validar_nome():
    
#     nome = input('Digite o nome do cliente para validação: ').strip()

#     if re.fullmatch(r'[A-ZÁÉÍÓÚÂÊÎÔÛÃÕÇ][a-záéíóúâêîôûãõç]+( [A-ZÁÉÍÓÚÂÊÎÔÛÃÕÇ][a-záéíóúâêîôûãõç]+)*', nome):
#         print('Nome cadastrado com sucesso!')
#     else:
#         print('Nome inválido! Certifique-se de que cada nome comece com letra maiúscula e não contenha números.')
        
# validar_nome()

# Ex08: Verificando o formato de um CPF

# def verificar_cpf():
    
    # cpf = input('Digite seu CPF no formato XXX.XXX.XXX-XX: ')
    
#     padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
#     resultado = re.search(padrao_cpf, cpf)

#     if resultado:
#         print('Cpf válido!')
#     else:
#         print('Cpf inválido!')

# verificar_cpf()

# Ex09: Encontrando palavras que começam com uma letra específica

# def palavra_ha_busca():
    
#     titulo = input('Digite o título do livro: ')
#     letra = input('Digite a letra inicial para pesquisar: ')
#     titulo_separado = titulo.strip()
    
#     print(re.findall(rf'\b{letra}[a-zà-ÿ]*', titulo_separado)) 
    
# palavra_ha_busca()

# Ex10: Agrupando informações dos pacientes

# def informações_dos_pacientes():
#     informacoes = input('Digite o nome completo e o ano de nascimento do paciente: ')
#     padrao = r'(\w+) (\w+) - (\d{4})'
    
#     resultado = re.search(padrao, informacoes)
    
#     primeiro_nome = resultado.group(1)
#     segundo_nome = resultado.group(2)
#     ano = resultado.group(3)
    
#     return print(f'Primeiro nome: {primeiro_nome} | Segundo nome: {segundo_nome} | Ano de nascimento: {ano}')

# informações_dos_pacientes()