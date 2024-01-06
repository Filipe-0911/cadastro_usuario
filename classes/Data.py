from datetime import datetime, timedelta

class Datas:
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()
        
    def mes_cadastro(self):
        meses_do_ano = ['Janeiro', 'Fevereiro', 'Março' , 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubto', 'Novembro', 'Dezembro']
        
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    def dia_semana(self):
        dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]
    
    def __str__(self) -> str:
        return self._format()
    
    def _format(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=3)) - self.momento_cadastro
        return tempo_cadastro
        