import tkinter as tk

colllum1= 10





app = tk.Tk()

app.geometry("800x300") 

vektor1 = tk.Label(app, text="indtast vektor 1:", font=("Arial", 16))
vektor1.pack(pady=20)
vektor1.place(x=colllum1, y=20)

x1 = tk.Entry(app)
x1.place(x=colllum1, y=60)

app.mainloop()