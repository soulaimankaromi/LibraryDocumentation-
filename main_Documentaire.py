from Documentaire import Documentaire, Exemplaire
import copy
D1 = Documentaire("speed" ,"01/12/2023")
D2 = Documentaire("bisnes" ,"01/01/2023")
DC = copy.copy (D1)

print (D1.ToString())
print(D2.ToString())
print(D1.Eqauls(D2))
print (DC.ToString())

E2 = Exemplaire("speed" ,"01/12/2023","01/12/2023")
E4 = Exemplaire("bisnes" ,"01/01/2023","01/01/2023", 25487)

print (E2.ToString())
print(E4.ToString())
print(E2.Eqauls(E4))