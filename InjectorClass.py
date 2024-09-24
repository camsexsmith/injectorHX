class Injector:

    def __init__(self,JSON) -> None:
        
        InjJSON = JSON["injector"]
        self.K = InjJSON["Conductivity"]
        self.rho = InjJSON["Density"]
        self.HHot = InjJSON["HTC Hot"]
        self.HCold = InjJSON["HTC Cold"]
        self.CombTemp = InjJSON["Comb Temp"]
        self.FuelTemp = InjJSON["Fuel Temp"]
        self.thick = InjJSON["Thick"]
        self.C = InjJSON["Specific Heat"]

        self.alpha = self.K/(self.rho*self.C)