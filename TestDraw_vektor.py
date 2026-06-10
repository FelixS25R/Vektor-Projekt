import matplotlib.pyplot as plt
import Vektor_math as vk

def pltShow(Real: bool = True)->None:
    plt.grid()
    plt.autoscale(enable=Real,axis="both")
    plt.show()



def plotVektor(*args: list):
    #Check vektor type for 2D or 3D
    if len(args[1]) == 2: #2D vektor
            for vec in args:
                plt.arrow(0,0,*vec,length_includes_head=True)
            pltShow()
    
    if len(args[0]) == 3: #3D vektor
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

#def plotVektor3D(*args: list):
plotVektor([3,2,2],[4,-2,5],[-6,-8,4])
"""
def drawVektorAdd(v1,v2):
    for i in [v1,v2,vk.VektorAddition2D(v1,v2)]:
        plt.arrow(0,0,*i,length_includes_head=True)
    pltShow()

def drawVektorSub(v1,v2):
    for i in [v1,v2,vk.VektorSubtraktion2D(v1,v2)]:
        plt.arrow(0,0,*i,length_includes_head=True)
    pltShow()

fe([3,4],[2,-10],[3,9])
"""