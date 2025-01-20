import tkinter as tk

janela = tk.Tk()
janela.title ("Tarefa PyInstall")
janela.geometry("600x400")

imagem = tk.PhotoImage(file="images1.png")

logo = imagem.subsample(1,1)

mostrar_imagem = tk.Label(janela, image=logo)
mostrar_imagem.pack(pady=50)

mostrar_imagem.image = logo

def on_button_click():
    label.config(text="Bem Vindos Turma VOUCHER 140")

label = tk.Label(janela, text="OLÁ MUNDO")
label.pack(pady=10)

button = tk.Button(janela, text="Clique Aqui", command=on_button_click)
button.pack(pady=10)


janela.mainloop()


