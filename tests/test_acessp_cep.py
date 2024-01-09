from classes.Acesso_cep import BuscaEndereco
import pytest
from pytest import mark

class TestClass:
    
    @mark.testes_cep
    def test_conecta_com_api_via_cep_e_busca_cep(self):
        # Given-Contexto
        entrada = 71060639
        esperado = '71060639'
        
        cep = BuscaEndereco(entrada)
        
        # When-Ação
        resultado = cep.cep
        
        # Then-desfecho
        assert esperado == resultado
        
    @mark.testes_cep
    def test_conecta_api_e_obtem_um_value_error(self):
        # Given-Contexto
        entrada = 9999999
        
        with pytest.raises(ValueError, match="CEP Inválido."): 
            cep = BuscaEndereco(entrada)
            
            assert cep
    
    @mark.testes_cep
    def test_obtem_dados_endereco_da_api_via_cep(self):
        # Given- Contexto
        entrada = 71060639
        esperado = (
            'Guará II',
            'Brasília',
            'DF'
        )
        
        endereco = BuscaEndereco(entrada)
        
        # When-Ação
        resultado = endereco.get_endereco()
        
        # Then-Desfecho
        assert resultado == esperado