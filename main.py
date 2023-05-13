from datetime import datetime
import os
import requests

def limpar_tela():
	os.system("cls")

def novo_post():
	titulo = input("Titulo: ")
	autor = input("Autor: ")
	conteudo = input("Conteudo: ")
	data = datetime.now()
	requests.post("http://127.0.0.1/postar", json={"titulo":titulo,"conteudo":conteudo,"data":str(data),"autor":autor})

def altera_post():
	identificador = input("Identificador: ")
	titulo = input("Titulo: ")
	autor = input("Autor: ")
	conteudo = input("Conteudo: ")
	data = datetime.now()
	requests.put(f"http://127.0.0.1/alterar/{identificador}", json={"titulo":titulo,"conteudo":conteudo,"data":str(data),"autor":autor})

def deleta_post():
	identificador = input("Identificador: ")
	requests.delete(f"http://127.0.0.1/deletar/{identificador}")

limpar_tela()

while True:
	print("1- Adicionar post")
	print("2- Alterar post")
	print("3- Deletar post")
	opcao = int(input(">>> "))

	if opcao == 1:
		limpar_tela()
		novo_post()

	elif opcao == 2:
		limpar_tela()
		altera_post()

	elif opcao == 3:
		limpar_tela()
		deleta_post()

	limpar_tela()
