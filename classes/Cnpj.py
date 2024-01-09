from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if len(documento) == 14:
            validade = self._cnpj_e_valido(documento)
            if validade:
                self.cnpj = documento
        else:
            raise ValueError("Quantidade de digitos inválida.")
    
    @staticmethod
    def _cnpj_e_valido(documento):
        validate_cnpj = CNPJ()
        if validate_cnpj.validate(documento):
            return True
        else:
            raise ValueError("CNPJ inválido.")
    
    def __str__(self) -> str:
        return self._format_cnpj()
    
    def __repr__(self) -> str:
        return self._format_cnpj()
    
    def _format_cnpj(self):    
        mask = CNPJ()
        return mask.mask(self.cnpj)
    
    def __eq__(self, other) -> bool:
        return self.cnpj == other.cnpj
    