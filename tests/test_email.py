from classes.Email import  Email
from classes.Usuario import Usuario
import pytest
from pytest import mark

class TestClass:
    
    @mark.testes_email
    def test_classe_email_deve_validar_se_email_e_valido(self):
        entrada = 'fbeltrano.ciclano@gmail.com'
        esperado = 'fbeltrano.ciclano@gmail.com'
        
        usuario_teste = Usuario('Fulano Beltrano Ciclano', 64252627028, 71060639, entrada, 5592999887766, "09/11/1993")
        resposta = usuario_teste.email
        
        assert esperado == resposta
        
    @mark.testes_email
    def test_classe_email_deve_validar_este_email_como_falso(self):
        entrada = 'fbeltrano.ciclano#gmail.com'
        
        #p tratar Exceptions DEVEMOS usar with pytest.raises(erro, match)
        with pytest.raises(ValueError, match="Email inválido"): 
            usuario_teste = Usuario('Fulano Beltrano Ciclano', 64252627028, 71060639, entrada, 5592984171672, "09/11/1993")
            
            assert usuario_teste