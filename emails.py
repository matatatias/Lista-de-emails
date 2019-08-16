#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

#Listas e variáveis

listaNomes = ['John Doe', 'Peter Parker', 'Mary Jane Watson-Parker', 'James Doe', 'John Elvis Doe', 'Jane Doe', 'Penny Parker']

nomesUsuario = []

emails = []

emailsFinal = []

domain = '@company.com'


#Separa os nomes, armazena sobrenome e iniciais para criar os nomes de usuários

for x in listaNomes:
	nome = x
	nome = re.sub('-','',nome)

	nomes = nome.rsplit(' ')
	sobrenome = len(nomes)

	inicialPrimeiroNome = nomes[0]
	inicialPrimeiroNome = inicialPrimeiroNome[0:1]

	inicialDois = nomes[1]
	inicialDois = inicialDois[0:1]

	inicialSobrenome = nomes[sobrenome-1]

	if(sobrenome<=2):
		email = (inicialSobrenome+'.'+inicialPrimeiroNome)
	else:
		email = (inicialSobrenome+'.'+inicialPrimeiroNome+'.'+inicialDois)
	
	email = email.lower()

	nomesUsuario.append(email)
	
	

#Verifica repetições e acrescenta o número às repetições seguintes

numeroUsuarios = len(nomesUsuario)

for x in range(0,numeroUsuarios):

	quantidadeOcorrencias = nomesUsuario.count(nomesUsuario[x])

	if quantidadeOcorrencias > 1:
		numeroOrdem = nomesUsuario[0:x].count(nomesUsuario[x])
		if numeroOrdem>=1:
			emails.append(nomesUsuario[x]+str(numeroOrdem+1))
		else:
			emails.append(nomesUsuario[x])
	else:
		emails.append(nomesUsuario[x])
		
#Combina nomes e emails e armazena numa nova lista

for x in range (0,numeroUsuarios):
	emailsFinal.append(listaNomes[x]+' <'+emails[x]+domain+'>')	
	
print (emailsFinal)
