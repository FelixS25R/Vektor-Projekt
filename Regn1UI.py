import tkinter as tk
from tkinter import *
import Vektor_math

collum1= 40
collum2=400



app = tk.Tk()
app.geometry("1000x500") 



vektor1 = tk.Label(app, text="indtast vektor 1:", font=("Arial", 16))
vektor1.pack(pady=20)
vektor1.place(x=collum1, y=20)



x1 = tk.Entry(app, font=("Arial", 16))
x1.pack(pady=10)
x1.place(x=collum1, y=60)

y1 = tk.Entry(app, font=("Arial", 16))
y1.pack(pady=10)
y1.place(x=collum1, y=100)




vektor2 = tk.Label(app, text="indtast vektor 2:", font=("Arial", 16))
vektor2.pack(pady=20)
vektor2.place(x=collum2, y=20)




x2 = tk.Entry(app, font=("Arial", 16))
x2.pack(pady=10)
x2.place(x=collum2, y=60)

y2 = tk.Entry(app, font=("Arial", 16))
y2.pack(pady=10)
y2.place(x=collum2, y=100)







v1=[x1, y1]
v2=[x2, y2]



beregn = tk.Button(app, text="beregn", font=("Arial", 16))
beregn.place(x=350, y=200)


variable = tk.StringVar(app)
variable.set("plus") # default value


w = tk.OptionMenu(app, variable, "plus", "minus", "scalar", "dot produkt", "længde", "vinkel mellem vektorer", "polær til kartesian", "kartesian til polær", "enhedsvektor", "tværvektor", "vektor projektion")
w.pack()
w.place(x=350, y=170)

funktioner = {
    "plus": VektorAddition2D,
    "minus": VektorSubtraktion2D,
    "scalar": SkalarMultiplikation2D,
    "dot produkt": DotProdukt2D,
    "længde": Laengde2D,
    "vinkel mellem vektorer": VinkelMellemVektorer2D,
    "polær til kartesian": PolærTilKartasian2D,
    "kartesian til polær": KartasianTilPolær2D,
    "enhedsvektor": Enhedsvektor2D,
    "tværvektor": TværVektor2D,
    "vektor projektion": VektorProjektion2D
}

def beregn():
    v1 = [float(x1.get()), float(y1.get())]
    v2 = [float(x2.get()), float(y2.get())]

    resultat = funktioner[variable.get()](v1, v2)
    print(resultat)




app.mainloop()