def affichage_list(list):
    print(list)

def fusion(gauche ,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
            print(resultat,'resultat gauche')
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
            print(resultat, 'resultat droite')
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat

def tri_fusion(m):
    if len(m) <= 1:
        return m
    millieu = len(m) // 2
    return fusion(tri_fusion(m[:millieu]), tri_fusion(m[millieu:]))

list_base = [20, 3, 5, 21, 20, 12, 42, 30, 5, 9, 13, 18, 5]
affichage_list(list_base)
list_trier=tri_fusion(list_base)
affichage_list(list_trier)