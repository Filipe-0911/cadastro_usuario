from classes.Usuario import Usuario
from classes.TelefonesBr import TelefonesBr
from pytest import mark
import pytest

class TestClass:
    
    @mark.testes_telefone
    def test_quando_instanciar_a_classe_telefone_deve_retornar_o_telefone_no_padrao_br(self):
        # Given
        entrada = 5592999887766
        esperado = TelefonesBr(entrada)
        
        usuario_teste = Usuario('Fulano Beltrano Ciclano', 64252627028, 71060639, 'fbeltrano.ciclano@gmail.com', entrada, "09/11/1993")
        
        # When
        resultado = usuario_teste.telefone
        # Then
        assert esperado == resultado
        
    @mark.testes_telefone
    def test_insere_numero_telefone_sem_ddd_e_obtem_value_error(self):
        entrada = 999887766
        with pytest.raises(ValueError, match="Número inválido"):
            tel_teste = TelefonesBr(entrada)
            
            assert tel_teste