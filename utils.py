import bisect

# Routine that recursively interpolates basic python datatypes
def RecInterp(d1,d2,t):
    if   isinstance(d1, (int, long, float, complex)):
        return (1-t)*d1 + t*d2
    elif isinstance(d1, dict): 
        return dict((k,RecInterp(d1[k],d2[k],t)) for k in d1)
    elif isinstance(d1, tuple): 
        return tuple(RecInterp(v1,v2,t) for v1,v2 in zip(d1,d2))


def RetrieveInterpolated(dic,mass):
    if mass in dic: return dic[mass]

    masses = sorted(dic.keys())
    if mass < masses[0] or mass > masses[-1]:
        raise IndexError("Input mass out of range.")

    idx = bisect.bisect_left(masses,mass)
    low,high = masses[idx-1],masses[idx]
    t = (mass-low)/(high-low)
    
    return RecInterp(dic[low],dic[high],t)
