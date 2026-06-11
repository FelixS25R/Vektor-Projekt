import tkinter as tk
from tkinter import *
from Vektor_math import *

from TestDraw_vektor import PlotVektor

import Draw_vektor as Draw
import matplotlib.pyplot as plt



collum1= 40
collum2=400
collum3=700

svarrækkke = 40


app = tk.Tk()
app.geometry("1200x700") 

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

z1 = tk.Entry(app, font=("inconsolata", 16))
z1.pack(pady=10)
z1.place(x=collum1, y=140)

vektor2 = tk.Label(app, text="indtast vektor 2:", font=("inconsolata", 16))
vektor2.pack(pady=20)
vektor2.place(x=collum2, y=20)

x2 = tk.Entry(app, font=("inconsolata", 16))
x2.pack(pady=10)
x2.place(x=collum2, y=60)

y2 = tk.Entry(app, font=("inconsolata", 16))
y2.pack(pady=10)
y2.place(x=collum2, y=100)

z2 = tk.Entry(app, font=("inconsolata", 16))
z2.pack(pady=10)
z2.place(x=collum2, y=140)
skalar = tk.Label(app, text="indtast skalar:", font=("inconsolata   ", 16))
skalar.pack(pady=20)
skalar.place(x=collum3, y=20)

S = tk.Entry(app, font=("inconsolata", 16))
S.pack(pady=10)
S.place(x=collum3, y=60)


variable = tk.StringVar(app)
variable.set("plus") # default value

w = tk.OptionMenu(app, variable, "plus", "minus", "scalar", "dot produkt", "længde", "vinkel mellem vektorer", "polær til kartesian", "kartesian til polær", "enhedsvektor", "tværvektor", "vektor projektion","plus3d", "minus3d", "scalar3d", "dot produkt3d", "længde3d", "vinkel mellem vektorer3d", "vektor produkt3d", "vektor projektion3d", "enhedsvektor3d")
w.pack()
w.place(x=svarrækkke, y=200)

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
    "vektor projektion": VektorProjektion2D,
    "plus3d": Vektor3DAddition,
    "minus3d": Vektor3DSubtraktion,
    "scalar3d": Vektor3DScalar,
    "dot produkt3d": VektorDotProdukt3D,
    "længde3d": LængdeVektor3D,
    "vinkel mellem vektorer3d": VinkelMellem2Vektor3D,
    "vektor produkt3d": VektorProdukt3D,
    "vektor projektion3d": VektorProjektion3D,
    "enhedsvektor3d": EnhedsVektor3D
}



def beregn():
    valgt = variable.get()

    if valgt in ["længde", "enhedsvektor", "tværvektor", "kartesian til polær"]:
        v1 = [float(x1.get()), float(y1.get())]
        resultat = funktioner[valgt](v1)

    elif valgt == "scalar":
        v1 = [float(x1.get()), float(y1.get())]
        Skalar = float(S.get())
        resultat = funktioner[valgt](v1, Skalar)
    
    elif valgt in ["polær til kartesian"]:
        Længde = float(S.get())
        Vinkel = float(S.get())
        resultat = funktioner[valgt](Længde, Vinkel)

    elif valgt in ["plus3d", "minus3d", "scalar3d", "dot produkt3d", "længde3d", "vinkel mellem vektorer3d", "vektor produkt3d", "vektor projektion3d"]:
        v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
        v2 = [float(x2.get()), float(y2.get()), float(z2.get())]
        if valgt == "scalar3d":
            Skalar = float(S.get())
            resultat = funktioner[valgt](v1, Skalar)
        else:
            resultat = funktioner[valgt](v1, v2)
    elif valgt in ["enhedsvektor3d"]:
        v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
        resultat = funktioner[valgt](v1)
    else:
        v1 = [float(x1.get()), float(y1.get())]
        v2 = [float(x2.get()), float(y2.get())]
        resultat = funktioner[valgt](v1, v2)
    print(resultat)
    svar.config(text=f"Resultat: {resultat}")

beregnKnap = tk.Button(app, text="beregn", font=("Arial", 16), command=lambda: beregn())
beregnKnap.place(x=svarrækkke, y=230)

svar = tk.Label(app, font=("Arial", 16))
svar.pack(pady=20)
svar.place(x=svarrækkke, y=280)



app.mainloop()