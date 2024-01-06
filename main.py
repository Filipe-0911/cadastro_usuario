from classes.Documento import Documento
from classes.TelefonesBr import TelefonesBr
from classes.Email import Email
from classes.Data import Datas
from classes.Acesso_cep import BuscaEndereco

cep = BuscaEndereco(71060639)
bairro, cidade, uf = cep.get_endereco()
cpf = Documento.cria_documento("44060631884")
cnpj = Documento.cria_documento("61115052000106")
telefone = TelefonesBr("5592984171672")
email = Email("fbianchi.andrade@gmail.com")
data = Datas()

print(f"""
CPF: {cpf}
CNPJ: {cnpj}
Email: {email}
Telefone:{telefone}
Data cadastro: {data}
Dia da semana: {data.dia_semana()}
Cep: {cep}
Cidade: {cidade}
UF: {uf}
Bairro: {bairro}""")