from classes.Documento import Documento
from classes.Acesso_cep import BuscaEndereco
from classes.Email import Email
from classes.Data import Datas
from classes.TelefonesBr import TelefonesBr
from datetime import datetime

class Usuario:
    def __init__(self, nome, documento, cep, email, telefone, data_nascimento=None, ehadmin=False, data=Datas()) -> None:
        self._nome = nome
        self._ehadmin = ehadmin
        self._documento = Documento.cria_documento(documento)
        self._cep = BuscaEndereco(cep)
        self._email = Email(email)
        self._data = data
        self._telefone = TelefonesBr(telefone)
        self._data_nascimento = data_nascimento
        
    @property
    def documento(self):
        return self._documento
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def email(self):
        return self._email
        
    def detalhar(self):
        return self.__dict__
    
    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split()
        return nome_quebrado[-1] #[-1] retorna sempre o último elemento da lista
    
    def idade(self):
        data_atual = datetime.today()
        data_nascimento = datetime.strptime(self._data_nascimento, '%d/%m/%Y')
        return ((data_atual - data_nascimento).days) // 365
    
    def _is_admin(self):
        return self._ehadmin
    
    def __str__(self) -> str:
        return self._format()
    
    def __repr__(self) -> str:
        return self.detalhar()
    
    def _format(self) -> str:
        return f"Nome: {self._nome}, Documento: {self._documento}, Email: {self._email}, Data de cadastro: {self._data}, Telefone: {self._telefone}, CEP: {self._cep}, Idade: {self.idade()}"