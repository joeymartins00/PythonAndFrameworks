import sqlite3

banco = sqlite3.connect('cadastro_276.db')
cursor = banco.cursor()


nome = "Enilda Caceres"
idade = 45
email = "enilda@gmail.com"
tel = "67981697437"


cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"','"+tel+"')")

#cursor.execute("UPDATE pessoas SET idade = 32 WHERE idade = 45")


#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text, tel text)")
#cursor.execute("INSERT INTO pessoas VALUES ('Lucas', 18, 'lucas_lss@gmail.com', '67992680894')")


#cursor.execute("DELETE FROM pessoas WHERE nome = 'Enilda Caceres'")
banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) 