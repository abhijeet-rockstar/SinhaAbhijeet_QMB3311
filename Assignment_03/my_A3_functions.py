def CESutility(x: float, y: float, r: float) ->float:
    u = (x**r) + (y**r)
    i = 1/r
    return u**i

def CESutility_value(x: float, y: float, r: float) ->float:
    if x >= 0 and y >= 0 and r > 0:
        u = (x**r) + (y**r)
        i = 1/r
        return u**i
    else:
        print ("wrong input")
        return None
    
def CESutility_in_budget(x: float, y: float, r: float, px: float, py: float, w: float) -> float:
    if w >= ((px * x) + (py * y)):
        CESutility_value(x,y,r)
    else:
        print ("it is out of your budget constrant")
        return None
    
