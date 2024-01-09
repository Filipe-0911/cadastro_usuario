from classes.Documento import Documento
from pytest import mark
import pytest

class TestClass:
    @mark.testes_documento
    def test_cria_documento_e_obtem_value_error(self):
        entrada = "1111111111111"
        
        #p tratar Exceptions DEVEMOS usar with pytest.raises(erro, match)
        with pytest.raises(ValueError, match="Quantidade de dígitos incorreta."): 
            doc_teste = Documento.cria_documento(entrada)
            
            assert doc_teste