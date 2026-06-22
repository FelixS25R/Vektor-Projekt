import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def close_program(root):
    plt.close("all")
    root.quit()        
    root.destroy()   

def PltShow2D(tk_Window, fig, Real: bool = True)->None:
    plt.grid()
    plt.autoscale(enable=Real,axis="both")
    canvas = FigureCanvasTkAgg(fig, master=tk_Window)
    canvas.draw()
    canvas.get_tk_widget().place(x=400, y=200)
    
    

def PltShow3D(ax, fig, args, tk_Window)->None:
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        xs = [v[0] for v in args]
        ys = [v[1] for v in args]
        zs = [v[2] for v in args]

        margin = 1

        ax.set_xlim(min(0, min(xs)) - margin, max(0, max(xs)) + margin)
        ax.set_ylim(min(0, min(ys)) - margin, max(0, max(ys)) + margin)
        ax.set_zlim(min(0, min(zs)) - margin, max(0, max(zs)) + margin)

        ax.set_box_aspect([
        ax.get_xlim()[1] - ax.get_xlim()[0],
        ax.get_ylim()[1] - ax.get_ylim()[0],
        ax.get_zlim()[1] - ax.get_zlim()[0]
        ])
        canvas = FigureCanvasTkAgg(fig, master=tk_Window)
        canvas.draw()
        canvas.get_tk_widget().place(x=400, y=200)
        

def PlotVektor(vektor_name: str, tk_Window: object, *args: list):
    tk_Window.protocol("WM_DELETE_WINDOW", lambda: close_program(tk_Window)) #Nødvendigt for at lukke matplotlib i tkinter
    #Check vektor type for 2D or 3D
    if len(args[0]) == 2: #2D vektor
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.set_title(vektor_name)
            for vec in args: plt.arrow(0,0,*vec,length_includes_head=True,head_width=0.3, head_length=0.3)
            PltShow2D(tk_Window, fig, True)
    
    elif len(args[0]) == 3: #3D vektor
            fig = plt.figure()
            ax = fig.add_subplot(111,projection="3d")
            ax.set_title(vektor_name)
            for vec in args: ax.quiver(0,0,0,*vec)
            PltShow3D(ax, fig, args, tk_Window)
    else:
          print("Too many variables for a vektor, only 2D and 3D supported")
