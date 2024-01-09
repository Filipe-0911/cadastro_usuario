from classes.Usuario import Usuario
from classes.Cnpj import Cnpj
from pytest import mark

class TestClass:
    
    @mark.testes_cnpj
    def test_quando_for_passado_um_cnpj_o_documento_deve_chamar_a_classe_cnpj(self):
        # Given-Contexto
        entrada = '00394460005887'
        esperado = Cnpj('00394460005887')
        
        usuario_teste = Usuario('Filipe de Bianchi Andrade', entrada, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, "09/11/1993")
        
        # When-ação
        resultado = usuario_teste.documento
        
        # Then-desfecho
        assert resultado == esperado