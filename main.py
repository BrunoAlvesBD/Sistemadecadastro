from datetime import date
# biblioteca para manipular tempo 
import datetime

# A variável "hoje" contém a data de hoje.
# Para o dia do mês, use:  hoje.day
# Para o mês, use:         hoje.month
# Para o ano, use:         hoje.year
hoje = date.today()

# lista para o cadastro
cadastros = []

# função para exibir o menu de opções
def menu():
  print('----------------MENU---------------\
        \n1. Para inserir novo cadastro\
        \n2. Para alterar CPF\
        \n3. Para trocar sobrenomes\
        \n4. Para remover cadastro\
        \n5. Para listar todos os cadastros\
        \n6. Para Encerrar\
        \n-----------------------------------')

# função para inserir cadastro
def novo_cadastro():
  id_cadastro = input('Informe o ID ou deixe em branco para anexar automaticamente: ')
  primeiro_nome = input('Informe seu primeiro nome: ')
  sobrenome = input('Informe seu sobrenome: ')
  cpf = input('informe seu CPF: ')
  # validação do CPF: para verificar se o cpf tem 11 dígitos numéricos
  if len(str(cpf)) != 11:
    print('Erro!! O CPF deve conter 11 caracteres.')
    return
  nascimento = input('Informe sua data de nascimento da forma indicada: \nDIA/MES/ANO: ')

  # esta condicional está verificando se o ID está sendo informado, se não for pelo usuário, será acrecentado automaticamente
  if id_cadastro == '':
    
    id_cadastro = len(cadastros) +1
  else:
    id_cadastro = int(id_cadastro)

  
# este dicionário serve para guardas chave e valor, está armazanando as informações do cadastro
  cadastro = {
    'id': id_cadastro,
    'nome': primeiro_nome.capitalize() + ' ' + sobrenome.capitalize(),
    'cpf': cpf,
    'nascimento': datetime.datetime.strptime(nascimento, '%d/%m/%Y').date()
  }

  
# a list 'cadastros' está recebendo o dicionário 'cadastro'
  cadastros.append(cadastro)
# print(cadastros)
  print('Cadastro inserido corretamente!!')
  


# Função para alterar o CPF
def alteracao_cpf():
  id_cadastro = int(input('Informe o ID do cadastro para ser modificado: '))
  novo_cpf = input('informe seu novo CPF: ')

  for i in cadastros:
    if i['id'] == id_cadastro:
       i['cpf'] = novo_cpf
       print('Sucesso na operação do CPF!!')
       return

  print('Cadastro não encontrado.')

# função para alterar o sobrenome, primeiro verificando os IDs dos cadastros a serem trocados e chamando outra função 'alterar_nome'
def mudar_sobrenome():
  id_cad1 = int(input('Informe o ID do primeiro cadastro:  '))
  id_cad2 = int(input('Informe o ID do segundo cadastro: '))
  cadastro1 = None
  cadastro2 = None

  for i in cadastros:
    if i in cadastros:
      if i['id'] == id_cad1:
        cadastro1 = i
      elif i['id'] == id_cad2:
        cadastro2 = i

  if cadastro1 and cadastro2:
    cadastro1['nome'], cadastro2['nome'] = alterar_nome(cadastro1['nome'], cadastro2['nome'])
    print('Sobrenome trocado!!')
  else:
    print('Cadastro não encontrado.')

# Função que funciona em paralelo a função 'mudar-sobrenomes', esta faz a troca dos sobrenomes
def alterar_nome(nome1, nome2):
  sobrenome_Id1 = nome1.split(' ')[-1]
  sobrenome_Id2 = nome2.split(' ')[-1]

  nome1 = nome1.replace(sobrenome_Id1, sobrenome_Id2)
  nome2 = nome2.replace(sobrenome_Id2, sobrenome_Id1)

  return nome1, nome2

 # função para remover o cadastro
def remover_cadastro():
  id_cadastro = int(input('Informe o ID, para remover o cadastro:  '))
  for i in cadastros: 
    if i['id'] ==id_cadastro:
      cadastros.remove(i)
      print('Cadastro removido!!')
      return
  print('Cadastro não encontrado.')



# função para calcular a idade em dias
def idade_dias(nascimento):
  atual = datetime.date.today()
  diferenca = atual - nascimento
  dias = diferenca.days
  return dias

# função para mostrar os cadastros
def mostrar_cadastro():
  print('-------------CADASTROS--------------')
  for i in cadastros:
    idade = idade_dias(i['nascimento'])
    print('ID: ', i['id'])
    print('Nome: ',i['nome'])
    print('CPF: ',i['cpf'])
    print('Data de nascimento: ',i['nascimento'].strftime('%d/%m/%y'))
    print('Idade em dias: ', idade)

# loop para chamar as funções já criadas:
while True:
  menu()
  opcao = input('Informe a opção desejada: ')

  if opcao == '1':
    novo_cadastro()
  elif opcao == '2':
    alteracao_cpf()
  elif opcao == '3':
    mudar_sobrenome()
  elif opcao == '4':
    remover_cadastro()
  elif opcao == '5':
    mostrar_cadastro()
  elif opcao == '6':
    print('Saindo do programa...')
    break
  else:
    print('ERRO!! esta opção não faz parte do sistema, informe opção válida')