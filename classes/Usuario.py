from classes.Documento import Documento
from classes.Acesso_cep import BuscaEndereco
from classes.Email import Email
from classes.Data import Datas
from classes.TelefonesBr import TelefonesBr
from datetime import datetime

class Usuario:
    def __init__(self, nome, documento, cep, email, telefone, data_nascimento=None) -> None:
        self._nome = nome
        self._documento = Documento.cria_documento(documento)
        self._cep = BuscaEndereco(cep)
        self._email = Email(email)
        self._data = Datas()
        self._telefone = TelefonesBr(telefone)
        self._data_nascimento = data_nascimento
        
    def detalhar(self):
        return self.__dict__
    
    def idade(self):
        data_atual = datetime.today()
        data_nascimento = datetime.strptime(self._data_nascimento, '%d/%m/%Y')
        return ((data_atual - data_nascimento).days) // 365
    
    def __str__(self) -> str:
        return self._format()
    
    def __repr__(self) -> str:
        return self.detalhar()
    
    def _format(self) -> str:
        return f"Nome: {self._nome}, Documento: {self._documento}, Email: {self._email}, Data de cadastro: {self._data}, Telefone: {self._telefone}, CEP: {self._cep}, Idade: {self.idade()}"