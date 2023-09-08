import sqlite3
conexao = sqlite3.connect ('organizador_tarefas.sqlite3')
cursor = conexao.cursor ()
sql_1 =  '''
CREATE TABLE categoria (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50)
    );'''

sql_2 = '''CREATE TABLE colaborador (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50),
	contato TEXT(50),
	matricula TEXT(11),
	CONSTRAINT colaborador_UN UNIQUE (matricula)
    );'''

sql_3 = '''CREATE TABLE tarefa (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	titulo TEXT(50),
	categoria_id INTEGER,
	"data" TEXT(50),
	colaborador_id INTEGER,
	status INT(3),
	CONSTRAINT tarefa_FK FOREIGN KEY (colaborador_id) REFERENCES categoria(id),
	);'''
    
	
cursor.execute(sql_1)
cursor.execute(sql_2)
cursor.execute(sql_3) 
conexao.commit ()
conexao.close ()
