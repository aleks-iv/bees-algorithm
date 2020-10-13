from math import pi, sqrt, cos, exp
from random import uniform, seed
import matplotlib.pyplot as plt

plt.style.use('ggplot')

seed(49)

def func(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2 #функція Химмельблау
    #return (x + 2*y - 7)**2 + (2*x + y - 5)**2 #функція Бута
    #return -20*exp(-0.2*sqrt(0.5*(x**2 + y**2))) - exp(0.5*(cos(2*pi*x) + cos(2*pi*y))) + exp(1) + 20 #функція Еклі

iterations = 40

ns = 50
nb = 20
ne = 5
nre = 10
nrb = 5
r = 1

graf_bee = []
graf_mk = []

#________________________________INIT________________________________

bees = {}
for i in range(ns):
    x = uniform(-5, 5)
    y = uniform(-5, 5)
    f = func(x, y)
    bees[f] = {'x':x, 'y':y}
    
elits = {}
bests = {}

for i in range(nb):
    if i < ne:
        elits[min(bees)] = bees[min(bees)]
    else:
        bests[min(bees)] = bees[min(bees)]
    del bees[min(bees)]

#________________________________MAIN________________________________

for iter in range(iterations):
    bees = {}

    for i in range(ns-nb):
        x = uniform(-5, 5)
        y = uniform(-5, 5)
        f = func(x, y)
        bees[f] = {'x':x, 'y':y}

    for bee in elits:
        forag = {'bee':bee, 'x':elits[bee]['x'], 'y':elits[bee]['y']}
        for i in range(nre):
            x = uniform(elits[bee]['x']-r, elits[bee]['x']+r)
            y = uniform(elits[bee]['y']-r, elits[bee]['y']+r)
            f = func(x, y)
            if f < forag['bee']: forag = {'bee':f, 'x':x, 'y':y}
        bees[forag['bee']] = {'x':forag['x'], 'y':forag['y']}
        
    for bee in bests:
        forag = {'bee':bee, 'x':bests[bee]['x'], 'y':bests[bee]['y']}
        for i in range(nrb):
            x = uniform(bests[bee]['x']-r, bests[bee]['x']+r)
            y = uniform(bests[bee]['y']-r, bests[bee]['y']+r)
            f = func(x, y)
            if f < forag['bee']: forag = {'bee':f, 'x':x, 'y':y}
        bees[forag['bee']] = {'x':forag['x'], 'y':forag['y']}

    elits = {}
    bests = {}
  
    for i in range(nb):
        if i < ne:
            elits[min(bees)] = bees[min(bees)]
        else:
            bests[min(bees)] = bees[min(bees)]
        del bees[min(bees)]

    graf_bee.append(min(elits))

print(min(elits), elits[min(elits)]['x'], elits[min(elits)]['y'])

for iter in range(iterations):
    temp = float('Inf')
    for i in range(ns+(nb-ne)*nrb + ne*nre):
        x = uniform(-5, 5)
        y = uniform(-5, 5)
        f = func(x, y)
        if f < temp: temp = f
    if graf_mk == [] or temp <= graf_mk[-1]:
        graf_mk.append(temp)
    elif temp > graf_mk[-1]:
        graf_mk.append(graf_mk[-1])
    else: print('Error!')         

plt.plot(graf_bee)
plt.plot(graf_mk)
plt.show() 
