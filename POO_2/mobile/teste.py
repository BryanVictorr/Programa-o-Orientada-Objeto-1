import requests
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class Aplicativo(App):

    def build(self):
        return GUI

    def on_start(self):

        self.root.ids["moeda_1"].text = f"Dólar R${self.cotacao('USD')})"
        self.root.ids["moeda_2"].text = f"Euro R${self.cotacao('EUR')}"
        self.root.ids["moeda_3"].text = f"Bitcoin R${self.cotacao('BTC')}"
        self.root.ids["moeda_4"].text = f"Ethereum R${self.cotacao('ETH')}"

    def cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic = requisicao.json()
        cotacao = dic[f"{moeda}BRL"]["bid"]
        return cotacao


Aplicativo().run()