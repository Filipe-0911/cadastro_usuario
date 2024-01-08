from classes.Cnpj import Cnpj
from classes.Cpf import Cpf

class Documento(Cpf, Cnpj):
    
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento )== 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta.")