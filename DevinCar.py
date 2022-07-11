from abc import ABC, abstractclassmethod
import os
import uuid
myuuid = uuid.uuid4()


veiculosDisponiveis = []
vendasTriciclos = []
vendasCarros = []
vendasCaminhonetes = []
veiculosVendidos = []

class Transferencia:
    def __init__(self):
        self.historicoTransferencia = []


    def gravarTransferencia(self):
        return self.historicoTransferencia.append(Veiculo.listarVendidos())


class Veiculo(ABC):
    def __init__(self, data_fabricacao, nome, placa, valor, cor):
        self.numero_chassi = str(myuuid)
        self.data_fabricacao = data_fabricacao
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.cpf_comprador = 0
        self.cor = cor
        
    def listarVendidos():
        global veiculosVendidos
        print(veiculosVendidos)

    def maiorValor():
        global veiculosVendidos
        maior = veiculosVendidos[0]
        for i in veiculosVendidos:
            if maior["Valor"] < i["Valor"]:
                maior = i
                print(maior["Valor"])

    def menorValor():
        global veiculosVendidos
        menor = veiculosVendidos[0]
        for i in veiculosVendidos:
            if menor["Valor"] > i["Valor"]:
                menor = i
                print(menor["Valor"])

    def estoque():
        global veiculosDisponiveis
        print(len(veiculosDisponiveis))

    @abstractclassmethod   
    def venderVeiculo(self):
        pass
    @abstractclassmethod
    def listarInformacoes(self):
        pass
    @abstractclassmethod
    def alterarInformacoes(self):
        pass


    def menu():
        opcao = None
        while opcao != 0:
            os.system('cls') or None
            print('1 - Vender Um Veicúlo')
            print('2 - Listar Informações')
            print('3 - Alterar Informações')
            print('4 - Listar Veicúlos Vendidos')
            print('5 - Listar Historico De Transferência')
            print('6 - Carros Disponiveis')
            print('7 - Listar Veicúlo Com Maior Preço Vendido')
            print('8 - Listar Veicúlo Com Menor Preço Vendido')
            print('0 - Para Sair')
            opcao = int(input('Digite Uma Opção : '))
            os.system('cls')

            if opcao == 1:
                op = int(input(""" Qual Categoria Deseja Fazer a Venda ? : 
                            1 - Para Moto/Triciclo
                            2 - Para Carros
                            3 - Para Caminhonetes
                            : """))

                if op == 1:
                    moto.venderVeiculo(moto, 0, '', 0)
                    os.system('pause')
                elif op == 2:
                    carro.venderVeiculo(carro, 0, '', 0)
                    os.system('pause')
                elif op == 3:
                    caminhonete.venderVeiculo(caminhonete, 0, '', 0)
                    os.system('pause')
                
            elif opcao == 2:
                op = int(input(""" Qual Categoria Deseja Listar Informações ? : 
                            1 - Para Moto/Triciclo
                            2 - Para Carros
                            3 - Para Caminhonetes
                            : """))

                if op == 1:
                    moto.listarInformacoes()
                    os.system('pause')
                elif op == 2:
                    carro.listarInformacoes()
                    os.system('pause')
                elif op == 3:
                    caminhonete.listarInformacoes()
                    os.system('pause')
            elif opcao == 3:
                op = int(input("""Qual Categoria Deseja Alterar Informações ? : 
                                            1 - Para Moto/Triciclo
                                            2 - Para Carros
                                            3 - Para Caminhonetes
                                            : """))

                if op == 1:
                    moto.alterarInformacoes()
                    os.system('pause')
                elif op == 2:
                    carro.alterarInformacoes()
                    os.system('pause')
                elif op == 3:
                    caminhonete.alterarInformacoes()
                    os.system('pause')
            elif opcao == 4:
                op = int(input("""Qual Categoria Deseja Listar Os Veicúlos Vendidos ? : 
                                                            1 - Para Moto/Triciclo
                                                            2 - Para Carros
                                                            3 - Para Caminhonetes
                                                            : """))

                if op == 1:
                    moto.listarVeiculos()
                    os.system('pause')
                elif op == 2:
                    carro.listarVeiculos()
                    os.system('pause')
                elif op == 3:
                    caminhonete.listarVeiculos()
                    os.system('pause')
            elif opcao == 5:
                transf.gravarTransferencia()
                os.system('pause')
            elif opcao == 6:
                Veiculo.estoque()
                os.system('pause')
            elif opcao == 7:
                Veiculo.maiorValor()
                os.system('pause')
            elif opcao == 8:
                Veiculo.menorValor()
                os.system('pause')
            elif opcao == 0:
                break        

