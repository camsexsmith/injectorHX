import json
import numpy as np
import InjectorClass as IN
import matplotlib.pyplot as plt

with open("input.json","r") as JSON:
    inData = json.load(JSON)

InjObj = IN.Inj(inData)

dt = 0.1
Ti = 300

Bi = InjObj.HHot*InjObj.thick/2/InjObj.K
BiInv = 1/Bi

print(BiInv)
tspan = np.arange(0,20,dt)
x = []
for n in range(np.size(tspan)):
    
    x.append(round(InjObj.alpha*tspan[n]/InjObj.thick**2,2))

    print(f'X - {x[n]}\t t - {round(tspan[n],2)}')

Y = 0.5

Tc = InjObj.CombTemp + (Ti - InjObj.CombTemp)*Y

print(Tc)