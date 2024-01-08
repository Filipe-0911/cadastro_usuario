import re
from typing import Any

class TelefonesBr:
    padrao_telefone = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})" 
    
    def __init__(self, telefone) -> None:
        telefone = str(telefone)
        if self._valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número inválido")    
    
    def _valida_telefone(self, telefone) -> bool:
        resposta = re.findall(self.padrao_telefone, telefone)

        if resposta:
            return True
        
        return False
    
    def _format(self):
        
        resposta = re.search(self.padrao_telefone, self.numero)
        numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        
        return numero_formatado
    
    def __str__(self) -> str:
        return self._format()
    
    def __repr__(self) -> str:
        return self._format()
        
        