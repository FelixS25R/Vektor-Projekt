import matplotlib.pyplot as plt
import Vektor_math as vk

def PltShow(Real: bool = True)->None:
    plt.grid()
    plt.autoscale(enable=Real,axis="both")
    plt.show()



def PlotVektor(vektor_name: str, *args: list):
    #Check vektor type for 2D or 3D
    if len(args[0]) == 2: #2D vektor
            for vec in args: plt.arrow(0,0,*vec,length_includes_head=True)
            PltShow()
    
    elif len(args[0]) == 3: #3D vektor
            fig = plt.figure()
            ax = fig.add_subplot(111,projection="3d")
            for vec in args: ax.quiver(0,0,0,*vec)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")
            ax.autoscale(enable=True,axis="both")
            
            ax.set_xlim(min(args[0][0],args[1][0],args[2][0])-1,max(args[0][0],args[1][0],args[2][0])+1)
            ax.set_ylim(min(args[0][1],args[1][1],args[2][1])-1,max(args[0][1],args[1][1],args[2][1])+1)
            ax.set_zlim(min(args[0][2],args[1][2],args[2][2])-1,max(args[0][2],args[1][2],args[2][2])+1)
            
            plt.show()
    else:
          print("Too many variables for a vektor, only 2D and 3D supported")
a = [0,2]
b = [6,3]
print(vk.VinkelMellem2Vektor2D(a,b))
