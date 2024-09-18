from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

# Cada aplicación Kivy es una clase descendiente de la clase kivy.app.App
class TriquiApp(App):
    turno=0

    def build(self):
        # Indica si juega el primer jugador o el segundo
        self.primer_jugador = True
        tablero = GridLayout(rows=3, cols=3)
        for i in range(9):
            casilla = Button(text=str(i+1), font_size=40)
            casilla.bind(on_press=self.jugar)
            tablero.add_widget(casilla)
        return tablero

    # Callback que se llama cuando hacen click en una casilla
    def jugar(self, sender):
        print("Hicieron click en una casilla: " + sender.text)
        if sender.text != "0" and sender.text != "X":
            if self.turno == 0:
                sender.text = "0"
                self.turno = 1
                print("boff")
            elif self.turno ==1:
                sender.text = "X"
                self.turno = 0
                print("epa")
        else:
            print("No se puede jugar en una casilla ocupada")
            return
        self.primer_jugador = not(self.primer_jugador)
        # Tareas
        # 1. Intercambiar entre X y 0
        # 2. No permitir jugsr sobre una casilla ocupada

if __name__ == "__main__":
    TriquiApp().run()