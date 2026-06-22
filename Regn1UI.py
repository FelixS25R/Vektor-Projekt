import tkinter as tk
from tkinter import *
from Vektor_math import *
from TestDraw_vektor import PlotVektor 
import matplotlib.pyplot as plt

def beregn():
    valgt = variable.get() #Henter valgt funktion fra dropdown menuen
    global v1, v2
    if valgt in ["længde2D", "enhedsvektor2D", "tværvektor2D", "kartesian til polær2D"]:
        v1 = [float(x1.get()), float(y1.get())]
        resultat = funktioner[valgt](v1) #Kald på funktioner der kun kræver en vektor
        if valgt in ["enhedsvektor2D", "tværvektor2D",]:
            PlotVektor(valgt, app, resultat,v1)
    elif valgt == "scalar2D":
        v1 = [float(x1.get()), float(y1.get())]
        Skalar = float(S.get())
        resultat = funktioner[valgt](v1, Skalar) #Dictinary kalder på funktion baseret på valgt funktion i dropdown menuen, og giver de nødvendige argumenter
        PlotVektor(valgt, app, resultat,v1)
    elif valgt in ["dot produkt2D", "vinkel mellem vektorer2D"]:
        v1 = [float(x1.get()), float(y1.get())]
        v2 = [float(x2.get()), float(y2.get())]
        resultat = funktioner[valgt](v1, v2)

    elif valgt in ["polær til kartesian2D"]:
        Længde = float(L.get())
        Vinkel = float(V.get())
        resultat = funktioner[valgt](Længde, Vinkel)
       # PlotVektor(valgt, app, resultat,v1,v2)

    elif valgt in ["plus3d", "minus3d", "scalar3d", "dot produkt3d", "længde3d", "vinkel mellem vektorer3d", "vektor produkt3d", "vektor projektion3d"]: #Funktioner der kræver 3D vektorer
        if valgt == "scalar3d":
            v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
            Skalar = float(S.get())
            resultat = funktioner[valgt](v1, Skalar)
            PlotVektor(valgt, app, resultat,v1)
        elif valgt == "længde3d":
            v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
            resultat = funktioner[valgt](v1)
        elif valgt in ["vinkel mellem vektorer3d","dot produkt3d"]:
            v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
            v2 = [float(x2.get()), float(y2.get()), float(z2.get())]
            resultat = funktioner[valgt](v1, v2)
        else:
            v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
            v2 = [float(x2.get()), float(y2.get()), float(z2.get())]
            resultat = funktioner[valgt](v1, v2)
            PlotVektor(valgt, app, resultat,v1,v2)
    
    elif valgt in ["enhedsvektor3d"]:
        v1 = [float(x1.get()), float(y1.get()), float(z1.get())]
        resultat = funktioner[valgt](v1)
        PlotVektor(valgt, app, resultat,v1)
    else: #Funktioner der kræver 2 vektorer, 
        v1 = [float(x1.get()), float(y1.get())]
        v2 = [float(x2.get()), float(y2.get())]
        resultat = funktioner[valgt](v1, v2)
        PlotVektor(valgt, app, resultat,v1,v2)
    
    svar.config(text=f"Resultat: {resultat}")

collum1= 40
collum2=350
collum3=700
collum4=1000

svarrækkke = 40


app = tk.Tk()
app.geometry("1300x700") 

app.configure(bg="grey")
############Vektor 1 input################
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
############################################
############Vektor 2 input################
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
######################################
###########scalar input################
skalar = tk.Label(app, text="indtast skalar:", font=("inconsolata   ", 16))
skalar.pack(pady=20)
skalar.place(x=collum3, y=20)

S = tk.Entry(app, font=("inconsolata", 16))
S.pack(pady=10)
S.place(x=collum3, y=60)
############################
#############længde input################
Længdeinput = tk.Label(app, text="indtast længde:", font=("inconsolata   ", 16))
Længdeinput.pack(pady=20)
Længdeinput.place(x=collum4, y=20)

L = tk.Entry(app, font=("inconsolata", 16))
L.pack(pady=10)
L.place(x=collum4, y=60)
############################
#############vinkel input################
Vinkelinput = tk.Label(app, text="indtast vinkel:", font=("inconsolata   ", 16))
Vinkelinput.pack(pady=20)
Vinkelinput.place(x=collum4, y=100)

V = tk.Entry(app, font=("inconsolata", 16))
V.pack(pady=10)
V.place(x=collum4, y=140)
############################
#########Beregn og resultat################
beregnKnap = tk.Button(app, text="beregn", font=("Arial", 16), command=lambda: beregn(),bg="green", fg="white", padx=10, pady=5)
beregnKnap.place(x=svarrækkke, y=250)

svar = tk.Label(app, font=("Arial", 16))
svar.pack(pady=20)
svar.place(x=svarrækkke, y=310)
############################################
############labels################################
x1label = tk.Label(app, text="x:", font=("inconsolata", 16))
x1label.pack(pady=10)  
x1label.place(x=collum1-30, y=60)   

y1label = tk.Label(app, text="y:", font=("inconsolata", 16))
y1label.pack(pady=10)
y1label.place(x=collum1-30, y=100)

z1label = tk.Label(app, text="z:", font=("inconsolata", 16))
z1label.pack(pady=10)
z1label.place(x=collum1-30, y=140)

x2label = tk.Label(app, text="x:", font=("inconsolata", 16))
x2label.pack(pady=10)  
x2label.place(x=collum2-30, y=60)

y2label = tk.Label(app, text="y:", font=("inconsolata", 16))
y2label.pack(pady=10)
y2label.place(x=collum2-30, y=100)

z2label = tk.Label(app, text="z:", font=("inconsolata", 16))
z2label.pack(pady=10)
z2label.place(x=collum2-30, y=140)
############################################
###########dropdown menu################
variable = tk.StringVar(app)
variable.set("Select Operation") # default value

w = tk.OptionMenu(app, variable, "plus2D", "minus2D", "scalar2D", "dot produkt2D", "længde2D", "vinkel mellem vektorer2D", "polær til kartesian2D", "kartesian til polær2D", "enhedsvektor2D", "tværvektor2D", "vektor projektion2D","plus3d", "minus3d", "scalar3d", "dot produkt3d", "længde3d", "vinkel mellem vektorer3d", "vektor produkt3d", "vektor projektion3d", "enhedsvektor3d")
w.pack()
w.place(x=svarrækkke, y=200)

funktioner = {
    "plus2D": VektorAddition2D,
    "minus2D": VektorSubtraktion2D,
    "scalar2D": VektorScalar2D,
    "dot produkt2D": DotProdukt2D,
    "længde2D": LængdeVektor2D,
    "vinkel mellem vektorer2D": VinkelMellem2Vektor2D,
    "polær til kartesian2D": PolærTilKartasian2D,
    "kartesian til polær2D": KartasianTilPolær2D,
    "enhedsvektor2D": Enhedsvektor2D,
    "tværvektor2D": TværVektor2D,
    "vektor projektion2D": VektorProjektion2D,
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

app.mainloop()