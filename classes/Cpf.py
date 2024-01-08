from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)

        if self._cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")
        
    def _cpf_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida.")
    
    def __str__(self) -> str:
        return self._format_cpf()
    
    def __repr__(self) -> str:
        return self._format_cpf()
    
    def _format_cpf(self):    
        mask = CPF()
        return mask.mask(self.cpf)