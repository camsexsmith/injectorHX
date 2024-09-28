class Injector:

    def __init__(self,JSONi,JSONm,mat) -> None:
        
        matJSON = JSONm[mat]
        self.K = matJSON['conductivity']
        self.rho = matJSON['rho']
        self.C = matJSON['specific heat']

        InjJSON = JSONi["injector"]
        self.HHot = InjJSON["HTC Hot"]
        self.HCold = InjJSON["HTC Cold"]
        self.CombTemp = InjJSON["Comb Temp"]
        self.FuelTemp = InjJSON["Fuel Temp"]
        self.thick = InjJSON["Thick"]

        self.alpha = self.K/(self.rho*self.C)