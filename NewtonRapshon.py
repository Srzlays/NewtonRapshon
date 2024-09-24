#---¡THIS-IS-A-SIMPLE-PROGRAM-TO-CALCULATE-
#----THE-ROOTS-OF-A-FUNTION-USING-A-NEWTON-RAPSHON-METHOD¡

#---¡IMPORT-LOCALS!
import functions as FUNCITONS

#---¡IN-THIS-LIST-WE-ADD-THE-ROOT!
X = []
#---¡NEWTON-RAPSHON-METHOD!
def Xn1(xn1, n):
    for i in range(n+1):
        xi = xn1
        fxn = FUNCITONS.f(xi)
        dfxn = FUNCITONS.df(xi)
        xn1 = xi - (fxn / dfxn)
        X.append(xn1)
        i += 1
        #print(f"When the {i} iteration the root is: {xn1}")