class Moto_Triciclo(Veiculo):
    def __init__(self, nome, placa, cor, potencia, totalRodas):
        self.data_fabricacao = '26/04/2022'
        self.numero_chassi = str(myuuid)
        self.nome = nome
        self.placa = placa
        self.cor = cor
        self.potencia = potencia
        self.totalRodas = totalRodas
        self.cpf = 0
        self.valor = 0
        self.data = ''
   
    def __dict__(self):
        return  {
            "Tipo" : 'Triciclo',
            "Nome": self.nome,
            "Numero Do Chassi": self.numero_chassi,
            "Placa": self.placa,
            "Cpf Do Comprador" : self.cpf,
            "Valor" : self.valor,
            "Cor" : self.cor,
            "Data Da Compra" : self.data
        }

    
    def venderVeiculo(self, veiculo, cpf, data, valor):
        self.cpf = input('Digite o Cpf: ')
        self.data = input('Digite a Data: ')
        self.valor = input('Digite o Valor: ')
        global veiculosDisponiveis
        global vendasTriciclos
        global veiculosVendidos
        super().venderVeiculo()
        vendasTriciclos.append(veiculo.__dict__())
        veiculosDisponiveis.pop(0)
        veiculosVendidos.append(veiculo.__dict__())
        print('Parabéns, Moto Vendida!')
        
    def listarInformacoes(self):
        global carrosDisponiveis
        global vendasTriciclos
        super().listarInformacoes()
        for i in vendasTriciclos:
            print(i["Nome"], i["Placa"], i["Numero Do Chassi"], i["Valor"])

            
    def alterarInformacoes(self):
        global vendasTriciclos
        super().alterarInformacoes()
        self.placa = input('Informe a Placa Que Deseja Pesquisar : ')
        self.novoValor = input('Informe o Novo Valor : ')
        self.novaCor = input('Informe a Nova Cor : ')
        for i in vendasTriciclos:
            if i["Placa"] == self.placa:
                i["Valor"] = self.novoValor
                i["Cor"] = self.novaCor
        
        
    def listarVeiculos(self):
        global vendasTriciclos
        print(vendasTriciclos)
    
        
class Carro(Veiculo):
    def __init__(self, nome, placa, cor, totalPortas, potencia, flex = True or False):
        self.data_fabricacao = '10/03/2022'
        self.numero_chassi = str(myuuid)
        self.nome = nome
        self.placa = placa
        self.valor = 0
        self.cpf = 0
        self.cor = cor
        self.totalPortas = totalPortas
        self.potencia = potencia
        self.flex = flex
        self.data = ''

    def __dict__(self):
        return {
            "Tipo": 'Carro',
            "Nome": self.nome,
            "Numero Do Chassi": self.numero_chassi,
            "Placa": self.placa,
            "Cpf Do Comprador" : self.cpf,
            "Valor" : self.valor,
            "Cor": self.cor,
            "Data Da Compra" : self.data
        }
        
    def venderVeiculo(self, veiculo, cpf, data, valor):
        self.cpf = input('Digite o Cpf: ')
        self.data = input('Digite a Data: ')
        self.valor = input('Digite o Valor: ')
        global veiculosDisponiveis
        global vendasCarros
        global veiculosVendidos
        super().venderVeiculo()
        vendasCarros.append(veiculo.__dict__())
        veiculosDisponiveis.pop(0)
        veiculosVendidos.append(veiculo.__dict__())
        print('Parabéns, Carro Vendido!')

    def listarInformacoes(self):
        global carrosDisponiveis
        global vendasTriciclos
        super().listarInformacoes()
        print(f'Modelo : {carro.nome}\n Placa : {carro.placa}\n Chassi : {carro.numero_chassi}\n Flex : {carro.flex}')

    def alterarInformacoes(self):
        global vendasCarros
        super().alterarInformacoes()
        self.placa = input('Informe a Placa Que Deseja Pesquisar : ')
        self.novoValor = input('Informe o Novo Valor : ')
        self.novaCor = input('Informe a Nova Cor : ')
        for i in vendasCarros:
            if i["Placa"] == self.placa:
                i["Valor"] = self.novoValor
                i["Cor"] = self.novaCor

    def listarVeiculos(self):
        global vendasCarros
        print(vendasCarros)
        

