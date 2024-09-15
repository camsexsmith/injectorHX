class Inj:

    def __init__(self,JSON) -> None:
        
        InjJSON = JSON["injector"]
        self.K = InjJSON["Conductivity"]
        self.rho = InjJSON["Density"]
        self.HHot = InjJSON["HTC Hot"]
        self.HCold = InjJSON["HTC Cold"]