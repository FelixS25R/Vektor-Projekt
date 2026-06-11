# Reference sheet for Vektor_math.py
#
# Format:
# FunktionNavn(parameter1, parameter2) -> returnerer
#     Kort forklaring
#     Eksempel


################ Vektor 2D ################

# VektorAddition2D(v1: list, v2: list) -> list
#     Lægger to 2D-vektorer sammen.
#     Formel: [v1.x + v2.x, v1.y + v2.y]
#     Eksempel: VektorAddition2D([2, 3], [4, 1]) -> [6, 4]
# VektorAddition2D
# Lægger to 2D-vektorer sammen.

# VektorSubtraktion2D(v1: list, v2: list) -> list
#     Trækker v2 fra v1.
#     Formel: [v1.x - v2.x, v1.y - v2.y]
#     Eksempel: VektorSubtraktion2D([5, 4], [2, 1]) -> [3, 3]
# VektorSubtraktion2D
# Trækker en 2D-vektor fra en anden 2D-vektor.

# VektorScalar2D(v1: list, S: float) -> list
#     Ganger en 2D-vektor med en skalar S.
#     Formel: [v1.x * S, v1.y * S]
#     Eksempel: VektorScalar2D([2, 3], 4) -> [8, 12]
# VektorScalar2D
# Ganger en 2D-vektor med en skalar.

# DotProdukt2D(v1: list, v2: list) -> float
#     Finder prikproduktet mellem to 2D-vektorer.
#     Formel: v1.x * v2.x + v1.y * v2.y
#     Eksempel: DotProdukt2D([2, 3], [4, 1]) -> 11
# DotProdukt2D
# Finder prikproduktet mellem to 2D-vektorer.

# LængdeVektor2D(v1: list) -> float
#     Finder længden af en 2D-vektor.
#     Formel: sqrt(x^2 + y^2)
#     Eksempel: LængdeVektor2D([3, 4]) -> 5.0
# LængdeVektor2D
# Finder længden af en 2D-vektor.

# VinkelMellem2Vektor2D(v1: list, v2: list) -> float
#     Finder vinklen mellem to 2D-vektorer i grader.
#     Formel: acos(dot(v1, v2) / (|v1| * |v2|))
#     Eksempel: VinkelMellem2Vektor2D([1, 0], [0, 1]) -> 90.0
# VinkelMellem2Vektor2D
# Finder vinklen mellem to 2D-vektorer.

# PolærTilKartasian2D(Længde: float, Vinkel: float) -> list
#     Omdanner fra polære koordinater til kartesiske koordinater.
#     Formel: [Længde * cos(Vinkel), Længde * sin(Vinkel)]
#     OBS: Funktionen bruger Vinkel direkte i sin/cos, så vinklen skal være i radianer.
#     Eksempel: PolærTilKartasian2D(5, 0) -> [5.0, 0.0]
# PolærTilKartasian2D
# Omdanner polære koordinater til kartesiske koordinater i 2D.

# KartasianTilPolær2D(v1: list) -> tuple
#     Omdanner fra kartesiske koordinater til polære koordinater.
#     Returnerer: (længde, vinkel_i_grader)
#     Formel: (sqrt(x^2 + y^2), degrees(atan(x / y)))
#     Eksempel: KartasianTilPolær2D([3, 4]) -> (5.0, ca. 36.87)
# KartasianTilPolær2D
# Omdanner kartesiske koordinater til polære koordinater i 2D.

# PunktTilVektor2D(Punkt1: list, Punkt2: list) -> list
#     Laver en vektor fra Punkt1 til Punkt2.
#     Formel: [Punkt2.x - Punkt1.x, Punkt2.y - Punkt1.y]
#     Eksempel: PunktTilVektor2D([1, 2], [4, 6]) -> [3, 4]
# PunktTilVektor2D
# Laver en 2D-vektor fra et punkt til et andet punkt.

# Enhedsvektor2D(v1: list) -> list
#     Finder enhedsvektoren for en 2D-vektor.
#     Formel: [x / |v|, y / |v|]