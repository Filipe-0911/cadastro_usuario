from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento) -> None:
        documento = str(documento)
        
        if self._cnpj_e_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido.")
    
    def _cnpj_e_valido(self, documento):
        if len(documento) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida.")
    
    def __str__(self) -> str:
        return self._format_cnpj()
    
    def __repr__(self) -> str:
        return self._format_cnpj()
    
    def _format_cnpj(self):    
        mask = CNPJ()
        return mask.mask(self.cnpj)
    