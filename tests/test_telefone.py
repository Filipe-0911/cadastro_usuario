from classes.Usuario import Usuario
from classes.TelefonesBr import TelefonesBr
from pytest import mark

class TestClass:
    
    @mark.testes_telefone
    def test_quando_instanciar_a_classe_telefone_deve_retornar_o_telefone_no_padrao_br(self):
        entrada = 5592984171672
        esperado = TelefonesBr(entrada)
        
        usuario_teste = Usuario("Filipe de Bianchi Andrade", 44060631884, 71060639, "fbianchi.andrade@gmail.com", entrada, "09/11/1993")
        
        resultado = usuario_teste.telefone
        
        assert esperado == resultado