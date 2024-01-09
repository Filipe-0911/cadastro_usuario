import requests

class BuscaEndereco:
    
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_valido(cep):
            self._cep = cep
        else:
            raise ValueError("CEP Inválido.")
        
    @property
    def cep(self):
        return self._cep
        
    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        return False
    
    def _format(self):
        return f"{self._cep[:5]}-{self._cep[5:]}"
    
    def __str__(self) -> str:
        return self._format()
    
    def __repr__(self) -> str:
        return self._format()
    
    def get_endereco(self):
        url = f"https://viacep.com.br/ws/{self._cep}/json/"
        resposta = requests.get(url)
        dados = resposta.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )