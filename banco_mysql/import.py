from database import *

class Loja:
    def __init__(self) -> None:
        self.nome = ""
        self.descricao = ""
        self.data_tarefa = ""
        self.estado_tarefa = ""
        self.db = Database()


    def informacoes(self):
        op = input("Deseja colocar as informações | [S/N]?").upper()
        while(op == "S"):
            self.nome = input("Insere o nome da loja aí: ")
            self.descricao = input("Qual a descrição dessa loja: ")
            self.data_tarefa = input("Qual é a atividade dela: ")
            self.estado_tarefa = input("Como está essa tarefa: ")

            loja = (self.nome,self.descricao,self.data_tarefa,self.estado_tarefa)
            chamar = self.db.insert(loja)
            if chamar == 1:
                print("Tarefa cadastrada com sucesso meu aliado!")

            op = input("\n Deseja colocar mais informações | [S/N]?")
            if op == "N":
                break

if __name__ == "__main__":
    l1 = Loja()
    l1.informacoes()