from ex06.controllers.abstractControladorPessoas import AbstractControladorPessoas
from ..model.cliente import Cliente
from ..model.tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        cadastrado = len(list(filter(lambda cliente: cliente.codigo == codigo, self.__clientes))) > 0
        if not cadastrado:
            self.__clientes.append(Cliente(nome, codigo))
            return self.__clientes[-1]

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        cadastrado = len(list(filter(lambda tecnico: tecnico.codigo == codigo, self.__tecnicos))) > 0
        if not cadastrado:
            self.__tecnicos.append(Tecnico(nome, codigo))
            return self.__tecnicos[-1]

