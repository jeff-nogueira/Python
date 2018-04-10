#!/usr/bin/python
# -*- coding: latin-1 -*-
# Importa o modulo de conexao com o mysql
import MySQLdb

# Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
db = MySQLdb.connect(host="mysql.lhost03.w3br.com", user="lhost03", passwd="suasenha", db="seudb")
# Posiciona o cursor
cursor = db.cursor()
# Executa a consulta na tabela selecionada
cursor.execute("SELECT * FROM seudb.suatabela")
# Conta o numero de linhas na tabela
numrows = int(cursor.rowcount)
# Obtendo resultados
print "--------------------------------------------------"
print "| ID  Campo                                      |"
print "--------------------------------------------------"
# Laço for para retornar os valores
for row in cursor.fetchall():
   print " ",row[0]," ",row[1
