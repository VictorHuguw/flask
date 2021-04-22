import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

criarTabela = "CREATE TABLE IF NOT EXISTS hoteis (\
    id INTEGER AUTO INCREMENT PRIMARY KEY,\
    nome TEXT,\
    estrelas REAL,\
    diaria REAL,\
    cidade TEXT)"

criarHotel = "INSERT INTO  hoteis (nome,estrelas,diaria,cidade) VALUES ('hotei1','2','100','manaus')"

cursor.execute(criarTabela)
cursor.execute(criarHotel)

connection.commit()
connection.close()