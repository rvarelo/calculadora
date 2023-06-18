from tkinter import *

root = Tk()
root.title("Sua Calculadora")
root.geometry("408x355")
root.minsize(408, 355)
root.maxsize(408, 355)

numero1 = ""
numero2 = ""
divisao = FALSE
multiplicacao = FALSE
subtracao = FALSE
adicao = FALSE
limpa = FALSE


root.configure(background="#282828")

e = Entry(
    root,
    width=15,
    borderwidth=4,
    relief=FLAT,
    fg="#ffffff",
    bg="#a7a28f",
    font=("futura", 25, "bold"),
    justify=CENTER,
)
e.grid(row=0, column=0, columnspan=4, pady=2)


# funcoes operadores
def botao_cick(num):
    e.insert(END, num)


def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_multiplicacao():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_adicao():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_limpa():
    e.delete(0, END)


def botao_igual():
    global subtracao
    global adicao
    global multiplicacao
    global divisao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisao = FALSE

divide = Button(
    root,
    text="/",
    padx=40,
    pady=20,
    command=botao_divisao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
divide.grid(row=0, column=4)

# primeira fileira
um = Button(
    root,
    text="1",
    padx=40,
    pady=20,
    command=lambda: botao_cick(1),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
um.grid(row=1, column=1)

dois = Button(
    root,
    text="2",
    padx=40,
    pady=20,
    command=lambda: botao_cick(2),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
dois.grid(row=1, column=2)

tres = Button(
    root,
    text="3",
    padx=46,
    pady=20,
    command=lambda: botao_cick(3),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
tres.grid(row=1, column=3)

multiplicacao = Button(
    root,
    text="*",
    padx=41,
    pady=20,
    command=botao_multiplicacao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
multiplicacao.grid(row=1, column=4)

# segunda fileira
quatro = Button(
    root,
    text="4",
    padx=40,
    pady=20,
    command=lambda: botao_cick(4),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
quatro.grid(row=2, column=1)

cinco = Button(
    root,
    text="5",
    padx=40,
    pady=20,
    command=lambda: botao_cick(5),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
cinco.grid(row=2, column=2)

seis = Button(
    root,
    text="6",
    padx=46,
    pady=20,
    command=lambda: botao_cick(6),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
seis.grid(row=2, column=3)

menos = Button(
    root,
    text="-",
    padx=42,
    pady=20,
    command=botao_subtracao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
menos.grid(row=2, column=4)

# terceira fileira
sete = Button(
    root,
    text="7",
    padx=40,
    pady=20,
    command=lambda: botao_cick(7),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
sete.grid(row=3, column=1)

oito = Button(
    root,
    text="8",
    padx=40,
    pady=20,
    command=lambda: botao_cick(8),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
oito.grid(row=3, column=2)

nove = Button(
    root,
    text="9",
    padx=46,
    pady=20,
    command=lambda: botao_cick(9),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
nove.grid(row=3, column=3)

mais = Button(
    root,
    text="+",
    padx=40,
    pady=20,
    command=botao_adicao,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
mais.grid(row=3, column=4)


# quarta fileira
zero = Button(
    root,
    text="0",
    padx=91,
    pady=20,
    command=lambda: botao_cick(0),
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
zero.grid(row=4, column=1, columnspan=2)

limpa = Button(
    root,
    text="C",
    padx=44,
    pady=20,
    command=botao_limpa,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
limpa.grid(row=4, column=3)

igual = Button(
    root,
    text="=",
    padx=40,
    pady=20,
    command=botao_igual,
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    bg="#320064",
    activebackground="#240046",
    relief=FLAT,
    font=("futura", 12, "bold"),
)
igual.grid(row=4, column=4)

root.mainloop()
