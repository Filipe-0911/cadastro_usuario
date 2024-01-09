from classes.Usuario import Usuario
from pytest import mark
from classes.Data import Datas

class TestClass:
    @mark.testes_usuario
    def test_quando_idade_recebe_09_11_1993_deve_retornar_o_valor_de_30(self):
        #Given-Contexto
        entrada = '09/11/1993' 
        esperado = 30
        
        usuario_teste = Usuario('Fulano Beltrano Ciclano', 64252627028, 71060639, 'fbeltrano.ciclano@gmail.com', 5592999887766, entrada)
        
        #When-ação
        resultado = usuario_teste.idade()
        
        #Then-desfecho
        assert resultado == esperado
    
    @mark.testes_usuario
    def test_quando_o_nome_recebe_filipe_de_bianchi_andrade_deve_retornar_apenas_andrade(self):
        #Given-Contexto
        entrada = 'Fulano Beltrano Ciclano'
        esperado = 'Ciclano'
        
        usuario_teste = Usuario(entrada, 64252627028, 71060639, 'fbeltrano.ciclano@gmail.com', 5592999887766, "09/11/1993")
        
        # When-ação
        resultado = usuario_teste.sobrenome()
        
        # Then-desfecho
        assert resultado == esperado
    
    @mark.testes_usuario 
    def test_verifica_se_usuario_eh_admin(self):
        # Given - Contexto
        entrada = True
        esperado = True
        
        usuario_teste = Usuario('Fulano Beltrano Ciclano', 64252627028, 71060639, 'fbeltrano.ciclano@gmail.com', 5592999887766, "09/11/1993", entrada)
        
        # When-ação
        resultado = usuario_teste._is_admin()
        
        # Then-desfecho
        assert resultado == esperado
        
    @mark.testes_usuario
    def test_testando_funcao_detalhar_que_retorna_um_dict_do_usuario_instanciado(self):
        # given
        data = Datas()
        entrada = Usuario('Fulano Beltrano Ciclano', 64252627028, 71060639, 'fbeltrano.ciclano@gmail.com', 5592999887766, "09/11/1993", True)
        
        esperado = entrada.__dict__
        # When
        resposta = entrada.detalhar()
        
        # then
        assert resposta == esperado