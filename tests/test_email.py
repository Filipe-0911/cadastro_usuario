from classes.Email import  Email
from classes.Usuario import Usuario
import pytest

class TestClass:
    
    def test_classe_email_deve_validar_se_email_e_valido(self):
        entrada = 'fbianchi.andrade@gmail.com'
        esperado = Email._valida_email(entrada)
        
        usuario_teste = Usuario("Filipe de Bianchi Andrade", 44060631884, 71060639, entrada, 5592984171672, "09/11/1993")
        
        resposta = usuario_teste.email
        
        assert esperado == True
        

    def test_classe_email_deve_validar_este_email_como_falso(self):
        entrada = 'fbianchi.andrade#gmail.com'
        
        with pytest.raises(ValueError, match="Email inválido"):
            usuario_teste = Usuario("Filipe de Bianchi Andrade", 44060631884, 71060639, entrada, 5592984171672, "09/11/1993")
