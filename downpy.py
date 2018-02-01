#coding: utf-8
# Developer: Derxs
# Version: 1.0
from colored import fg, bg, attr
import requests, time, random, os

def obter_conexao():
	print('''{}
╔╦╗┌─┐┬ ┬┌┐┌╔═╗┬ ┬
 ║║│ │││││││╠═╝└┬┘
═╩╝└─┘└┴┘┘└┘╩   ┴ by Derxs v1.0{}
	'''.format(fg('magenta'), attr('reset')))

	conexao = requests.get(input('{}{}DownPy>{} '.format(fg('white'), bg('grey_15'), attr('reset'))), stream=True)
	
	tipo_arquivo = input('{}{}DownPy>Tipo de arquivo>{} '.format(fg('white'), bg('grey_15'), attr('reset')))
	
	print("{}{}DownPy>Baixando arquivo...{}".format(fg('white'), bg('grey_15'), attr('reset')))

	tamanho_arquivo = int(conexao.headers['content-length'])
	
	nome_arquivo = random.choice(['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'at', 'libero', 'tempus', 'dignissim', 'massa', 'ut', 'tempus', 'velit'])
	
	if os.path.exists(nome_arquivo) == True:
		nome_arquivo = random.choice(['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'at', 'libero', 'tempus', 'dignissim', 'massa', 'ut', 'tempus', 'velit'])

	with open('downpy-{}.{}'.format(nome_arquivo, tipo_arquivo), 'wb') as file:
		for conteudo in conexao.iter_content(chunk_size=1024*tamanho_arquivo):
			file.write(conteudo)

	print("{}{}DownPy>{}{}Download finalizado!\n{}{}DownPy>Nome do arquivo: downpy-{}.{}{}".format(fg('white'), bg('grey_15'), fg('black'), bg('white'), fg('white'), bg('grey_15'), nome_arquivo, tipo_arquivo, attr('reset')))
	exit(0)

def main():
	obter_conexao()

try:
	main()
except KeyboardInterrupt:
	print('\n{}{}DownPy>{}{}Você decidiu sair!{}'.format(fg('white'), bg('grey_15'), fg('black'), bg('red'), attr('reset')))
	exit(0)
