print("Entrez la tailles de vote triforce")
taille=int(input())
for j in range (taille):
    print((2*taille-j)*" "+(2*j+1)*"*")
for j in range (taille):
    print((taille-j)*" "+(2*j+1)*"*"+(2*(taille-j)-1)*" "+(2*j+1)*"*")