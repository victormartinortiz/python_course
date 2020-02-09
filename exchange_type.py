def run():
	print('C A L C U L A D O R A  D E  D I V I S A S')
	print('Convierte pesos argentinos a pesos colombianos.')
	print('')

	amount = float(input('Ingresa la cantidad de pesos argentinos que quieres convertir:'))
	
	result = foreign_exchange_calculator(amount)

	print('${} pesos argentinos son ${} pesos colombianos'.format(amount, result))
	print('')

def foreign_exchange_calculator(amount):
	ar_to_col_rate = 56.20
	return ar_to_col_rate * amount

if __name__ == '__main__':
	run()