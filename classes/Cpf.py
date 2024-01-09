from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if len(documento) == 11:
            if self._cpf_valido(documento):
                self.cpf = documento
        else:
            raise ValueError("CPF inválido.")
        
    def _cpf_valido(self, documento):
        validador = CPF()
        if validador.validate(documento):
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida.")
    
    def __str__(self) -> str:
        return self._format_cpf()
    
    def __repr__(self) -> str:
        return self._format_cpf()
    
    def __eq__(self, other) -> bool:
        return self.cpf == other.cpf
    
    def _format_cpf(self):    
        mask = CPF()
        return mask.mask(self.cpf)