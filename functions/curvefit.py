def KCurve(T):

    #SS304 Conductivity W/m-K
    if T > 1100:
        K = 25.9
    elif T < 150:
        K = 10.5
    else:
        #Valid for temp 150K to 1130K
        #Taken from milspec data
        K = 0.00000001*T**3 - 0.00003288*T**2 + 0.03595963*T + 6.75493946

    return K

def alphaCurve(T):

    if T > 2500:
        alpha = 7.8e-3
    elif T < 0:
        alpha = 3.7e-3
    else:
        #Valid for temp range of 0K to 2500K
        #Taken from "Approximate Analytic Solutions of Transient Nonlinear Heat Conduction with Temperature-Dependent Thermal Diffusivity"
        alpha = (2e-6)*T + 0.0037

    return alpha