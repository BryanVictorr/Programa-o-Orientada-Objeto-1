from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operadores = ["/", "*", "+", "-"]
        self.ultimo_operador = None
        self.ultimo_botao = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solucao = TextInput(background_color = "black", foreground_color = "white", multiline=False, halign="right", font_size=55, readonly=True)

        main_layout.add_widget(self.solucao)
        botoes = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "c", "-"],
        ]

        for x in botoes:

            h_layout = BoxLayout()

            for label in x:

                botao = Button(
                    text = label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                botao.bind(on_press=self.on_button_press)
                h_layout.add_widget(botao)
            main_layout.add_widget(h_layout)

        igual_button = Button(
            text = "=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        igual_button.bind(on_press=self.on_solucao)
        main_layout.add_widget(igual_button)

        return main_layout

    def on_button_press(self, instancia):
        atual = self.solucao.text
        botao_text = instancia.text

        if botao_text == "c":
            self.solucao.text = ""
        else:
            if atual and (
                self.ultimo_operador and botao_text in self.operadores):
                return
            elif atual == "" and botao_text in self.operadores:
                return 
            else:
                novo_text = atual + botao_text
                self.solucao.text = novo_text
        self.ultimo_botao = botao_text
        self.ultimo_operador = self.ultimo_botao in self.operadores

    def on_solucao(self, instancia):
        text = self.solucao.text
        if text:
            solucao = str(eval(self.solucao.text))
            self.solucao.text = solucao 

if __name__ == "__main__":
    app = MainApp()
    app.run()