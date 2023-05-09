import os
import smtplib
from email.message import EmailMessage
import requests
from translate import Translator
import translate
from datetime import date

API_KEY = '311a5cfb2c7f684aef1e1ef1e96473c3'

class Cidade():

    lista_de_cidades = []

    def __init__(self,nome=str):

        self._cidade = nome
        self._dados = {}
        link = f'https://api.openweathermap.org/data/2.5/weather?q={self._cidade}&appid={API_KEY}&lang=pt_br&units=metric'
        object_link = requests.get(link)
        self._dados_objeto = object_link.json()

    def temperatura(self):

        dados_temp = {}

        dados_temp['Temperatura'] = round(self._dados_objeto['main']['temp'],1)
        dados_temp['Sensação'] = round(self._dados_objeto['main']['feels_like'],1)
        return dados_temp

    def umidade(self):
        return self._dados_objeto['main']['humidity']

    def clima(self):

        dados_clima = {}
        t = Translator(from_lang='english',to_lang='pt-br')
        grupo_climatico = t.translate(self._dados_objeto['weather'][0]['main'])

        dados_clima['Grupo Climatico'] = grupo_climatico
        dados_clima['Condição'] = self._dados_objeto['weather'][0]['description']
        return dados_clima

    def nuvens(self):
        return (self._dados_objeto['clouds']['all'])

    def dados(self):
        return self._dados_objeto

    def atualizar(self):
        
        link = f'https://api.openweathermap.org/data/2.5/weather?q={self._cidade}&appid={API_KEY}&lang=pt_br&units=metric'
        object_link = requests.get(link)
        self._dados_objeto = object_link.json()

    @staticmethod
    def atualizar_todas():

        for cidade in Cidade.lista_de_cidades:
            link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade._name}&appid={API_KEY}&lang=pt_br&units=metric'
            object_link = requests.get(link)
            cidade._dados_objeto = object_link.json()

    @staticmethod
    def adicionar(objeto):
        try:
            Cidade.lista_de_cidades.append(objeto)
        except:
            return None

    @staticmethod
    def remover(objeto):
        try:
            Cidade.lista_de_cidades.remove(objeto)
        except:
            return None

    @staticmethod
    def listar_cidades():

        lista_de_nomes = []

        for objeto in Cidade.lista_de_cidades:
            lista_de_nomes.append(objeto._cidade)

        return lista_de_nomes


    def alerta(self,mensagem):
        
        EMAIL = "pyweather@gmail.com"
        PASSWORD = "32254632bx!"

        msg = EmailMessage()
        msg['Subject'] = "Seu Alerta foi ativado!"
        msg['From'] = "pyweather@gmail.com"
        msg['To'] = "bryan12345788@gmail.com"
        msg.set_content(f"{mensagem}")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)
    
    def salvar(self):

        data_atual = date.today()
        d = data_atual.strftime('%d/%m/%Y')
        t = self.temperatura()
        c = self.clima()
        u = self.umidade()
        n = self.nuvens()

        temp = t["Temperatura"]
        sens = t["Sensação"]
        g_clima = c["Grupo Climatico"]
        clima = c["Condição"]

        try:

            nova_linha = []

            arquivo = open(self._cidade, "r", encoding="utf-8")
            
            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo}{d}")

            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo}{temp}")

            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo}{sens}")

            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo}{g_clima}")

            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo}{clima}")

            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo}{u}")

            conteudo = arquivo.readline()
            conteudo = conteudo.replace("\n",",")
            nova_linha.append(f"{conteudo},{n}")

            novos_dados = "\n".join(nova_linha)
            arquivo = open(self._cidade, "w", encoding="utf-8")
            arquivo.writelines(novos_dados)
            arquivo.close()

        except:
            with open(self._cidade, "w", encoding='utf-8') as arquivo:
                arquivo.write(f"DATA {d}\nTEMPERATURA {temp}\nSENSAÇÂO {sens}\nGRUPO CLIMATICO {g_clima}\nCONDIÇÂO {clima}\nUMIDADE {u}\nNUVENS {n}")

