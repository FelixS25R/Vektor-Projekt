import math
#############Vektor 2D################
def VektorAddition2D(v1: list, v2: list):
    return [v1[0] + v2[0], v1[1] + v2[1]]
def VektorSubtraktion2D(v1: list, v2: list):
    return [v1[0] - v2[0], v1[1] - v2[1]]
def VektorScalar2D(v1: list, S: float):
    return [v1[0] * S, v1[1] * S]
def DotProdukt2D(v1: list, v2: list):
    return v1[0] * v2[0] + v1[1] * v2[1]
def LængdeVektor2D(v1: list):
    return math.sqrt(v1[0]**2+v1[1]**2)
def VinkelMellem2Vektor2D(v1: list,v2:list):
    return math.degrees(math.acos(DotProdukt2D(v1,v2)/(LængdeVektor2D(v1)*LængdeVektor2D(v2))))
def PolærTilKartasian2D(Længde: float, Vinkel: float):
    return [Længde*math.cos(Vinkel), Længde*math.sin(Vinkel)]
def KartasianTilPolær2D(v1: list):
    return LængdeVektor2D(v1), math.degrees(math.atan((v1[0]/v1[1])))
def PunktTilVektor2D(Punkt1:list, Punkt2:list):
    return [Punkt2[0] - Punkt1[0], Punkt2[1] - Punkt1[1]]
def Enhedsvektor2D(v1:list):
    return [v1[0]/LængdeVektor2D(v1), v1[1]/LængdeVektor2D(v1)]
def TværVektor2D(v1:list):
    return [-v1[0], v1[1]]
def VektorProjektion2D(v1:list,v2:list):
    scale = DotProdukt2D(v1, v2) / LængdeVektor2D(v2)**2
    return [v2[0] * scale, v2[1] * scale]

################Vektor 3D################
def Vektor3DAddition(v1: list, v2: list):
    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]
def Vektor3DSubtraktion(v1: list, v2: list):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]
def Vektor3DScalar(v1: list, S: float):
    return [v1[0] * S, v1[1] * S, v1[2] * S]
def VektorDotProdukt3D(v1: list, v2: list):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
def LængdeVektor3D(v1: list):
    return math.sqrt(v1[0]**2+v1[1]**2+v1[2]**2)
def VinkelMellem2Vektor3D(v1: list,v2:list):
    return math.degrees(math.acos(VektorDotProdukt3D(v1,v2)/(LængdeVektor3D(v1)*LængdeVektor3D(v2))))
def VektorProdukt3D(v1:list,v2:list):
    return [(v1[1]*v2[2]-v1[2]*v2[1]), (v1[2]*v2[0]-v1[0]*v2[2]), (v1[0]*v2[1]-v1[1]*v2[0])]
def VektorProjektion3D(v1,v2):
    scale = VektorDotProdukt3D(v1,v2) / LængdeVektor3D(v2)**2
    return [scale*v2[0],scale*v2[1],scale*v2[2]]
def EnhedsVektor3D(v1):
    length = LængdeVektor3D(v1)
    return [v1[0]/length,v1[1]/length,v1[2]/length]
