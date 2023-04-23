from .abstractChamado import AbstractChamado
from .tipoChamado import TipoChamado
from datetime import date as Date
from .cliente import Cliente
from .tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        self.__data = data
        self.__cliente = cliente
        self.__tecnico = tecnico
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__tipo = tipo

    @property
    def data(self) -> Date:
        return self.__data

    @data.setter
    def data(self, data: Date):
        self.__data = data

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def tecnico(self) -> Tecnico:
        return self.__tecnico

    @tecnico.setter
    def tecnico(self, tecnico: Tecnico):
        self.__tecnico = tecnico

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        self.__prioridade = prioridade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoChamado):
        self.__tipo = tipo
