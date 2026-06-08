import matplotlib.pyplot as plt
import Vektor_math as vk

def pltShow(Real: bool = True)->None:
    plt.grid()
    plt.autoscale(enable=Real,axis="both")
    plt.show()

def drawVektorAdd(v1,v2):
    for i in [v1,v2,vk.VektorAddition2D(v1,v2)]:
        plt.arrow(0,0,*i,length_includes_head=True)
    plt.show()

def drawVektorSub(v1,v2):
    for i in [v1,v2,vk.VektorSubtraktion2D(v1,v2)]:
        plt.arrow(0,0,*i,length_includes_head=True)
    plt.show()

drawVektorSub([3,4],[2,-10])
