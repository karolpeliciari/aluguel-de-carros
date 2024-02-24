from datetime import datetime

class Carro:
    def __init__(self, placa, cor, ano, combustivel, numero_de_portas, km_rodados, renavam, chassi, valor_de_locacao, modelo): 
        self.placa = placa
        self.cor = cor 
        self.ano = ano
        self.combustivel = combustivel
        self.numero_de_portas = numero_de_portas
        self.km_rodados = km_rodados
        self.renavam = renavam
        self.chassi = chassi
        self.valor_de_locacao = valor_de_locacao
        self.modelo = modelo
        self.locado = False
        self.data_hora_locacao = None
        self.data_hora_devolucao = None
    
    def alugar(self):
        self.locado = True
        self.data_hora_locacao = datetime.now()

    def devolver(self):
        self.locado = False
        self.data_hora_devolucao = datetime.now()

class Modelo:
    def __init__(self, nome, marca_do_modelo):
        self.nome = nome
        self.marca_do_modelo = marca_do_modelo
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)

class Marca:
    def __init__(self, nome):
        self.nome = nome
        self.modelos = []

    def adicionar_modelo(self, modelo):
        self.modelos.append(modelo)

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carros_alugados = []

    def alugar_carro(self, carro):
        carro.alugar()
        self.carros_alugados.append(carro)

    def devolver_carro(self,carro):
        carro.devolver()
        self.carros_alugados.remove(carro)

def main():
    fiat = Marca("fiat")
    palio = Modelo("palio", fiat)
    estrada = Modelo("estrada", fiat)
    ram = Modelo("ram", fiat)
    
    carro1 = Carro("sdf4568", "azul", 2020, "gasolina", 4, 145000, "1234567", "dvdfsh", 5000, estrada)
    carro2 = Carro("dvd6489","verde" , 2023, "oleo", 2, 65464, "84654654", "vfvdgfv", "9000", palio)
    carro3 = Carro("qse3455", "rosa", 2024, "gasolina", 4, 644,"56654685" , "vdghgxh", 60000, ram)
    

    palio.adicionar_carro(carro2)
    estrada.adicionar_carro(carro1)
    ram.adicionar_carro(carro3)


    cliente1 = Cliente("karol")
    cliente2 = Cliente("vini")

    cliente1.alugar_carro(carro3)
    cliente2.alugar_carro(carro2)
    
    carros = [carro1, carro2, carro3] 
    print(carros)
    
    for carro in carros:
        if carro.locado:
            print(f"o carro com a placa {carro.placa} esta alugado")
        else:
             print(f"o carro com a placa {carro.placa} esta disponivel para aluguel")

if __name__ == "__main__":
    main()
