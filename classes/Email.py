import re

class Email:
    padrao_email = r"\w{2,50}@\w{2,15}\.[a-z]{2,3}\.?([a-z]{2,3})?"
    
    def __init__(self, email) -> None:
        if self._valida_email(email):
            self._email = email
        else:
            raise ValueError("Número inválido")    
    
    def _valida_email(self, email) -> bool:
        resposta = re.findall(self.padrao_email, email)

        if resposta:
            return True
        
        return False
    
    def __str__(self) -> str:
        return self._email
    
    def __repr__(self) -> str:
        return self._email
        
        