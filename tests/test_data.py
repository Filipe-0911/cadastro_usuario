from datetime import datetime, timedelta
import datetime as dt
from classes.Data import Datas
from pytest import mark
import pytest

class TestClass:
    meses_do_ano = ['Janeiro', 'Fevereiro', 'Março' , 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubto', 'Novembro', 'Dezembro']
    dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    
    @mark.testes_data
    def test_cria_data_e_obtem_dia_da_semana(self):
        # Given
        entrada = datetime.today().weekday()
        esperado = self.dias_semana[entrada]
        
        # When
        resultado = Datas().dia_semana()
        
        # Then
        assert resultado == esperado
        
    @mark.testes_data
    def test_cria_data_e_obtem_mes_cadastro(self):
        # given
        entrada = datetime.today().month - 1
        esperado = self.meses_do_ano[entrada]
        # when
        resultado = Datas().mes_cadastro()
        # then
        assert resultado == esperado
    
    @mark.testes_data
    def test_cria_data_e_calcula_tempo_de_cadastro(self):
        # given
        data = dt.datetime(2024,1,9)
        entrada = Datas(data)
        esperado = entrada.tempo_cadastro().seconds
        # when
        resultado = entrada.tempo_cadastro().seconds
        # then
        assert resultado == esperado