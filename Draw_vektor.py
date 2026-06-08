from matplotlib import pyplot as plt
import Vektor_math

def create_plt(width: float | int = 10, height: float | int = 10, min_x: float | int = -10, max_x: float | int = 10, min_y: float | int = -10, max_y: float | int = 10)->None:
    global fig, ax
    fig, ax = plt.subplots(figsize=(width, height))
    
def start_point(x:float | int = 0, y:float | int = 0)->float | int:
    start_pos = [x,y]
    return start_pos

def TegnVectorAdd(v1,v2,Stedvektor: bool = True)->None:
    create_plt()
    if not Stedvektor:
        start_pos=start_point()
    else:
        start_pos = [0,0]

    vec=Vektor_math.Vektor2DAddition(v1,v2)
    for vektor in [v1,v2,vec]:
        ax.quiver(*start_pos,*vektor,scale=1, angles='xy', scale_units='xy')

def TegnVectorSub(v1,v2,Stedvektor: bool = True)->None:
    create_plt()
    if not Stedvektor:
        start_pos=start_point()
    else:
        start_pos = [0,0]

    vec=Vektor_math.Vektor2DSubtraktion(v1,v2)
    ax.quiver(*start_pos,*vec,scale=1, angles='xy', scale_units='xy')

def TegnVectorScalar(v1,S,Stedvektor: bool = True)->None:
    create_plt()
    if not Stedvektor:
        start_pos=start_point()
    else:
        start_pos = [0,0]
    
    vec=Vektor_math.Vektor2DScalar(v1,S)
    ax.quiver(*start_pos,*vec,scale=1, angles='xy', scale_units='xy')

def main():
    
    vektor1 = [1,1]
    vektor2 = [1,1]
    TegnVectorAdd(vektor1, vektor2, Stedvektor=True)
    
    plt.show()
"""
if __name__ == "__main__":
    create_plt()
    main()
"""



x1 = 1
y1 = 1
x2 = 1
y2 = 8
vektor1 = [x1, y1]
vektor2 = [x2, y2]
TegnVectorAdd(vektor1, vektor2, Stedvektor=True)
plt.xlim(-10, 10)
plt.ylim(10, -10)
plt.show()    