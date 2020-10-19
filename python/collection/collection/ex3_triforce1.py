print ("quel taille de triangle de la triforce voulez vous?")
nbr=int(input())
i=0
nbrblanc=1
x=0
nbrstar=1

for i in range(nbr):
    nbrblanc=nbrblanc+2
nbr1=nbr
nbrblanc1=nbrblanc
x=0
for x in range (nbr1):
    star = ""
    for x in range (nbrblanc1):
        star=star+ ' '

    for x in range (nbrstar) :
        star=star+'*'
    nbrstar+=2

    nbrblanc1-=1
    print(star)
x=0
nbrstar = 1
for x in range (nbr):
    star = ""
    for x in range(nbrblanc//2 +1):
        star = star + ' '

    for x in range(nbrstar):
        star = star + '*'

    for x in range(nbrblanc -2):
        star = star + ' '

    for x in range(nbrstar):
        star = star + '*'
    nbrstar += 2
    nbrblanc -= 2
    print(star)




    