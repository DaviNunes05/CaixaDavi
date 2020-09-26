import getpass
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

while True:
  print("\n**************************")
  print("*****Caixa Eletrônico*****")
  print("**************************")
  print('\nDigite os dados solicitados.')
  conta_digitada = input('Conta: ')
  senha_digitada = getpass.getpass('Senha: ')

  lista_contas = {
    '12345' : {
    'senha' : '123',
    'nome'  : 'Davi',
    'valor' : 'R$ 1200'
    }
  }

  if conta_digitada in lista_contas and senha_digitada == lista_contas[conta_digitada]['senha']:
    limpar()
    print('\nTitular: %s' % lista_contas[conta_digitada]['nome'])
    print('Escolha uma das opções abaix: ')
    print('1 - Saldo')
    opcao = input('Opção: ')
    if opcao == '1':
      print('Seu Saldo: %s'% lista_contas[conta_digitada]['valor'])
    print()
  else:
    print('Conta Inválida.')
  
  input('Pressione <Enter> para continuar.')
  limpar()