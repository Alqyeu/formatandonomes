# -*- coding: utf-8 -*-
"""Ályque - Análise de Produção Diária.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
# #Criando dados
# %%writefile producao.txt
#    roBERto luIS Costa
#    150
#    180
#    210

#Abrindo o arquivo
arquivo = open('producao.txt', 'r', encoding='utf-8')
#Lendo as linhas
nome = arquivo.readline()
manha = arquivo.readline()
tarde = arquivo.readline()
noite = arquivo.readline()
#Fechando o arquivo
arquivo.close()
#Formatando o nome do operador
operador = nome.strip().title()
#Formatando os dados transformando em int e removendo espaços brancos
turno_manha = int(manha.strip())
turno_tarde = int(tarde.strip())
turno_noite = int(noite.strip())
#Somando o total de peças produzidas
total = turno_manha + turno_tarde +turno_noite
#Mostrando os dados solicitados
print("Relátorio de operação diária:")
print(f"Operador: {operador}")
print(f"Total produzido: {total} peças")