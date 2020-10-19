
def fibbonacci(i):
    if i>2:
        return i
    else:
        suite=fibbonacci(i-1)+fibbonacci(i-2)
        return suite

print("quel numéro de la suite de fibbonanci voulez vous")
try:
    nbr=int(input())
except ValueError:
    print("valeur incorrecte")
else:
    print(fibbonacci(nbr))