from dicBrs import dicBrs
from utils import RetrieveInterpolated

def Br(mass):
    return RetrieveInterpolated(dicBrs,mass)
   
