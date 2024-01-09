from classes.Usuario import Usuario
from pytest import mark

class TestClass:
    @mark.testes_usuario
    def test_quando_idade_recebe_09_11_1993_deve_retornar_o_valor_de_30(self):
        #Given-Contexto
        entrada = '09/11/1993' 
        esperado = 30
        
        usuario_teste = Usuario("Filipe de Bianchi Andrade", 44060631884, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, entrada)
        
        #When-ação
        resultado = usuario_teste.idade()
        
        #Then-desfecho
        assert resultado == esperado
    
    @mark.testes_usuario
    def test_quando_o_nome_recebe_filipe_de_bianchi_andrade_deve_retornar_apenas_andrade(self):
        #Given-Contexto
        entrada = 'Filipe de Bianchi Andrade'
        esperado = 'Andrade'
        
        usuario_teste = Usuario(entrada, 44060631884, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, "09/11/1993")
        
        # When-ação
        resultado = usuario_teste.sobrenome()
        
        # Then-desfecho
        assert resultado == esperado
    
    @mark.testes_usuario 
    def test_verifica_se_usuario_eh_admin(self):
        # Given - Contexto
        entrada = True
        esperado = True
        
        usuario_teste = Usuario("Filipe de Bianchi Andrade", 44060631884, 71060639, "fbianchi.andrade@gmail.com", 5592984171672, "09/11/1993", entrada)
        
        # When-ação
        resultado = usuario_teste._is_admin()
        
        # Then-desfecho
        assert resultado == esperado       