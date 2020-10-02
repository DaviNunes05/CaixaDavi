import getpass
import os

def limpar():
	os.system('cls' if os.name == 'nt' else 'clear')

lista_contas = {
	'12345' : {
	'senha' : '123',
	'nome'  : 'Davi',
	'valor' : 1200,
	'admin' : False
},
	'654321': {
	'senha' : '123',
	'nome'  : 'Davi',
	'valor' : 3200,
	'admin' : True
}
}
caixa_cedulas = {
	'2'   : 0,
	'5'   : 0,
	'10'  : 6,
	'20'  : 7,
	'50'  : 2,
	'100' : 50
}

while True:
	print("\n**************************")
	print("*****Caixa Eletrônico*****")
	print("**************************")
	print('\nDigite os dados solicitados.')
	conta_digitada = input('Conta: ')
	senha_digitada = getpass.getpass('Senha: ')
	
	if conta_digitada in lista_contas and senha_digitada == lista_contas[conta_digitada]['senha']:
		saldo = lista_contas[conta_digitada]['valor']
		limpar()
		#print(saldo)
		print('\nTitular: %s' % lista_contas[conta_digitada]['nome'])
		print('Escolha uma das opções abaixo: ')
		print('1 - Saldo\n2 - Saque')
		if lista_contas[conta_digitada]['admin']:
			print('10 - Incluir Cédulas')
		opcao = input('Opção: ')

		if opcao == '1':
			print('Seu Saldo: %s'% lista_contas[conta_digitada]['valor'])

		elif opcao == '10' and lista_contas[conta_digitada]['admin']:
			qtd_digitada = input('Digite a quantidade de cédulas: ')
			cedula_digitada = input('Digite a cédula a ser incluída: ')
			caixa_cedulas[cedula_digitada] += int(qtd_digitada)
			print(caixa_cedulas)

		elif opcao == '2':
			valor_saque = int(input('Digite o Valor do Saque: '))
			att_saldo = valor_saque
			cedulas_saque = {}

			if saldo > valor_saque:

				if valor_saque // 100 > 0 and valor_saque // 100 <= caixa_cedulas['100']:
					cedulas_saque['100'] = valor_saque // 100
					valor_saque = valor_saque - valor_saque // 100 * 100
				
				if valor_saque // 50 > 0 and valor_saque // 50 <= caixa_cedulas['50']:
					cedulas_saque['50'] = valor_saque // 50
					valor_saque = valor_saque - valor_saque // 50 * 50
				
				if valor_saque // 20 > 0 and valor_saque // 20 <= caixa_cedulas['20']:
					cedulas_saque['20'] = valor_saque // 20
					valor_saque = valor_saque - valor_saque // 20 * 20

				if valor_saque // 10 > 0 and valor_saque // 10 <= caixa_cedulas['10']:
					cedulas_saque['10'] = valor_saque // 10
					valor_saque = valor_saque - valor_saque // 10 * 10
				
				if valor_saque // 5 > 0 and valor_saque // 5 <= caixa_cedulas['5']:
					cedulas_saque['5'] = valor_saque // 5
					valor_saque = valor_saque - valor_saque // 5 * 5

				if valor_saque // 2 > 0 and valor_saque // 2 <= caixa_cedulas['2']:
					cedulas_saque['2'] = valor_saque // 2
					valor_saque = valor_saque - valor_saque // 2 * 2

				if valor_saque != 0:
					print('Cédulas indisponíves para este valor.')

				else:
					for acerto_caixa in cedulas_saque:
						caixa_cedulas[acerto_caixa] -= cedulas_saque[acerto_caixa]
					
					lista_contas[conta_digitada]['valor'] -= att_saldo
					print('Saque as Notas: ')
					print(cedulas_saque)
					print(caixa_cedulas)
					print(lista_contas[conta_digitada]['valor'])
			
			else :
				print('\nSaldo Insuficiente')

	else:
		print('Conta Inválida.')

	input('Pressione <Enter> para continuar.')
	limpar()
