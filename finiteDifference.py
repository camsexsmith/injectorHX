import json
import numpy as np
import InjectorClass as IC
import matplotlib.pyplot as plt
from functions import curvefit

with open('input.json','r') as JSON:
    inData = json.load(JSON)

with open('materials.json','r') as JSON:
    matData = json.load(JSON)

mat = '304SS'

I = IC.Injector(inData,matData,mat)

dt = 0.01
tspan = np.arange(0,15,dt)

nx = 5
Lvec = np.linspace(0,I.thick,nx)

dx = Lvec[1]-Lvec[0]

LHS = dx**2/(I.alpha*dt)
RHS = 2*(I.HHot*dx/I.K + 1)

Ti = 220
T = np.ones((len(tspan)+1,len(Lvec)))*Ti

for p in range(len(tspan)):
    
    for n in range(len(Lvec)):
        
        I.K = curvefit.KCurve(T[p,n])
        #I.alpha = curvefit.alphaCurve(T[p,n])
        if n == 0:
            T[p+1,n] = I.alpha*dt/dx**2*((dx**2/(I.alpha*dt) - 2*I.HHot*dx/I.K -2)*T[p,n] + 2*T[p,n+1] + 2*I.HHot*dx*I.CombTemp/I.K)

        elif n == len(Lvec)-1:
            T[p+1,n] = I.alpha*dt/dx**2*((dx**2/(I.alpha*dt) - 2*I.HCold*dx/I.K -2)*T[p,n] + 2*T[p,n-1] + 2*I.HCold*dx*I.FuelTemp/I.K)

        else:
            T[p+1,n] = (1 - (2*I.alpha*dt/dx**2))*T[p,n] + I.alpha*dt/dx**2*(T[p,n+1] + T[p,n-1])

if LHS >= RHS:
    print('Convergence satisfied')
else:
    print('Convergence failed')

T = T[:-1]
fig1, ax1 = plt.subplots()
ax1.plot(tspan,T[:,0]-273,label='Hot Wall Temp')
ax1.plot(tspan,T[:,2]-273,label='Mid Wall Temp')
ax1.plot(tspan,T[:,-1]-273,label='Cold Wall Temp')
#ax1.plot(tspan, [matData[mat] for _ in range(len(tspan))], linestyle='---')
ax1.set_title('Injector Temperature vs Time VARIABLE K')
ax1.set_ylabel('Temperature [C]')
ax1.set_xlabel('Time [s]')
ax1.grid(True)
ax1.legend()

plt.show()