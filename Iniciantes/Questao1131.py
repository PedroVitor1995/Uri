def main():
	qtd_jogos = 0
	inter = 0
	gremio =0
	empate = 0

	while True:

		gols = input().split(" ")
		gol_inter = int(gols[0])
		gol_gremio = int(gols[1])
	
		qtd_jogos += 1

		if(gol_inter > gol_gremio):
			inter += 1
		elif(gol_gremio > gol_inter):
			gremio += 1
		else:
			empate += 1

		resposta = 0
		while True:
			print("Novo grenal (1-sim 2-nao)")
			opcao = int(input())
			if(opcao == 1 or opcao == 2):
				resposta = opcao
				break;
		if(resposta == 2):
			print("%d grenais"%qtd_jogos)
			print("Inter:%d"%inter)
			print("Gremio:%d"%gremio)
			print("Empates:%d"%empate)

			if(inter > gremio and inter > empate):
				print("Inter venceu mais")
			elif(gremio > inter and gremio > empate):
				print("Gremio venceu mais")
			else:
				print("Nao houve vencedor")
			break;
if __name__ == '__main__':
	main()