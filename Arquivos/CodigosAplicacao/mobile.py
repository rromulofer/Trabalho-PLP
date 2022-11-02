# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 28/10/22
# Ciência da Computação - UENF
# Disciplina: PLP

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

kivy.require('1.9.1')

var = 0
def soma_um(instance):
    global var
    var += 1
    instance.text = str(var)    
    
class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                padding=[40, 20, 40, 20])
        
        layout.add_widget(Label(text='Olá do Kivy!'))
        btn = Button(text='Pressione-me!', size=(100,50))
        
        btn.bind(on_press=soma_um)
        layout.add_widget(btn)
        return layout 
    
if __name__ == '__main__':
    MeuApp().run()