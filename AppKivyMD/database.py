from typing import Any
import mysql.connector

class Database():
    def __init__(self, banco="meuapp") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco, user="root", password="")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor com  sucesso!", db_info)
        else:
            print("Erro ao conectar!!!")


    def insert(self,pessoa):
        self.connect()

        try:
            self.cursor.execute("INSERT INTO pessoas (nome, cpf, email, telefone, endereco) VALUES (%s,%s,%s,%s,%s)", (pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4]))
            self.conn.commit()
            return "Cadastrada com sucesso!"
        
        except Exception as erro:
            return erro

        finally:
            self.close_connection()
 

    def select(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM pessoas")
            result = self.cursor.fetchall()
            return result

        except Exception as erro:
            return erro

        finally:
            self.close_connection()



    def filter(self,texto,texto2):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM pessoas
                                WHERE NOME LIKE '%{texto}%' OR CPF LIKE '%{texto2}%';
                                """)
            result = self.cursor.fetchall()

            for task in result:
                print(task[1],"  -  ",task[2])
                
                
        
        except Exception as erro:
            return erro

        finally:
            self.close_connection()



    def delete(self,id):
        self.connect()
        try:
            self.cursor.execute(f'delete from pessoas where id = {id}')
            self.conn.commit()
            self.select()

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()



    
    def update(self,dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                UPDATE pessoas SET
                    nome = '{dados[1]}',
                    cpf = '{dados[2]}',
                    email = '{dados[3]}',
                    telefone = '{dados[4]}',
                    endereco = '{dados[5]}'
                    WHERE id = '{dados[0]}'


                                """)
            self.conn.commit()
            self.select()

        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()




    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!")



if __name__ == "__main__":
    # id = int(input("Digite o id da tarefa a ser alterada: "))
    # nome = input("Digite o novo nome: ")
    # desc = input("Digite a nova descrição: ")
    # data = input("Digite a nova data: ")
    # estado = input("Digite o novo estado: ")
   

    # dados = (id,nome,desc,data,estado)

    db = Database()
    db.connect()
    # db.filter('valo', 'er')
    # db.update(dados)
    db.insert()
    # db.insert(task)
    db.close_connection()