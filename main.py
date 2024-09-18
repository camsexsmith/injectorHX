import json
import math
import numpy as np
import InjectorClass as IN


with open("input.json","r") as JSON:
    inData = json.load(JSON)

InjObj = IN.Inj(inData)

T0 = 300
dt = 0.1

A = 0.01*0.01
V = InjObj.thick*A

R = 1/InjObj.HHot + InjObj.thick/InjObj.K + 1/InjObj.HCold

qpp = (InjObj.CombTemp - InjObj.FuelTemp) / R

tspan = np.arange(0,15,dt)

T = [T0]
for n in range(np.size(tspan)):

    Tnew = T[n] + qpp*A*dt/(InjObj.rho*V*InjObj.C)
    T.append(Tnew)

print(T)