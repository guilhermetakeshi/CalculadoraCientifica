# Importando a biblioteca
from future.moves import tkinter #necessario baixar o modulo future com o "pip install future"
import math

# Para fornecer funcionalidades
def click(val):
    e = entry.get()  # obtendo o valor do widget de entrada entry.
    ans = " " # Iniciando ans, que será usado para calcular o resultado da operação, como uma string vazia.

    try:
        # Para limpar o último texto inserido
        if val == "C":
            e = e[0:len(e) - 1]  # apagando o último valor inserido
            entry.delete(0, "end")
            entry.insert(0, e)
            return

        # Para apagar tudo
        elif val == "CE":
            entry.delete(0, "end")

        # Raiz quadrada
        elif val == "√":
            ans = math.sqrt(eval(e))

        # valor de pi
        elif val == "π":
            ans = math.pi

        # valor de cos
        elif val == "cosθ":
            ans = math.cos(math.radians(eval(e)))

        # valor de sen
        elif val == "sinθ":
            ans = math.sin(math.radians(eval(e)))

        # Valor de tangente
        elif val == "tanθ":
            ans = math.tan(math.radians(eval(e)))

        # valor de 2π 
        elif val == "2π":
            ans = 2 * math.pi

        # valor de coshiper
        elif val == "cosh":
            ans = math.cosh(eval(e))

        # valor de senhiper
        elif val == "sinh":
            ans = math.sinh(eval(e))

        # valor de tanhiper
        elif val == "tanh":
            ans = math.tanh(eval(e))

        # valor de raiz cúbica
        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)

        # x elevado à potência y
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return

        # valor do cubo
        elif val == "x\u00B3":
            ans = eval(e) ** 3

        # valor do quadrado
        elif val == "x\u00B2":
            ans = eval(e) ** 2

        # valor de ln
        elif val == "ln":
            ans = math.log2(eval(e))

        # valor em graus
        elif val == "deg":
            ans = math.degrees(eval(e))

        # valor em radianos
        elif val == "rad":
            ans = math.radians(eval(e))

        # valor de e
        elif val == "e":
            ans = math.e

        # valor de log10
        elif val == "log10":
            ans = math.log10(eval(e))

        # valor de fatorial
        elif val == "x!":
            ans = math.factorial(eval(e))

        # operador de divisão
        elif val == chr(247):
            entry.insert("end", "/")
            return

        elif val == "=":
            ans = eval(e)

        else:
            entry.insert("end", val)
            return

        entry.delete(0, "end")
        entry.insert(0, ans)

    except SyntaxError:
        pass


# Criando o objeto, inicializando uma janela TK que será a principal janela da nossa aplicação.
root = tkinter.Tk()

# Definindo o título e a geometria
root.title("Calculadora Científica")
root.geometry("680x486+100+100") # (largura x altura + posição x + posição y).

# Definindo a cor de fundo
root.config(bg="black")

# Campo de entrada
entry = tkinter.Entry(root, font=("arial", 20, "bold"), bg="black", fg="white", bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

'''
root – objeto janela

font – O estilo da fonte no qual queremos que as informações sejam inseridas

bg – Indicando a cor de fundo do espaço

fg – Informando a cor do texto que apareceu

bd – Borda do widget de entrada

width – largura do widget de entrada
'''

# lista de botões
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg",
               "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]

# Inicializando as variáveis r e c, que ajudarão a posicionar os botões na janela.
r = 1
c = 0

# Loop para obter os botões na janela
for i in button_list:
    # Botões
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i, bg="black", fg="white",
        font=("arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    # Isso é usado para posicionar os botões na janela em uma formação de grade. A cada iteração, a coluna c é incrementada
    # até passar de 7, neste momento, a linha r é incrementada e c é reiniciado.
    c += 1
    if c > 7:
        r += 1
        c = 0

# Mantém a janela em loop
root.mainloop()
