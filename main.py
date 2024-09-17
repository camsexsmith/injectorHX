import json
import math
import numpy as np
import InjectorClass as IN


with open("input.json","r") as JSON:
    inData = json.load(JSON)

InjObj = IN.Inj(inData)

R = 1/InjObj.HHot + InjObj.thick/InjObj.K + 1/InjObj.HCold

qpp = (InjObj.CombTemp - InjObj.FuelTemp) / R

print(qpp)