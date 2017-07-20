def main():	
	funcionario = int(input())
	horas_trab = int(input())
	valor_hora = float(input())

	salario = float(horas_trab * valor_hora)

	print("NUMBER = %d" %funcionario)
	print("SALARY = U$ %0.2f" %salario)
if __name__ == '__main__':
	main()