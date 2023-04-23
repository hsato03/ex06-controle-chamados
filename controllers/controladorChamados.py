from .abstractControladorChamados import AbstractControladorChamados
from ..model.tipoChamado import TipoChamado
from ..model.chamado import Chamado
from datetime import date as Date
from ..model.cliente import Cliente
from ..model.tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return len(list(filter(lambda chamado: chamado.tipo.codigo == tipo.codigo, self.__chamados)))

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado) -> Chamado:
        if not (isinstance(cliente, Cliente)
                and isinstance(tecnico, Tecnico)
                and isinstance(tipo, TipoChamado)):
            return
        cadastrado = len(list(filter(lambda chamado: chamado.data == data
                                     or chamado.cliente.codigo == cliente.codigo
                                     or chamado.tecnico.codigo == tecnico.codigo
                                     or chamado.tipo.codigo == tipo.codigo
                                     or chamado.tipo.codigo,
                                     self.__chamados))) > 0
        if not cadastrado:
            self.__chamados.append(Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo))
            return self.__chamados[-1]

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        cadastrado = len(list(filter(lambda tipo: tipo.codigo == codigo, self.__tipos_chamados))) > 0
        if not cadastrado:
            self.__tipos_chamados.append(TipoChamado(codigo, descricao, nome))
            return self.__tipos_chamados[-1]

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
