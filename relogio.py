from tkinter import *
from time import strftime

def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

# Criação da janela principal
janela = Tk()
janela.title("Relógio Digital Simples")

# Configuração do rótulo do relógio
rotulo_relogio = Label(
    janela,
    font=("Arial", 40, "bold"),
    background="black",
    foreground="white"
)
rotulo_relogio.pack(anchor="center")

# Iniciar a atualização do relógio
atualizar_relogio()

# Executar a interface
janela.mainloop()
