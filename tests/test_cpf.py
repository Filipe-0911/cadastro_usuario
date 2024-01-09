from classes.Usuario import Usuario
from classes.Cpf import Cpf
from pytest import mark
import pytest

class TestClass:
    
    @mark.testes_cpf
    def test_quando_for_passado_um_cpf_o_documento_deve_chamar_a_classe_cpf(self):
        # Given-Contexto
        entrada = '44060631884'
        esperado = Cpf('44060631884')
        
        usuario_teste = Usuario('Filipe de Bianchi Andrade', entrada, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, "09/11/1993")
        
        # When-ação
        resultado = usuario_teste.documento
        
        # Then-desfecho
        assert resultado == esperado
        
    @mark.testes_cpf
    def test_quando_for_passado_um_valor_invalido_para_cpf_ele_retorna_value_error(self):
        entrada = '44444444444'

        #p tratar Exceptions DEVEMOS usar with pytest.raises(erro, match)
        with pytest.raises(ValueError, match="Quantidade de digitos inválida."): 
            cnpj_teste = Cpf(entrada)
            
            assert cnpj_teste
            
    @mark.testes_cpf
    def test_quando_for_passado_um_valor_menor_que_o_desejado_para_cpf_ele_retorna_value_error_init(self):
        entrada = '444444444'
        
        #p tratar Exceptions DEVEMOS usar with pytest.raises(erro, match)
        with pytest.raises(ValueError, match="CPF inválido."): 
            cnpj_teste = Cpf(entrada)
            
            assert cnpj_teste