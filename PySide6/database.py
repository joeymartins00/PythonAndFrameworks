from typing import Any
import mysql.connector

class Database():
    def __init__(self, banco="locadora") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco, user="root", password="")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor com  sucesso!", db_info)
        else:
            print("Erro ao conectar!!!")


    def insert(self,carro):
        self.connect()

        try:
            self.cursor.execute("INSERT INTO carros (nome_carro, marca_carro, cor_carro, ano_carro, placa_carro) VALUES (%s,%s,%s,%s,%s)", (carro[0],carro[1],carro[2],carro[3],carro[4]))
            self.conn.commit()
            return "Cadastrada com sucesso!"
        
        except Exception as erro:
            return erro

        finally:
            self.close_connection()
 

    def select(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM carros")
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
                SELECT * FROM carros
                                WHERE nome_carro LIKE '%{texto}%' OR placa_carro LIKE '%{texto2}%';
                                """)
            result = self.cursor.fetchall()

            for locadora in result:
                print(locadora[1],"  -  ",locadora[2])
                
                
        
        except Exception as erro:
            return erro

        finally:
            self.close_connection()



    def delete(self,id_carro):
        self.connect()
        try:
            self.cursor.execute(f'delete from carros where id = {id_carro}')
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
                UPDATE carros SET
                    nome_carro = '{dados[1]}',
                    marca_carro = '{dados[2]}',
                    cor_carro = '{dados[3]}',
                    ano_carro = '{dados[4]}',
                    placa_carro = '{dados[5]}'
                    WHERE id_carro = '{dados[0]}'
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
    db = Database()
    db.connect()
    # db.filter('valo', 'er')
    # db.update(dados)
    # db.insert()
    db.insert(carro)
    db.close_connection()