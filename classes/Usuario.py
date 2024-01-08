from classes.Documento import Documento
from classes.Acesso_cep import BuscaEndereco
from classes.Email import Email
from classes.Data import Datas
from classes.TelefonesBr import TelefonesBr

class Usuario:
    def __init__(self, nome, documento, cep, email, telefone) -> None:
        self.nome = nome
        self.documento = Documento(documento)
        self.cep = BuscaEndereco(cep)
        self.email = Email(email)
        self.data = Datas()
        self.telefone = TelefonesBr(telefone)
        
    def detalhar(self):
        return self.__dict__
    
    def __str__(self) -> str:
        return self._format()
    
    def __repr__(self) -> str:
        return self.detalhar()
    
    def _format(self) -> str:
        return f"Nome: {self.nome}, Documento: {self.documento}, Email: {self.email}, Data de cadastro: {self.data}, Telefone: {self.telefone}, CEP: {self.cep}"