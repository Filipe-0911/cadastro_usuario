from classes.Usuario import Usuario
from classes.Cpf import Cpf

class TestClass:
    def test_quando_for_passado_um_cpf_o_documento_deve_chamar_a_classe_cpf(self):
        # Given-Contexto
        entrada = '44060631884'
        esperado = Cpf('44060631884')
        
        usuario_teste = Usuario('Filipe de Bianchi Andrade', entrada, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, "09/11/1993")
        
        # When-ação
        resultado = usuario_teste.documento
        
        # Then-desfecho
        assert resultado == esperado