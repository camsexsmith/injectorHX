import json
import numpy as np
import InjectorClass as IN
import matplotlib.pyplot as plt


with open("input.json","r") as JSON:
    inData = json.load(JSON)

InjObj = IN.Inj(inData)

T0 = 300
dt = 0.1

R = 1/InjObj.HHot + InjObj.thick/InjObj.K + 1/InjObj.HCold

tspan = np.arange(0,20,dt)

T = [T0]
for n in range(np.size(tspan)):

    qpp = (InjObj.CombTemp - InjObj.FuelTemp) / R
    Tnew = T[n] + qpp*dt/(InjObj.rho*InjObj.thick*InjObj.C)
    T.append(Tnew)
    InjObj.FuelTemp = InjObj.FuelTemp + 3

T.pop()

fig1, ax1 = plt.subplots()
ax1.plot(tspan,T)
ax1.set_title('Injector Temperature vs Time')
ax1.set_ylabel('Temperature [K]')
ax1.set_xlabel('Time [s]')
ax1.grid(True)
plt.show()