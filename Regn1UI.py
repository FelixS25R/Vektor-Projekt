import tkinter as tk
from tkinter import *
from Vektor_math import *

collum1= 40
collum2=400
collum3=700


app = tk.Tk()
app.geometry("1000x500") 

app.configure(bg="grey")

vektor1 = tk.Label(app, text="indtast vektor 1:", font=("inconsolata", 16))
vektor1.pack(pady=20)
vektor1.place(x=collum1, y=20)

x1 = tk.Entry(app, font=("inconsolata", 16))
x1.pack(pady=10)
x1.place(x=collum1, y=60)

y1 = tk.Entry(app, font=("inconsolata", 16))
y1.pack(pady=10)
y1.place(x=collum1, y=100)

vektor2 = tk.Label(app, text="indtast vektor 2:", font=("inconsolata", 16))
vektor2.pack(pady=20)
vektor2.place(x=collum2, y=20)

x2 = tk.Entry(app, font=("inconsolata", 16))
x2.pack(pady=10)
x2.place(x=collum2, y=60)

y2 = tk.Entry(app, font=("inconsolata", 16))
y2.pack(pady=10)
y2.place(x=collum2, y=100)

skalar = tk.Label(app, text="indtast skalar:", font=("inconsolata   ", 16))
skalar.pack(pady=20)
skalar.place(x=collum3, y=20)

S = tk.Entry(app, font=("inconsolata", 16))
S.pack(pady=10)
S.place(x=collum3, y=60)


variable = tk.StringVar(app)
variable.set("plus") # default value


w = tk.OptionMenu(app, variable, "plus", "minus", "scalar", "dot produkt", "længde", "vinkel mellem vektorer", "polær til kartesian", "kartesian til polær", "enhedsvektor", "tværvektor", "vektor projektion")
w.pack()
w.place(x=350, y=170)

funktioner = {
    "plus": VektorAddition2D,
    "minus": VektorSubtraktion2D,
    "scalar": VektorScalar2D,
    "dot produkt": DotProdukt2D,
    "længde": LængdeVektor2D,
    "vinkel mellem vektorer": VinkelMellem2Vektor2D,
    "polær til kartesian": PolærTilKartasian2D,
    "kartesian til polær": KartasianTilPolær2D,
    "enhedsvektor": Enhedsvektor2D,
    "tværvektor": TværVektor2D,
    "vektor projektion": VektorProjektion2D
}



v1=[x1, y1]
v2=[x2, y2]

def beregn():

    

    valgt = variable.get()

    if valgt in ["længde", "enhedsvektor", "tværvektor", "kartesian til polær"]:
        v1 = [float(x1.get()), float(y1.get())]
        resultat = funktioner[valgt](v1)

    elif valgt == "scalar":
        v1 = [float(x1.get()), float(y1.get())]
        S = float(S.get())
        resultat = funktioner[valgt](v1, S)

    else:
        v1 = [float(x1.get()), float(y1.get())]
        v2 = [float(x2.get()), float(y2.get())]
        resultat = funktioner[valgt](v1, v2)

    print(resultat)

beregnKnap = tk.Button(app, text="beregn", font=("Arial", 16), command=lambda: beregn())
beregnKnap.place(x=350, y=200)




app.mainloop()