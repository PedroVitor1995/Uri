# -*- coding: utf-8 -*-
def main():
	numeros  = (raw_input('').split())
	valor_a = float(numeros[0])
	valor_b = float(numeros[1])
	valor_c = float(numeros[2])
	diferenca_lados_b_c = valor_b - valor_c
	soma_lados_b_c = valor_b + valor_c
	diferenca_lados_a_c = valor_a - valor_c
	soma_lados_a_c = valor_a + valor_c
	diferenca_lados_b_c = valor_b - valor_c
	soma_lados_a_b = valor_a + valor_b

	if valor_a > diferenca_lados_b_c and valor_a < soma_lados_b_c:
	    if valor_b > diferenca_lados_a_c and valor_b < soma_lados_a_c:
	        if valor_c > diferenca_lados_b_c and valor_c < soma_lados_b_c:
	            perimetro_triangulo = valor_a + valor_b + valor_c
	            print('Perimetro = %.1f') % perimetro_triangulo
	else:
	    area_trapezio = (valor_a + valor_b) / 2 * valor_c
	    print('Area = %.1f') % area_trapezio
if __name__ == '__main__':
	main()