class Caminhonete(Veiculo):
    def __init__(self, nome, placa, totalPortas, capacidadeCarregamento, potencia, combustivel, ):
        self.data_fabricacao = '18/08/2022'
        self.numero_chassi = str(myuuid)
        self.cor = 'Roxa'
        self.nome = nome
        self.placa = placa
        self.valor = 0
        self.cpf = 0
        self.totalPortas = totalPortas
        self.capacidadeCarregameto = capacidadeCarregamento
        self.potencia = potencia
        self.combustivel = combustivel
        self.data = ''

    def __dict__(self):
        return {
            "Tipo": 'Caminhonete',
            "Nome": self.nome,
            "Numero Do Chassi": self.numero_chassi,
            "Placa": self.placa,
            "Cpf Do Comprador" : self.cpf,
            "Valor" : self.valor,
            "Cor": self.cor,
            "Data Da Compra" : self.data
        }

    def venderVeiculo(self, veiculo, cpf, data, valor):
        self.cpf = input('Digite o Cpf: ')
        self.data = input('Digite a Data: ')
        self.valor = input('Digite o Valor: ')
        global veiculosDisponiveis
        global vendasCaminhonetes
        global veiculosVendidos
        super().venderVeiculo()
        vendasCaminhonetes.append(veiculo.__dict__())
        veiculosDisponiveis.pop(0)
        veiculosVendidos.append(veiculo.__dict__())
        print('Parabéns, Caminhonete Vendida!')

    def listarInformacoes(self):
        global carrosDisponiveis
        global vendasCaminhonetes
        super().listarInformacoes()
        print(f'Modelo : {caminhonete.nome}\n Placa : {caminhonete.placa}\n Chassi : {caminhonete.numero_chassi}')

    def alterarInformacoes(self):
        global vendasCaminhonetes
        super().alterarInformacoes()
        self.placa = input('Informe a Placa Que Deseja Pesquisar : ')
        self.novoValor = input('Informe o Novo Valor : ')
        self.novaCor = input('Informe a Nova Cor : ')
        for i in vendasCaminhonetes:
            if i["Placa"] == self.placa:
                i["Valor"] = self.novoValor
                i["Cor"] = self.novaCor

    def listarVeiculos(self):
        global vendasCaminhonetes
        print(vendasCaminhonetes)


moto = Moto_Triciclo('NMAX', 'XXX000', 'BRANCA', 150, 2)
triciclo = Moto_Triciclo('RAV', 'ZZZ555', 'PRETA', 300, 3)
moto2 = Moto_Triciclo('PCX', 'RRR555', 'AZUL', 160, 2)

carro = Carro('PRISMA', '000XXX', 'BRANCO', 4, 1600, True )
carro2 = Carro('KA', 'TTT333', 'PRETO', 4, 1400, True)
carro3 = Carro('ARGO', 'AAA444', 'AZUL', 4, 1000, True )

caminhonete = Caminhonete('S10', 'BBB555', 5, 10000, 4000, 'DIESEL')
caminhonete2 = Caminhonete('AMAROK', 'CCC444', 5, 10000, 4000, 'DIESEL')
caminhonete3 = Caminhonete('TORO', 'PPP777', 5, 5000, 3000, 'GASOLINA')

veiculosDisponiveis.append(moto)
veiculosDisponiveis.append(triciclo)
veiculosDisponiveis.append(moto2)
veiculosDisponiveis.append(carro)
veiculosDisponiveis.append(carro2)
veiculosDisponiveis.append(carro3)
veiculosDisponiveis.append(caminhonete)
veiculosDisponiveis.append(caminhonete2)
veiculosDisponiveis.append(caminhonete3)

transf = Transferencia()

Veiculo.menu()







