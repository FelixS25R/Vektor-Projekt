import tkinter as tk
from tkinter import *

collum1= 40
collum2=400



app = tk.Tk()
app.geometry("1000x500") 



variable = tk.StringVar(app)
variable.set("plus") # default value


w = tk.OptionMenu(app, variable, "plus", "minus", "gange")
w.pack()
w.place(x=350, y=170)




vektor1 = tk.Label(app, text="indtast vektor 1:", font=("Arial", 16))
vektor1.pack(pady=20)
vektor1.place(x=collum1, y=20)


vektor2 = tk.Label(app, text="indtast vektor 2:", font=("Arial", 16))
vektor2.pack(pady=20)
vektor2.place(x=collum2, y=20)



x1 = tk.Entry(app, font=("Arial", 16))
x1.pack(pady=10)
x1.place(x=collum1, y=60)

y1 = tk.Entry(app, font=("Arial", 16))
y1.pack(pady=10)
y1.place(x=collum1, y=100)



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









app.mainloop()