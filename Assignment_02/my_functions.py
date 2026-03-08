def present_value(fv: float, R: float, T: float, p: int =1) -> float:
    """"fv: future value
    R: rate of return per year
    T: time
    P: compount period
        it will bring the future value into current form 
    """
    n = T * p
    i = R/p 
    
    pv = fv / (1+i)**n
    return pv

print(present_value(1000, 0.10,1))


def future_value(pv: float, r: float, t: float, p: int=1) -> float:
    i = r/p
    n = t * p
    fv = pv * (1+i)**n
    return fv

def revenue_function(q: float, p: float) -> float:
    return q * p

def total_cost(mc: float, fc: float, q: float) -> float:
    TC = (mc * (q**2)) + fc
    return TC

def CESutility(x: float, y: float, r: float) ->float:
    u = (x**r) + (y**r)
    i = 1/r
    return u**i
