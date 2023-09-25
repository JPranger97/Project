def speed(u, a, t):
     v = u + a * t
     return(v)

def distance(u, a, t):
    s = u * t + 0.5 * a * t * t
    return(s)

def brakingTime(u, a):
    t = 0
    while speed(u, a, t) > 0:
        t += 1
    return(t)

def brakingDistance(u, a):
    t = brakingTime(u, a)
    return(distance(u, a, t))

def reactionDistance(u):
    t = 0.3
    a = 0
    return(distance(u, a, t))

def distanceBetweenCars(u, a):
    d = brakingDistance(u, a) + reactionDistance(u)
    return(d)

def safeDistanceBetweenCars(u, a):
    return(distanceBetweenCars(u, a) + 2)

def capacityTunnel(u, a, Lt):
    Lc = 4
    d = safeDistanceBetweenCars(u, a)
    capacity = int(Lt / (Lc + d))
    print(capacity)

def carsPerTimeUnit(u):
    Lc = 4
    a = 0
    t = 0
    d = safeDistanceBetweenCars(u, a) + Lc
    while distance(u, a, t) < d:
        t += 1
    print(t)
    print(60/t)

carsPerTimeUnit(8.3)











