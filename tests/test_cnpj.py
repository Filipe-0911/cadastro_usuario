from classes.Usuario import Usuario
from classes.Cnpj import Cnpj
from pytest import mark
import pytest

class TestClass:
    
    @mark.testes_cnpj
    def test_quando_for_passado_um_cnpj_o_documento_deve_chamar_a_classe_cnpj(self):
        # Given-Contexto
        entrada = '00394460005887'
        esperado = Cnpj('00394460005887')
        
        cnpj_teste = Usuario('Filipe de Bianchi Andrade', entrada, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, "09/11/1993")
        
        # When-ação
        resultado = cnpj_teste.documento
        
        # Then-desfecho
        assert resultado == esperado
    
    @mark.testes_cnpj
    def test_quando_for_passado_um_valor_invalido_para_cnpj_ele_retorna_value_error(self):
        entrada = '0039446000588'

        #p tratar Exceptions DEVEMOS usar with pytest.raises(erro, match)
        with pytest.raises(ValueError, match="Quantidade de digitos inválida."): 
            cnpj_teste = Cnpj(entrada)
            
            assert cnpj_teste
            
    @mark.testes_cnpj
    def test_quando_for_passado_um_valor_invalido_para_cnpj_ele_retorna_value_error_init(self):
        entrada = '00394460005884'
        
        #p tratar Exceptions DEVEMOS usar with pytest.raises(erro, match)
        with pytest.raises(ValueError, match="CNPJ inválido."): 
            cnpj_teste = Cnpj(entrada)
            
            assert cnpj_teste
    